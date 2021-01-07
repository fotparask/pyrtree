from rectangle import Rectangle

MAX_ENTRIES = 2
MAX_VALUE = 488663658200000


class RtreeBlock():

    def __init__(self, rect: Rectangle, data, contained_node):
        self.rect = rect
        self.data = data
        self.contained_node = None
        self.child = None

    def setContainedNode(self, node):
        self.contained_node = node

    def containedNode(self):
        return self.contained_node

    def is_leaf(self):
        if self.child == None:
            return True
        else:
            return False



class RtreeNode():

    def __init__(self, blocks: list, parent: RtreeBlock, level: int):
        self.blocks = []
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

    RtreeData: list = []

    def __init__(self,RtreeRoot: RtreeNode):
        self.RtreeRoot = RtreeRoot
        Rtree.RtreeData.append(RtreeRoot)

    def addNode(self,RtreeNode: RtreeNode):
        Rtree.RtreeData.append(RtreeNode)
    
    def deleteNode(self,node: RtreeNode):
        Rtree.RtreeData.pop(Rtree.RtreeData.index(node))


    @classmethod
    def changeRoot(self, newRootNode: RtreeNode):
        oldRootNode = self.RtreeData[0]
        Rtree.RtreeData.append(oldRootNode)
        Rtree.RtreeData.insert(0, newRootNode)

    @classmethod
    def treeLength(cls):
        pass





def insertBlock(rtree: Rtree, block: RtreeBlock):

    #starting with the root node, we search a node to place the new block.
    rootNode = rtree.RtreeRoot
    selectedNode: RtreeNode = None

    selectedNode = chooseLeaf(rtree, block)

    while len(selectedNode.blocks) > MAX_ENTRIES:

        if selectedNode == rootNode:
            break

        quadraticSplit(rtree,selectedNode)
        selectedNode = selectedNode.parent.contained_node


    if selectedNode == rootNode and len(selectedNode.blocks) > MAX_ENTRIES:
        newRootCreation(rtree, selectedNode, block)

    return

    

def newRootCreation(rtree: Rtree, rootNode: RtreeNode, block: RtreeBlock):

    #the blocks that are inside the node we want to split
    tmpInitialBlocks = rootNode.blocks
    newNode: RtreeNode = None
    counter = 0

    #emptying the existing root to reform it
    for counter in range(MAX_ENTRIES - 1):
        rootNode.blocks[counter] = None

    firstBlockInNode1: RtreeBlock = None
    firstBlockInNode2: RtreeBlock = None

    firstBlockInNode1 , firstBlockInNode2 = pickSeed(tmpInitialBlocks)


    #removing the blocks from the tmpInitialBlocks list and adding them to the new nodes
    tmpInitialBlocks.pop(tmpInitialBlocks.index(firstBlockInNode1))
    tmpInitialBlocks.pop(tmpInitialBlocks.index(firstBlockInNode2))
    rootNode.blocks.append(firstBlockInNode1)
    newNode.blocks.append(firstBlockInNode2)


    #pickNext Stage.
    x = MAX_ENTRIES - 3
    if x < 0: x = 0
    for counter in range(x):
        nodeTobePlaced: RtreeNode = None
        nodeTobePlaced = pickNext(rootNode, newNode, tmpInitialBlocks[counter])
        if nodeTobePlaced ==  rootNode:
            rootNode.blocks.append(tmpInitialBlocks[counter])
        else:
            newNode.blocks.append(tmpInitialBlocks[counter])



    #creating new root node
    newRootNode: RtreeNode(None, None, 0)
    newRect: Rectangle(0,0,0,0)
    newBlock: RtreeBlock(newRect,"blockName", newRootNode)
    newBlock2: RtreeBlock(newRect,"blockName", newRootNode)
    newRootNode.blocks.append(newBlock)
    newRootNode.blocks.append(newBlock2)

    rootNode.parent = newRootNode.blocks[0]
    newNode.parent = newRootNode.blocks[1]
    fixParent(rootNode)
    fixParent(newNode)

    rtree.changeRoot(newRootNode)

    return




def chooseLeaf(rtree: Rtree, block: RtreeBlock):

    selectedNode: RtreeBlock = None

    #First case that the root is still empty
    if len(rtree.RtreeRoot.blocks) == 0:
        selectedNode = rtree.RtreeRoot
        return selectedNode

    minSpaceNeeded = MAX_VALUE
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

def quadraticSplit(rtree: Rtree, node: RtreeNode):
    
    #the blocks that are inside the node we want to split
    tmpInitialBlocks = node.blocks
    newNode: RtreeNode = None

    #emptying the existing node to reform it
    for counter in range(MAX_ENTRIES - 1):
        node.blocks[counter] = None

    firstBlockInNode1: RtreeBlock = None
    firstBlockInNode2: RtreeBlock = None

    firstBlockInNode1 , firstBlockInNode2 = pickSeed(tmpInitialBlocks)

    tmpInitialBlocks.pop(tmpInitialBlocks.index(firstBlockInNode1))
    tmpInitialBlocks.pop(tmpInitialBlocks.index(firstBlockInNode2))

    x = MAX_ENTRIES - 3
    if x < 0: x = 0
    for counter in range(x):
        nodeTobePlaced: RtreeNode = None
        nodeTobePlaced = pickNext(node, newNode, tmpInitialBlocks[counter])
        if nodeTobePlaced ==  node:
            node.blocks.append(tmpInitialBlocks[counter])
        else:
            newNode.blocks.append(tmpInitialBlocks[counter])


    fixParent(node)

    newRect: Rectangle(0,0,0,0)
    newBlock: RtreeBlock(newRect,"blockName", node.parent.contained_node)
    newBlock.rect = findParentCoveringRect(newNode)

    node.parent.contained_node.blocks.append(newBlock) 

    rtree.addNode(newNode)

    return



def fixParent(node: RtreeNode):

    node.parent.rect = findParentCoveringRect(node)
    return




def findParentCoveringRect(node: RtreeNode):
    
    block: RtreeBlock = None
    counter = 0
    min_x = MAX_VALUE
    max_x = 0
    min_y = MAX_VALUE
    max_y = 0
    edgedValues = [min_x, max_x, min_y, max_y]


    while node.blocks[counter] != None and counter < MAX_ENTRIES:
        
        min_x, max_x, min_y, max_y = node.blocks[counter].rect.findEdgedValues(edgedValues)
        edgedValues = [min_x, max_x, min_y, max_y]
        counter += 1

    block.rect.__init__(min_x, max_x, min_y, max_y)

    return block.rect





# function that checks where we can create the smallest rectangle and returns the tree_node to do so.
def pickSeed(node: RtreeNode): 
  
    block_to_pair_with = 1
    block_in_node_selected = 0
    largestRectangle = 0
    pairs_selected = [0,0]
    blocks_selected = [None,None]

    while block_in_node_selected < (MAX_ENTRIES - 1):
        while block_to_pair_with < MAX_ENTRIES:
            x = node.blocks[block_in_node_selected].rect.pairedPerimeter(node.blocks[block_to_pair_with].rect)
            if x > largestRectangle:
                largestRectangle = x
                pairs_selected[0] = block_in_node_selected
                pairs_selected[1] = block_to_pair_with
            block_to_pair_with += 1
        block_in_node_selected += 1 
        block_to_pair_with = block_in_node_selected + 1
    
    blocks_selected = [ node.blocks[pairs_selected[0]], node.blocks[pairs_selected[1]] ]
    
    return blocks_selected



def pickNext(nodeGroup1: RtreeNode, nodeGroup2: RtreeNode, pickedBlock: RtreeBlock):

    unionWithBlock1 = 0
    unionWithBlock2 = 0

    Block1 = nodeGroup1.blocks[0]
    Block2 = nodeGroup2.blocks[0]

    unionWithBlock1 = Block1.rect.pairedPerimeter(pickedBlock.rect)
    unionWithBlock2 = Block2.rect.pairedPerimeter(pickedBlock.rect)

    if unionWithBlock1 < unionWithBlock2 :
        return nodeGroup1
    else:
        return nodeGroup2




