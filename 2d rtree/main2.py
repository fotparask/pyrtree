import shapefile
from rtree import *

node = RtreeNode(None, 0, 0)

sf = shapefile.Reader("ne_110m_coastline.shp")
shapes = sf.shapes()
print("==============================================================")

newTree = Rtree(node)

temp = shapes[0].points[0]
print(temp)
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block1', None)
insertBlock(newTree, testBlock)
temp = shapes[0].points[1]
print(temp)
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block2', None)
insertBlock(newTree, testBlock)
temp = shapes[0].points[2]
print(temp)
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block3', None)
insertBlock(newTree, testBlock)
temp = shapes[0].points[3]
print(temp)
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block4', None)
insertBlock(newTree, testBlock)
temp = shapes[0].points[4]
print(temp)
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block5', None)
insertBlock(newTree, testBlock)
temp = shapes[0].points[5]
print(temp)
print("=================================================================")
print("Root Node contains blocks:",newTree.RtreeRoot.blocks[0].data,",",newTree.RtreeRoot.blocks[1].data)
print("Node number 1 has rectangle:",newTree.RtreeData[0].blocks[0].rect.x_min,",",newTree.RtreeData[0].blocks[0].rect.x_max,",",newTree.RtreeData[0].blocks[0].rect.y_min,",",newTree.RtreeData[0].blocks[0].rect.y_max)
print("Node number 1 contains blocks:",newTree.RtreeData[1].blocks[0].data,",",newTree.RtreeData[1].blocks[1].data)
print("Node number 2 contains blocks:",newTree.RtreeData[2].blocks[0].data,",",newTree.RtreeData[2].blocks[1].data,",",newTree.RtreeData[2].blocks[2].data)

print("=================================================================")
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block6', None)
insertBlock(newTree, testBlock)
temp = shapes[0].points[6]
print("=================================================================")
print("Root Node contains blocks:",newTree.RtreeRoot.blocks[0].data,",",newTree.RtreeRoot.blocks[1].data)
print("Node number 1 has rectangle:",newTree.RtreeData[0].blocks[0].rect.x_min,",",newTree.RtreeData[0].blocks[0].rect.x_max,",",newTree.RtreeData[0].blocks[0].rect.y_min,",",newTree.RtreeData[0].blocks[0].rect.y_max)
print("Node number 1 contains blocks:",newTree.RtreeData[1].blocks[0].data,",",newTree.RtreeData[1].blocks[1].data)
print("Node number 2 contains blocks:",newTree.RtreeData[2].blocks[0].data)
print("Node number 3 contains blocks:",newTree.RtreeData[3].blocks[0].data,",",newTree.RtreeData[3].blocks[1].data,",",newTree.RtreeData[3].blocks[2].data)
print("=================================================================")
print(temp)
rect = Rectangle(temp[0],temp[0],temp[1],temp[1])
testBlock = RtreeBlock(rect, 'block7', None)
insertBlock(newTree, testBlock)
print("=================================================================")
print("Root Node contains blocks:",newTree.RtreeRoot.blocks[0].data,",",newTree.RtreeRoot.blocks[1].data)
print("Node number 1 has rectangle:",newTree.RtreeData[0].blocks[0].rect.x_min,",",newTree.RtreeData[0].blocks[0].rect.x_max,",",newTree.RtreeData[0].blocks[0].rect.y_min,",",newTree.RtreeData[0].blocks[0].rect.y_max)
print("Node number 1 contains blocks:",newTree.RtreeData[1].blocks[0].data)
print("Node number 2 contains blocks:",newTree.RtreeData[2].blocks[0].data,",",newTree.RtreeData[2].blocks[1].data)
print("Node number 3 contains blocks:",newTree.RtreeData[3].blocks[0].data)
print("Node number 3 contains blocks:",newTree.RtreeData[4].blocks[0].data,",",newTree.RtreeData[4].blocks[1].data)
print("Node number 3 contains blocks:",newTree.RtreeData[5].blocks[0].data,",",newTree.RtreeData[5].blocks[1].data)
print("=================================================================")


