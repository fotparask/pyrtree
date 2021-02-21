from rectangle import Rectang
import copy
import sys

MAX_ENTRIES = 3
MAX_VALUE = 48866365820000000
MIN_VALUE = -48866365820000000






class RtreeBlock():

    def __init__(self, rect: Rectang, data: str, contained_node):
        self.rect = rect
        self.data = data
        self.contained_node = contained_node
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

    def __init__(self, parent: RtreeBlock, level: int, indexPosition: int):
        self.blocks = []
        self.parent = parent
        self.level = level
        self.indexPosition = 0

    def is_root(self):
        if self.parent == None:
            return True
        else:
            return False

    def set_new_level(self, new_level):
        self.level = new_level

    def setIndexPosition(self, position: int):
        self.indexPosition = position



class Rtree():

    RtreeData: list = []

    def __init__(self,RtreeRoot: RtreeNode):
        self.RtreeRoot = RtreeRoot
        self.RtreeRoot.setIndexPosition(0)
        Rtree.RtreeData.append(RtreeRoot)

    def addNode(self,RtreeNode: RtreeNode):
        listLenght = len(self.RtreeData)
        RtreeNode.setIndexPosition(listLenght - 1)
        Rtree.RtreeData.append(RtreeNode)
    
    def deleteNode(self,nodeLocation: int):
        self.RtreeData.pop(nodeLocation)

    def changeRoot(self, newRootNode: RtreeNode):
        self.RtreeData.insert(0, newRootNode)
        self.RtreeRoot = newRootNode

    def treeLength(self):
        return len(self.RtreeData)










def deleteBlock(rtree: Rtree, rect: Rectang):

    #finding in which node the block is located
    nodeLocation = 0
    blockLocation = 0
    indexPositions = [nodeLocation,blockLocation]

    indexPositions = searchBlock(rtree, rect)
    nodeLocation = indexPositions[0]
    blockLocation = indexPositions[1]
    
    if nodeLocation is None:
        sys.exit('Could not delete block object.\nCould not find block with coordinates: (', rect.x_min,",",rect.y_min,")")

    rtree.deleteNode(nodeLocation) 

    print("Block has been deleted")
    if rtree.RtreeData == []:
        return

    if rtree.RtreeData[nodeLocation].blocks == []:
        rtree.deleteNode(nodeLocation)
    


def searchBlock(rtree: Rtree, rect: Rectang):


    nodeSelected = rtree.RtreeRoot
    selectedBlock: RtreeBlock = None
    selectedNode: RtreeNode = None
    spaceDifference = MAX_VALUE
    indexPositions = [None, None]
    
    
    while nodeSelected.blocks[0].is_leaf() == False:
        counter = 0
        smallestBlock = 0
        for blockVar in nodeSelected.blocks:
            counter += 1
            x = blockVar.rect.spaceNeeded(rect)
            if x < spaceDifference:
                spaceDifference = x
                smallestBlock = counter
        else:
            selectedNode = nodeSelected.blocks[smallestBlock].child

    for blockVar in selectedNode.blocks:
        if blockVar.rect == rect:
            indexPositions[0] = 0
            indexPositions[1] = counter
        counter += 1
    else:
        indexPositions = [None, None]
        return indexPositions
    



def insertBlock(rtree: Rtree, block: RtreeBlock):

    #starting with the root node, we search a node to place the new block.
    rootNode = rtree.RtreeRoot
    selectedNode: RtreeNode = None

    selectedNode = chooseLeaf(rtree, block)

    if len(selectedNode.blocks) < MAX_ENTRIES:
        block.contained_node = selectedNode
        selectedNode.blocks.append(block)
        return
    else:
        selectedNode.blocks.append(block) 
        while len(selectedNode.blocks) > MAX_ENTRIES:
            if selectedNode == rtree.RtreeRoot:
                break  
            quadraticSplit(rtree,selectedNode)
            selectedNode = selectedNode.parent.contained_node
         

    if selectedNode == rootNode and len(selectedNode.blocks) > MAX_ENTRIES:
        print("==============================================")
        print("New root is going to be created")
        print("==============================================")
        newRootCreation(rtree, block)
    return

    

def newRootCreation(rtree: Rtree, block: RtreeBlock):

    #the blocks that are inside the node we want to split
    nodeTobePlaced: RtreeNode = None
    newNode = RtreeNode(None,0,0)
    nodeTobePlaced = RtreeNode(None,0,0)
    tempBlock1 , tempBlock2 = pickSeed(rtree.RtreeRoot)
    blockCounter = 1

    newNode.blocks.append(tempBlock2)

    rtree.RtreeRoot.blocks[0] , rtree.RtreeRoot.blocks[rtree.RtreeRoot.blocks.index(tempBlock1)] = rtree.RtreeRoot.blocks[rtree.RtreeRoot.blocks.index(tempBlock1)] , rtree.RtreeRoot.blocks[0]
    rtree.RtreeRoot.blocks[-1] , rtree.RtreeRoot.blocks[rtree.RtreeRoot.blocks.index(tempBlock2)] = rtree.RtreeRoot.blocks[rtree.RtreeRoot.blocks.index(tempBlock2)] , rtree.RtreeRoot.blocks[-1]
    rtree.RtreeRoot.blocks[-1] = None
    rtree.RtreeRoot.blocks.pop()

    while blockCounter < len(rtree.RtreeRoot.blocks):
        nodeTobePlaced = pickNext(rtree.RtreeRoot, newNode, rtree.RtreeRoot.blocks[blockCounter])
        if nodeTobePlaced == rtree.RtreeRoot:
            rtree.RtreeRoot.blocks[blockCounter].contained_node = rtree.RtreeRoot
            blockCounter += 1
        else:
            newNode.blocks.append(rtree.RtreeRoot.blocks[blockCounter])
            newNode.blocks[-1].contained_node = newNode
            rtree.RtreeRoot.blocks[-1] , rtree.RtreeRoot.blocks[blockCounter] = rtree.RtreeRoot.blocks[blockCounter] , rtree.RtreeRoot.blocks[-1]
            rtree.RtreeRoot.blocks[-1] = None
            rtree.RtreeRoot.blocks.pop()
            blockCounter = 1



    #creating new root node
    newRootNode = RtreeNode(None, 0, 0)
    newRect = Rectang(0,0,0,0)
    newBlock1 = RtreeBlock(newRect,"BlockRootContainer", newRootNode)
    newBlock2 = RtreeBlock(newRect,"BlockRootContainer", newRootNode) 

    newBlock1.child = rtree.RtreeRoot
    newBlock2.child = newNode
    newRootNode.blocks.append(newBlock1)
    newRootNode.blocks.append(newBlock2)

    rtree.RtreeRoot.parent = newRootNode.blocks[0]
    newNode.parent = newRootNode.blocks[1]
    rtree.addNode(newNode)
    
    fixParent(rtree.RtreeRoot)
    fixParent(newNode)

    rtree.changeRoot(newRootNode)

    return



def chooseLeaf(rtree: Rtree, block: RtreeBlock):

    selectedNode: RtreeNode = None
    selectedNode = rtree.RtreeRoot
    counter = 0
    indexSelected = 0
    #First case that the root is still empty
    if len(rtree.RtreeRoot.blocks) == 0:
        selectedNode = rtree.RtreeRoot
        return selectedNode
    
    #while loop checks where we can place the new object in order to create the smallest rectang.
    
    while selectedNode.blocks[0].is_leaf() == False:
        counter = 0
        minSpaceNeeded = MAX_VALUE
        for blockNumber in selectedNode.blocks:
            x = blockNumber.rect.spaceNeeded(block.rect) 
            if x < minSpaceNeeded:
                minSpaceNeeded = x
                indexSelected = counter
            counter += 1
        else:
            selectedNode = selectedNode.blocks[indexSelected].child

    return selectedNode



#If the if statement below fails to enter, it means that the node we 
# are going to insert the new block is full, so it needs
# nodesplitting. For nodesplite I use the the QuadraticSplit method.
def quadraticSplit(rtree: Rtree, node: RtreeNode):
    
    #the blocks that are inside the node we want to split
    newNode = RtreeNode(None,0,0)
    nodeTobePlaced = RtreeNode(None,0,0)
    tempBlock1 , tempBlock2 = pickSeed(node)
    blockCounter = 1

    newNode.blocks.append(tempBlock2)
    
    node.blocks[0] , node.blocks[node.blocks.index(tempBlock1)] = node.blocks[node.blocks.index(tempBlock1)] , node.blocks[0]
    node.blocks[-1] , node.blocks[node.blocks.index(tempBlock2)] = node.blocks[node.blocks.index(tempBlock2)] , node.blocks[-1]
    node.blocks[-1] = None
    node.blocks.pop()
    while blockCounter < len(node.blocks):
        nodeTobePlaced = pickNext(node, newNode, node.blocks[blockCounter])
        if nodeTobePlaced == node:
            node.blocks[blockCounter].contained_node = node
            blockCounter += 1
        else:
            newNode.blocks.append(node.blocks[blockCounter])
            newNode.blocks[-1].contained_node = newNode
            node.blocks[-1] , node.blocks[blockCounter] = node.blocks[blockCounter] , node.blocks[-1]
            node.blocks[-1] = None
            node.blocks.pop()
            blockCounter = 1

    fixParent(node)

    newRect = Rectang(0,0,0,0)
    newBlock = RtreeBlock(newRect,"BlockNodeContainer", node.parent.contained_node)
    newBlock.child = newNode
    newNode.parent = newBlock
    newBlock.rect = findParentCoveringRect(newNode)
    node.parent.contained_node.blocks.append(newBlock)

    rtree.addNode(newNode)

    return



def fixParent(node: RtreeNode):

    node.parent.rect = findParentCoveringRect(node)
    return



def findParentCoveringRect(node: RtreeNode):
    
    counter = 0
    min_x = MAX_VALUE
    max_x = MIN_VALUE
    min_y = MAX_VALUE
    max_y = MIN_VALUE
    edgedValues = [min_x, max_x, min_y, max_y]
    try:
        while counter < MAX_ENTRIES and node.blocks[counter]:
            min_x, max_x, min_y, max_y = node.blocks[counter].rect.findEdgedValues(edgedValues)
            edgedValues = [min_x, max_x, min_y, max_y]
            counter += 1
    except IndexError:
        pass
    newRect = Rectang(min_x, max_x, min_y, max_y)

    return newRect



# function that checks where we can create the smallest rectang and returns the tree_node to do so.
def pickSeed(node: RtreeNode): 
  
    block_to_pair_with = 1
    block_in_node_selected = 0
    largestRectang = MIN_VALUE
    pairs_selected = [0,0]
    blocks_selected = [None,None]

    while block_in_node_selected < MAX_ENTRIES:
        while block_to_pair_with < MAX_ENTRIES + 1:
            x = node.blocks[block_in_node_selected].rect.pairedPerimeter(node.blocks[block_to_pair_with].rect)
            if x > largestRectang:
                largestRectang = x
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