from rtree import *

z = 0

rect = Rectangle(3,10,2,8)
testBlock = RtreeBlock(rect, 'testBlock', None)

node = RtreeNode(None, 0, 0)

newTree = Rtree(node)

insertBlock(newTree, testBlock)

print(node.blocks[0].data)
print(newTree.RtreeData[0].blocks[0].data)