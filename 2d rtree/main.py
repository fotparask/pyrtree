import shapefile
from rtree import *

node = RtreeNode(None, 0, 0)

newTree = Rtree(node)

rect = Rectangle(3,10,2,8)
testBlock = RtreeBlock(rect, 'block1', None)
insertBlock(newTree, testBlock)
rect = Rectangle(10,82,3,6)
testBlock = RtreeBlock(rect, 'block2', None)
insertBlock(newTree, testBlock)
rect = Rectangle(76,98,5,9)
testBlock = RtreeBlock(rect, 'block3', None)
insertBlock(newTree, testBlock)
rect = Rectangle(34,45,1,8)
testBlock = RtreeBlock(rect, 'block4', None)
insertBlock(newTree, testBlock)
rect = Rectangle(80,85,6,8)
testBlock = RtreeBlock(rect, 'block5', None)
insertBlock(newTree, testBlock)
rect = Rectangle(4,8,3,7)
testBlock = RtreeBlock(rect, 'block6', None)
insertBlock(newTree, testBlock)
print("=================================================================")
print("Root Node contains blocks:",newTree.RtreeRoot.blocks[0].data,",",newTree.RtreeRoot.blocks[1].data,",",newTree.RtreeRoot.blocks[2].data)
print("Node number 1 contains blocks:",newTree.RtreeData[1].blocks[0].data,",",newTree.RtreeData[1].blocks[1].data)
print("Node number 2 contains blocks:",newTree.RtreeData[2].blocks[0].data,",",newTree.RtreeData[2].blocks[1].data,",",newTree.RtreeData[2].blocks[2].data)
print("Node number 3 contains blocks:",newTree.RtreeData[3].blocks[0].data)
print("=================================================================")



# sf = shapefile.Reader("ne_110m_coastline.shp")
# shapes = sf.shapes()
# print("==============================================================")
# for x in shapes[0].points:
#     print(x)
# print("==============================================================")
# for x in shapes[1].points:
#     print(x)
# print("==============================================================")
# for x in shapes[2].points:
#     print(x)
# print("==============================================================")
