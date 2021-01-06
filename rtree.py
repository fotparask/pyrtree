from rectangle import Rectangle

MAX_ENTRIES = 2


class RtreeBlock():

    def __init__(self, rect: Rectangle, data, contained_node):
        self.rect = rect
        self.data = data
        self.contained_node = None
        self.child = None

    def setContainedNode(self, Node):
        self.contained_node = None

    def containedNode(self):
        return self.contained_node

    def is_leaf(self):
        if self.child == None:
            return True
        else:
            return False



class RtreeNode():

    def __init__(self, blocks: list, parent: RtreeBlock, level: int):
        self.blocks = None
        self.parent = parent
        self.level = level

    def is_root(self):
        if self.parent == None:
            return True
        else:
            return False

    def set_new_level(self, new_level):
        self.level = new_level



class Rtree():

    RtreeData: list = None

    def __init__(self,RtreeRoot: RtreeNode):
        self.RtreeRoot = RtreeRoot

    def addNode(self,RtreeNode: RtreeNode):
        Rtree.RtreeData.append(RtreeNode)
    
    def deleteNode(self,RtreeNode: RtreeNode):
        Rtree.RtreeData.pop(RtreeNode)

    def changeRoot(self, RtreeNode: RtreeNode):
        pass


    @classmethod
    def treeLength(cls):
        pass


def chooseLeaf(rtree: Rtree, block: RtreeBlock):

    selectedNode: RtreeBlock = None

    #First case that the root is still empty
    if len(rtree.RtreeRoot.blocks) == 0:
        selectedNode = rtree.RtreeRoot
        return selectedNode

    minSpaceNeeded = 488663658200000
    nodeSelected = rtree.RtreeRoot
    #while loop checks where we can place the new object in order to create the smallest rectangle.
    while nodeSelected.blocks.is_leaf == False:
        for blockNumber in nodeSelected.blocks:
            x = blockNumber.rect.spaceNeeded(block.rect) 
            if x < minSpaceNeeded:
                minSpaceNeeded = x
                nodeSelected = blockNumber.child

    return selectedNode


#If the if statement below fails to enter, it means that the node we 
# are going to insert the new block is full, so it needs
# nodesplitting. For nodesplite I use the the QuadraticSplit method.

def quadraticSplit():
    pass

# function that checks where we can create the smallest rectangle and returns the tree_node to do so.
def pickSeeds(node: RtreeNode, block: RtreeBlock): 

    for blockNumber in node.blocks:
            x = blockNumber.rect.spaceNeeded(block.rect) 
            if x < minSpaceNeeded:
                minSpaceNeeded = x
                node = blockNumber.child
    
    return node

def pickNext():
    pass


#TreeNode contains the blocks of the r-tree. Each block has a child of type TreeNode. Also each Node has a parent
#of type TreeDataBlock.


# def insertBlocktoNode(dataBlock: TreeDataBlock, rootNode: TreeNode):
#     if len(rootNode.blocks) < MAX_ENTRIES:
#         rootNode.insertBlocktoNode(dataBlock)
#         return
    
#     minSpaceNeeded = 488663658200000
#     nodeSelected = rootNode
#     #while loop checks where we can place the new object in order to create the smallest rectangle.
#     while ~nodeSelected.blocks.is_leaf:
#         for blockNumber in nodeSelected.blocks:
#             x = blockNumber.rect.spaceNeeded(dataBlock.rect) 
#             if x < minSpaceNeeded:
#                 minSpaceNeeded = x
#                 nodeSelected = blockNumber.child

#     #If the if statement below fails to enter, it means that the node we 
#     # are going to insert the new block is full, so it needs
#     # nodesplitting. For nodesplite I use the the QuadraticSplit method.
#     if len(nodeSelected.blocks) < MAX_ENTRIES:
#         nodeSelected.blocks.append(dataBlock)
#         return 
    
#     #node splitting algorithms begins   
#     nodeSelected.parent = None
#     counter = 0
#     block_in_node_selected = 0
#     block_to_pair_with = MAX_ENTRIES - 1
#     largestRectangle = 0
#     pairs_selected = [0,0]

#     while block_in_node_selected < (MAX_ENTRIES - 1):
#         while counter < block_to_pair_with:
#             x = nodeSelected.blocks[block_in_node_selected].rect.pairedPerimeter(nodeSelected.blocks[block_to_pair_with].rect)
#             if x > largestRectangle:
#                 largestRectangle = x
#                 pairs_selected[0] = block_in_node_selected
#                 pairs_selected[1] = block_to_pair_with
#             counter += 1
#         block_in_node_selected += 1 
    
#     if nodeSelected.blocks[pairs_selected[0]].rect.isRectSmallerThan(nodeSelected.blocks[pairs_selected[1]].rect):
#         pass
#     else:
#         pairs_selected[0], pairs_selected[1] = pairs_selected[1], pairs_selected[0]

#     nodeSelected.parent.contained_node.blocks.pop(MAX_ENTRIES)

#     z_var += 1
#     nodeSelected.parent.contained_node.blocks.append(TreeDataBlock(dataBlock.rect, TreeNode(None, nodeSelected.blocks[pairs_selected[0]]), z_var, nodeSelected.parent.contained_node))
#     z_var += 1
#     nodeSelected.parent.contained_node.blocks.append(TreeDataBlock(dataBlock.rect, TreeNode(None, nodeSelected.blocks[pairs_selected[1]]), z_var, nodeSelected.parent.contained_node))

#     if len(nodeSelected.parent.contained_node.blocks) > MAX_ENTRIES:
#         insertBlocktoNode(nodeSelected.blocks[pairs_selected[1]], nodeSelected.parent.contained_node) 
#     else:
#         return






#always use the root node for this algorithm to work. From the root 
#the algorithm start to calculate where to place the Data Block(the rectangle)



