import shapefile
from rtree import *

node = RtreeNode(None, 0, 0)

rtree = Rtree(node)
sf = shapefile.Reader("ne_110m_coastline.shp")
shapes = sf.shapes()
print("==============================================================")



for x in shapes[2].points:
    print("==============================================")
    print("Going to insert points:",x)
    rect = Rectangle(x[0],x[0],x[1],x[1])
    block = RtreeBlock(rect, 'insertedBlock', None)
    insertBlock(rtree, block)
    print("Points Inserted")
print("==============================================================")
print("Root Node contains blocks:",rtree.RtreeRoot.blocks[0].data,",",rtree.RtreeRoot.blocks[1].data)
print("Node number 1 has rectangle:",rtree.RtreeData[0].blocks[0].rect.x_min,",",rtree.RtreeData[0].blocks[0].rect.x_max,",",rtree.RtreeData[0].blocks[0].rect.y_min,",",rtree.RtreeData[0].blocks[0].rect.y_max)
print("Node number 1 has rectangle:",rtree.RtreeData[0].blocks[1].rect.x_min,",",rtree.RtreeData[0].blocks[1].rect.x_max,",",rtree.RtreeData[0].blocks[1].rect.y_min,",",rtree.RtreeData[0].blocks[1].rect.y_max)
print("Node number 1 contains blocks:",rtree.RtreeData[1].blocks[0].data)
print("Node number 2 contains blocks:",rtree.RtreeData[2].blocks[0].data,",",rtree.RtreeData[2].blocks[1].data)

for x in shapes[3].points:
    print(x)
# for x in shapes[1].points:
#     print(x)
# print("==============================================================")
# for x in shapes[2].points:
#     print(x)
# print("==============================================================")



