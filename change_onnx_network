import onnx

def scrfd_modify_onnx():
    onnx_model = onnx.load(r'Z:\scrfd_convert\insightface\detection\scrfd\onnx/scrfd_2.5g_bnkps_shape288x512.onnx')
    graph = onnx_model.graph

    for node in graph.node:
        if node.name == 'Sigmoid_145':
            node.output[0] = 'o_score_8'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_score_8', onnx.TensorProto.FLOAT, [1, 4608, 1]))
        elif node.name == 'Reshape_149':
            node.output[0] = 'o_bbox_8'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_bbox_8', onnx.TensorProto.FLOAT, [1, 4608, 4]))
        elif node.name == 'Reshape_153':
            node.output[0] = 'o_kps_8'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_kps_8', onnx.TensorProto.FLOAT, [1, 4608, 10]))

        elif node.name == 'Sigmoid_169':
            node.output[0] = 'o_score_16'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_score_16', onnx.TensorProto.FLOAT, [1, 1152, 1]))
        elif node.name == 'Reshape_173':
            node.output[0] = 'o_bbox_16'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_bbox_16', onnx.TensorProto.FLOAT, [1, 1152, 4]))
        elif node.name == 'Reshape_177':
            node.output[0] = 'o_kps_16'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_kps_16', onnx.TensorProto.FLOAT, [1, 1152, 10]))

        elif node.name == 'Sigmoid_193':
            node.output[0] = 'o_score_32'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_score_32', onnx.TensorProto.FLOAT, [1, 288, 1]))
        elif node.name == 'Reshape_197':
            node.output[0] = 'o_bbox_32'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_bbox_32', onnx.TensorProto.FLOAT, [1, 288, 4]))
        elif node.name == 'Reshape_201':
            node.output[0] = 'o_kps_32'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_kps_32', onnx.TensorProto.FLOAT, [1, 288, 10]))

    concat_score = onnx.helper.make_node('Concat', ['o_score_8', 'o_score_16', 'o_score_32'], ['concat_score'], name='concat_score', axis=1)
    concat_bbox = onnx.helper.make_node('Concat', ['o_bbox_8', 'o_bbox_16', 'o_bbox_32'], ['concat_bbox'], name='concat_bbox', axis=1)
    concat_kps = onnx.helper.make_node('Concat', ['o_kps_8', 'o_kps_16', 'o_kps_32'], ['concat_kps'], name='concat_kps', axis=1)
    graph.node.append(concat_score)
    graph.node.append(concat_bbox)
    graph.node.append(concat_kps)

    for i in range(len(graph.output)):
        graph.output.pop()
    graph.output.append(onnx.helper.make_tensor_value_info('concat_score', onnx.TensorProto.FLOAT, [1, 6048, 1]))
    graph.output.append(onnx.helper.make_tensor_value_info('concat_bbox', onnx.TensorProto.FLOAT, [1, 6048, 4]))
    graph.output.append(onnx.helper.make_tensor_value_info('concat_kps', onnx.TensorProto.FLOAT, [1, 6048, 10]))
    onnx.save(onnx_model, r'Z:\scrfd_convert\insightface\detection\scrfd\onnx/output.onnx')

'''
  将多个输出合并为3个 concat 输出, 针对ov框架进行适配
'''
def yolov5sDms_modify_onnx():
    onnx_model = onnx.load(r'D:\003 Models\modified_onnx/320_320_yolov5sRelu_0.667_v5.onnx')
    graph = onnx_model.graph

    for node in graph.node:
        if node.name == 'Mul_442':
            o_32_0 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_32_0"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_32_0', onnx.TensorProto.FLOAT, [1, 2, 3, 100]))
            graph.node.append(o_32_0)
        elif node.name == 'Mul_455':
            o_32_1 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_32_1"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_32_1', onnx.TensorProto.FLOAT, [1, 2, 3, 100]))
            graph.node.append(o_32_1)
        elif node.name == 'Slice_460':
            o_32_2 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_32_2"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_32_2', onnx.TensorProto.FLOAT, [1, 4, 3, 100]))
            graph.node.append(o_32_2)

        elif node.name == 'Mul_334':
            o_16_0 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_16_0"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_16_0', onnx.TensorProto.FLOAT, [1, 2, 3, 400]))
            graph.node.append(o_16_0)
        elif node.name == 'Mul_347':
            o_16_1 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_16_1"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_16_1', onnx.TensorProto.FLOAT, [1, 2, 3, 400]))
            graph.node.append(o_16_1)
        elif node.name == 'Slice_352':
            o_16_2 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_16_2"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_16_2', onnx.TensorProto.FLOAT, [1, 4, 3, 400]))
            graph.node.append(o_16_2)

        elif node.name == 'Mul_226':
            o_8_0 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_8_0"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_8_0', onnx.TensorProto.FLOAT, [1, 2, 3, 1600]))
            graph.node.append(o_8_0)
        elif node.name == 'Mul_239':
            o_8_1 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_8_1"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_8_1', onnx.TensorProto.FLOAT, [1, 2, 3, 1600]))
            graph.node.append(o_8_1)
        elif node.name == 'Slice_244':
            o_8_2 = onnx.helper.make_node("Transpose", inputs=["%s" % node.output[0]], outputs=["o_8_2"], perm=[0, 3, 1, 2])
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_8_2', onnx.TensorProto.FLOAT, [1, 4, 3, 1600]))
            graph.node.append(o_8_2)

    Concat_32 = onnx.helper.make_node('Concat', inputs=['o_32_0', 'o_32_1', 'o_32_2'], outputs=['Concat_32'], name='concat_score', axis=1)
    graph.value_info.append(onnx.helper.make_tensor_value_info('Concat_245', onnx.TensorProto.FLOAT, [1, 8, 100, 3]))
    graph.node.append(Concat_32)

    Concat_16 = onnx.helper.make_node('Concat', inputs=['o_16_0', 'o_16_1', 'o_16_2'], outputs=['Concat_16'], name='concat_score', axis=1)
    graph.value_info.append(onnx.helper.make_tensor_value_info('Concat_245', onnx.TensorProto.FLOAT, [1, 8, 400, 3]))
    graph.node.append(Concat_16)

    Concat_8 = onnx.helper.make_node('Concat', inputs=['o_8_0', 'o_8_1', 'o_8_2'], outputs=['Concat_8'], name='concat_score', axis=1)
    graph.value_info.append(onnx.helper.make_tensor_value_info('Concat_245', onnx.TensorProto.FLOAT, [1, 8, 1600, 3]))
    graph.node.append(Concat_8)

    for i in range(len(graph.output)):
        graph.output.pop()

    graph.output.append(onnx.helper.make_tensor_value_info('Concat_32', onnx.TensorProto.FLOAT, [1, 8, 3, 100]))
    graph.output.append(onnx.helper.make_tensor_value_info('Concat_16', onnx.TensorProto.FLOAT, [1, 8, 3, 400]))
    graph.output.append(onnx.helper.make_tensor_value_info('Concat_8', onnx.TensorProto.FLOAT, [1, 8, 3, 1600]))



    onnx.save(onnx_model, r'D:\003 Models\modified_onnx/modify_320_320_yolov5sRelu_0.667_v5.onnx')

def yoloxNonoCutCMS_onnx():
    onnx_model = onnx.load(r'Z:\ambarella\model_convert\models/512x288_yoloxNonoCutCMS_v2.onnx')
    graph = onnx_model.graph

    for node in graph.node:
        if node.name == 'Transpose_326':
            node.output[0] = 'o_score_32'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_score_32', onnx.TensorProto.FLOAT, [1, 288, 1]))
        elif node.name == 'Reshape_197':
            node.output[0] = 'o_bbox_32'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_bbox_32', onnx.TensorProto.FLOAT, [1, 288, 4]))
        elif node.name == 'Reshape_201':
            node.output[0] = 'o_kps_32'
            graph.value_info.append(onnx.helper.make_tensor_value_info('o_kps_32', onnx.TensorProto.FLOAT, [1, 288, 10]))

    concat_score = onnx.helper.make_node('Concat', ['o_score_8', 'o_score_16', 'o_score_32'], ['concat_score'], name='concat_score', axis=1)
    concat_bbox = onnx.helper.make_node('Concat', ['o_bbox_8', 'o_bbox_16', 'o_bbox_32'], ['concat_bbox'], name='concat_bbox', axis=1)
    concat_kps = onnx.helper.make_node('Concat', ['o_kps_8', 'o_kps_16', 'o_kps_32'], ['concat_kps'], name='concat_kps', axis=1)
    graph.node.append(concat_score)
    graph.node.append(concat_bbox)
    graph.node.append(concat_kps)

    for i in range(len(graph.output)):
        graph.output.pop()
    graph.output.append(onnx.helper.make_tensor_value_info('concat_score', onnx.TensorProto.FLOAT, [1, 6048, 1]))
    graph.output.append(onnx.helper.make_tensor_value_info('concat_bbox', onnx.TensorProto.FLOAT, [1, 6048, 4]))
    graph.output.append(onnx.helper.make_tensor_value_info('concat_kps', onnx.TensorProto.FLOAT, [1, 6048, 10]))
    onnx.save(onnx_model, r'Z:\scrfd_convert\insightface\detection\scrfd\onnx/output.onnx')

'''
 * 手掌检测
 * 原模型: 192_192_HandSmall_v0.onnx
'''
def HandSmall_modify_onnx():
    onnx_model = onnx.load(r'D:\003 Models/192_192_HandSmall_v0.onnx')
    node = onnx_model.graph.node

    # 修改输入为 1,3,192,192
    input = onnx_model.graph.input
    print("输入层属性: \n", input)
    input_dims = input[0].type.tensor_type.shape.dim
    input_dims[0].dim_value = 1
    input_dims[1].dim_value = 3
    input_dims[2].dim_value = 192
    input_dims[3].dim_value = 192

    # 删除 Transpose 层
    onnx_model.graph.node.remove(node[0])

    # 修改 conv 层输入为 input_1
    node[0].input[0] = 'input_1'

    onnx.save(onnx_model, r'D:\003 Models/192_192_HandSmall_change_v0.onnx')

'''
 * 手指关键点检测
 * 原模型: 192_192_HandSmall_v0.onnx
'''
def HandKeyPointSmall_modify_onnx():
    onnx_model = onnx.load(r'D:\003 Models/224_224_handKeyPointSmall_v0.onnx')
    node = onnx_model.graph.node

    # 修改输入为 1,3,192,192
    input = onnx_model.graph.input
    print("输入层属性: \n", input)
    input_dims = input[0].type.tensor_type.shape.dim
    input_dims[0].dim_value = 1
    input_dims[1].dim_value = 3
    input_dims[2].dim_value = 224
    input_dims[3].dim_value = 224

    # 删除 Transpose 层
    onnx_model.graph.node.remove(node[0])

    # 修改 conv 层输入为 input_1
    node[0].input[0] = 'input_1'

    onnx.save(onnx_model, r'D:\003 Models/224_224_handKeyPointSmallChange_v0.onnx')

if __name__ == "__main__":
    # scrfd_modify_onnx()
    # yolov5sDms_modify_onnx()
    # HandSmall_modify_onnx()
    HandKeyPointSmall_modify_onnx()
