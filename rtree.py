from rectangle import Rectangle


MAX_ENTRIES = 2
global z_var
    
from rectangle import Rectangle

class Rtree():

    RtreeData: list = None

    def __init__(self,RtreeRoot):
        self.RtreeRoot = RtreeRoot

    def addNode(self,RtreeNode):
        Rtree.RtreeData.append(RtreeNode)
    
    def deleteNode(self,RtreeNode):
        Rtree.RtreeData.pop(RtreeNode)

    @classmethod
    def treeLength(cls):
        pass


class RtreeBlock():

    def __init__(self, rect: Rectangle, data, contained_node):
        self.rect = rect
        self.data = data
        self.contained_node = None

    def setContainedNode(self, Node):
        self.contained_node = None

    def containedNode(self):
        return self.contained_node



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



# class TreeDataBlock():

#     def __init__ (self, rect: Rectangle, child: TreeNode, data: int, contained_node: TreeNode):
#         self.rect = rect
#         self.child = child
#         self.data = data
#         self.contained_node = contained_node

#     def is_pointer (self):
#         if self.child:
#             return True
#         return False

#     #if Block does not have a child, it means its a leaf node, so if self.child != NULL then it is not a leaf Block.
#     def is_leaf (self):
#         if self.child:
#             return False
#         return True

# class TreeNode():

#     def __init__ (self, parent: TreeDataBlock, blocks: TreeDataBlock):
#         self.blocks = blocks
#         self.parent = parent

#     #if Node is not a parent, it means it is the root, so if self.parent != NULL then it is not the root Node.
#     @property
#     def is_root(self):
#         if self.parent:
#             return False
#         return True

    


#TreeNode contains the blocks of the r-tree. Each block has a child of type TreeNode. Also each Node has a parent
#of type TreeDataBlock.


def insertBlocktoNode(dataBlock: TreeDataBlock, rootNode: TreeNode):
    if len(rootNode.blocks) < MAX_ENTRIES:
        rootNode.insertBlocktoNode(dataBlock)
        return
    
    minSpaceNeeded = 488663658200000
    nodeSelected = rootNode
    #while loop checks where we can place the new object in order to create the smallest rectangle.
    while ~nodeSelected.blocks.is_leaf:
        for blockNumber in nodeSelected.blocks:
            x = blockNumber.rect.spaceNeeded(dataBlock.rect) 
            if x < minSpaceNeeded:
                minSpaceNeeded = x
                nodeSelected = blockNumber.child

    #If the if statement below fails to enter, it means that the node we 
    # are going to insert the new block is full, so it needs
    # nodesplitting. For nodesplite I use the the QuadraticSplit method.
    if len(nodeSelected.blocks) < MAX_ENTRIES:
        nodeSelected.blocks.append(dataBlock)
        return 
    
    #node splitting algorithms begins   
    nodeSelected.parent = None
    counter = 0
    block_in_node_selected = 0
    block_to_pair_with = MAX_ENTRIES - 1
    largestRectangle = 0
    pairs_selected = [0,0]

    while block_in_node_selected < (MAX_ENTRIES - 1):
        while counter < block_to_pair_with:
            x = nodeSelected.blocks[block_in_node_selected].rect.pairedPerimeter(nodeSelected.blocks[block_to_pair_with].rect)
            if x > largestRectangle:
                largestRectangle = x
                pairs_selected[0] = block_in_node_selected
                pairs_selected[1] = block_to_pair_with
            counter += 1
        block_in_node_selected += 1 
    
    if nodeSelected.blocks[pairs_selected[0]].rect.isRectSmallerThan(nodeSelected.blocks[pairs_selected[1]].rect):
        pass
    else:
        pairs_selected[0], pairs_selected[1] = pairs_selected[1], pairs_selected[0]

    nodeSelected.parent.contained_node.blocks.pop(MAX_ENTRIES)

    z_var += 1
    nodeSelected.parent.contained_node.blocks.append(TreeDataBlock(dataBlock.rect, TreeNode(None, nodeSelected.blocks[pairs_selected[0]]), z_var, nodeSelected.parent.contained_node))
    z_var += 1
    nodeSelected.parent.contained_node.blocks.append(TreeDataBlock(dataBlock.rect, TreeNode(None, nodeSelected.blocks[pairs_selected[1]]), z_var, nodeSelected.parent.contained_node))

    if len(nodeSelected.parent.contained_node.blocks) > MAX_ENTRIES:
        insertBlocktoNode(nodeSelected.blocks[pairs_selected[1]], nodeSelected.parent.contained_node) 
    else:
        return






# function that checks where we can create the smallest rectangle and returns the tree_node to do so.
def minRectExpansion(nodeVar: TreeNode, blockVar: TreeDataBlock):

    for blockNumber in nodeVar.blocks:
            x = blockNumber.rect.spaceNeeded(blockVar.rect) 
            if x < minSpaceNeeded:
                minSpaceNeeded = x
                nodeVar = blockNumber.child
    
    return nodeVar





#always use the root node for this algorithm to work. From the root 
#the algorithm start to calculate where to place the Data Block(the rectangle)



