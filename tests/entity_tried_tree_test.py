# create by fanfan on 2019/5/29 0029
from triedTree.patten_tried_tree import PattenTriedTree
from triedTree.entity_tried_tree import EntityTriedTree
if __name__ == '__main__':
    entity_folder = r'E:\company-work\nlu_core\data\sky_iot_control\entity'
    entity_obj = EntityTriedTree(entity_folder)

    pattern_folder =r'E:\company-work\nlu_core\data\sky_iot_control\intention'
    patten_obj = PattenTriedTree(pattern_folder)

    test_list = [
        '打开哈哈',
        '打开电洗衣机',
        '打开的洗衣机',
        '打开洗衣机吧',
        '帮我打开洗衣机吧',
    ]

    for content in test_list:
        print('\n')
        print("%s 句型匹配结果" % content)
        print(entity_obj.process_with_patten(content, patten_obj))

