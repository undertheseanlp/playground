import torch
from supar import BiaffineDependencyParser
from supar.utils import CoNLL

from wip_vlsp2020_dp.export.modules.model import BiaffineDependencyModel


# model = BiaffineDependencyModel(10, 10, 5)
#
# words = torch.tensor([[1, 2, 3, 4, 5]])
# feats = torch.tensor([[[2], [3], [1], [4], [5]]])
#
# output = model(words, feats)
# print(output)

args = type("Args", (object, ), {})()
args.feat = 'char'
args.build = False
model = BiaffineDependencyModel(10, 10, 10)
transform = CoNLL()
parser = BiaffineDependencyParser.build(path='dp/dp')
