#include <windows.h>
#include <iostream>
#include <random>
#include <chrono>

const int MIN_DELAY_MS = 50;  
const int MAX_DELAY_MS = 200; 

/*Heuristic script which is written with core functionality, note that it cannot be used in CS2*/
const int HOLD_TIME_MS = 50; 

//std::random_device rd;
//std::mt19937 gen(rd());
//std::uniform_int_distribution<> dis(MIN_DELAY_MS, MAX_DELAY_MS);

void simulateKeyPressWithHold(char key, int holdTimeMs) {
    INPUT inputs[2] = { 0 };

    inputs[0].type = INPUT_KEYBOARD;
    inputs[0].ki.wVk = key;
    inputs[0].ki.dwFlags = 0;
    SendInput(1, inputs, sizeof(INPUT));

    Sleep(holdTimeMs);

    inputs[1].type = INPUT_KEYBOARD;
    inputs[1].ki.wVk = key;
    inputs[1].ki.dwFlags = KEYEVENTF_KEYUP; 
    SendInput(1, inputs + 1, sizeof(INPUT));
}

LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT* pKeyboard = (KBDLLHOOKSTRUCT*)lParam;
        if (wParam == WM_KEYUP || wParam == WM_SYSKEYUP) {
           if (!(pKeyboard->flags & LLKHF_INJECTED)) {
                char keyToPress = 0;
                if (pKeyboard->vkCode == 'A') {
                    keyToPress = 'D';
                }
                else if (pKeyboard->vkCode == 'D') {
                    keyToPress = 'A';
                }

                if (keyToPress != 0) {
                   //int delay = dis(gen);
                   // Sleep(delay);
                    simulateKeyPressWithHold(keyToPress, HOLD_TIME_MS);
                }
            }
        }
    }
    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int main() {
    HHOOK hHook = SetWindowsHookEx(WH_KEYBOARD_LL, LowLevelKeyboardProc, GetModuleHandle(NULL), 0);
    if (hHook == NULL) {
        std::cerr << "error in hooking" << std::endl;
        return 1;
    }

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(hHook);
    return 0;
}
