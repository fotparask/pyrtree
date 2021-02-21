import shapefile
import random
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
from rtree import insertBlock, RtreeBlock, RtreeNode, Rtree, MAX_VALUE, MIN_VALUE
from cuboid import Cuboid


node = RtreeNode(None, 0, 0)
rtree = Rtree(node)

counter = 0

#Importing Shape file
sf = shapefile.Reader("ne_110m_coastline.shp")
shapes = sf.shapes()

while counter < 10000:

    x_min1 = random.randint(1, 1000)
    x_max1 = random.randint(1, 1000)
    y_min1 = random.randint(1, 1000)
    y_max1 = random.randint(1, 1000)
    z_min1 = random.randint(1, 1000)
    z_max1 = random.randint(1, 1000)

    print(x_min1, x_max1 , y_min1 , y_max1, z_min1, z_max1)

    print("==============================================")
    rect = Cuboid(x_min1, x_max1, y_min1, y_max1, z_min1, z_max1)
    testBlock = RtreeBlock(rect, 'block1', None)
    insertBlock(rtree, testBlock)
    print("Points Inserted")

    counter += 1






print("=================================================================")
print("Root Node contains blocks:",rtree.RtreeRoot.blocks[0].data,",",rtree.RtreeRoot.blocks[1].data)
# print("Node number 1 has rectangle:",rtree.RtreeData[0].blocks[0].rect.x_min,",",rtree.RtreeData[0].blocks[0].rect.x_max,",",rtree.RtreeData[0].blocks[0].rect.y_min,",",rtree.RtreeData[0].blocks[0].rect.y_max)
# print("Node number 1 contains blocks:",rtree.RtreeData[1].blocks[0].data)
# print("Node number 2 contains blocks:",rtree.RtreeData[2].blocks[0].data,",",rtree.RtreeData[2].blocks[1].data)
# print("Node number 3 contains blocks:",rtree.RtreeData[3].blocks[0].data)
# print("Node number 3 contains blocks:",rtree.RtreeData[4].blocks[0].data,",",rtree.RtreeData[4].blocks[1].data)
# print("Node number 3 contains blocks:",rtree.RtreeData[5].blocks[0].data,",",rtree.RtreeData[5].blocks[1].data)
print("=================================================================")


