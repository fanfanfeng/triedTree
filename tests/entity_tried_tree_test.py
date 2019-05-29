# create by fanfan on 2019/5/29 0029
from triedTree.patten_tried_tree import PattenTriedTree
from triedTree.entity_tried_tree import EntityTriedTree
if __name__ == '__main__':
    entity_folder = '../data/entity'
    entity_obj = EntityTriedTree(entity_folder)

    pattern_folder = '../data/intention'
    patten_obj = PattenTriedTree(pattern_folder)

    test_list = [
        '打开电洗衣机',
        '打开的洗衣机',
        '打开洗衣机吧',
        '帮我打开洗衣机吧',
    ]

    print(entity_obj.process('打开洗衣机'))
    for content in test_list:
        print('\n')
        print("%s 句型匹配结果" % content)
        print(entity_obj.process_with_patten(content, patten_obj))