# create by fanfan on 2019/5/29 0029

from triedTree.base_tried_tree import BaseTriedTree

sample_data_path = '../data/sample_tried_tree.csv'
tree = BaseTriedTree(sample_data_path)

sample_string = "我喜欢小米手机和香蕉"
entitys, types = tree.process(sample_string)
print(entitys,types)
assert '小米手机' in entitys[0]
assert 'phone' in types[0]