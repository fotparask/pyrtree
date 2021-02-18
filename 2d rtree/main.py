from rtree import *

z = 0

rect = Rectangle(3,10,2,8)
testBlock = RtreeBlock(rect, 'testBlock', None)

node = RtreeNode(None, 0, 0)

newTree = Rtree(node)

insertBlock(newTree, testBlock)

print(newTree.RtreeData[0].blocks[0].data)

deleteBlock(newTree,testBlock)

insertBlock(newTree, testBlock)

print(newTree.RtreeData[0].blocks[0].data)