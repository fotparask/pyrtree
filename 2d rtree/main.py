import shapefile
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
from rtree import insertBlock, RtreeBlock, RtreeNode, deleteBlock, Rtree, MAX_VALUE, MIN_VALUE
from rectangle import Rectang


print("=============================================================")
print("                   2D R-Tree Data Structure")
print("=============================================================\n\n\n")

choice = 50
counter = 0

#Importing Shape file
sf = shapefile.Reader("ne_110m_coastline.shp")
shapes = sf.shapes()


data = []
for shape in shapes:
    for point in shape.points:
        data.append(point)

print("1.Press (1) to generate R-tree.")
print("2.Press any other number to exit.\n\n")

choice = input("Enter:")
choice = int(choice)

if choice == 1:

    node = RtreeNode(None, 0, 0)
    rtree = Rtree(node)

    for x in data:
        print("==============================================")
        print("Going to insert points:",x)
        rect = Rectang(x[0],x[0],x[1],x[1])
        block = RtreeBlock(rect, 'insertedBlock', None)
        insertBlock(rtree, block)
        print("Points Inserted")

else:
    exit()

print("\n\n==============================================")
print("              All points inserted")
print("==============================================")

while choice != 4:

    print("\n\n1.Press (1) to see R-Tree in matplotlib.(Visualize)")
    print("2.Press (2) to see all listed points in the R-Tree.")
    print("3.Press (3) to delete an entry in the R-Tree.")
    print("4.Press (4) to exit.\n\n")
    choice = input("Enter:")
    choice = int(choice)

    if choice == 1:

        #define Matplotlib figure and axis
        fig, ax = plt.subplots()
        min_x, max_x, min_y, max_y = MAX_VALUE, MIN_VALUE, MAX_VALUE, MIN_VALUE
        edge_values = [min_x, max_x, min_y, max_y]


        for dataBlock in rtree.RtreeData[0].blocks:
            edge_values = dataBlock.rect.findEdgedValues(edge_values)


        ax.add_patch(Rectangle((edge_values[0], edge_values[2]), edge_values[1] - edge_values[0], edge_values[3] - edge_values[2], fill=False))


        for dataNode in rtree.RtreeData:
            for dataBlock in dataNode.blocks:
                ax.add_patch(Rectangle((dataBlock.rect.x_min, dataBlock.rect.y_min), dataBlock.rect.rect_x(), dataBlock.rect.rect_y(), fill=False))

        #creating x and y axis
        ax.plot([edge_values[0] - 5, edge_values[1] + 5],[edge_values[2] - 5, edge_values[2] - 5])
        ax.plot([edge_values[0] - 5, edge_values[0] - 5],[edge_values[2] - 5, edge_values[3] + 5])
        ax.plot([edge_values[0] - 5, edge_values[1] + 5],[edge_values[3] + 5, edge_values[3] + 5])
        ax.plot([edge_values[1] + 5, edge_values[1] + 5],[edge_values[2] - 5, edge_values[3] + 5])

        #displaying plot
        plt.show()

    elif choice == 2:

        for counter in range(1, len(data),2):
            try:
                print("Point", counter,":",data[counter],"\tPoint", counter + 1,":",data[counter + 1])
            except IndexError:
                break


    elif choice == 3:
        
        print("\n\nEnter the value of the point you want to delete.\nPlease enter float value.(ex: x = 113.71293541875868, y =3.8935094262811556.")
        x_to_delete = input("\n\nEnter value of x:")
        y_to_delete = input("Enter value of y:")
        x_to_delete = float(x_to_delete)
        y_to_delete = float(y_to_delete)

        rectToDel = Rectang(x_to_delete,x_to_delete,y_to_delete,y_to_delete)

        deleteBlock(rtree, rectToDel)

        print("\nPoint successfully deleted.\n")


    elif choice == 4:
        exit()

    else:
        pass
