from rectangle import Rectangle
import copy
import sys

MAX_ENTRIES = 3
MAX_VALUE = 488663658200000
MIN_VALUE = -488663658200000


class RtreeBlock():

    def __init__(self, rect: Rectangle, data: str, contained_node):
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



def deleteBlock(rtree: Rtree, block: RtreeBlock):

    #finding in which node the block is located
    nodeLocation = 0
    blockLocation = 0
    indexPositions = [nodeLocation,blockLocation]

    indexPositions = searchBlock(rtree, block, 2)
    nodeLocation = indexPositions[0]
    blockLocation = indexPositions[1]
    
    if nodeLocation is None:
        sys.exit('Could not delete block object. Program tried to delete root block.')


    rtree.deleteNode(nodeLocation) 

    print("Block has been deleted")
    if rtree.RtreeData == []:
        return

    if rtree.RtreeData[nodeLocation].blocks == []:
        rtree.deleteNode(nodeLocation)

    

        

    
    

#searchBlock algorithm. If searchType is 1, we are searching by data
# and the algorithm searches the blocks one by one to find it.
#if searchType is 2, we are searching by rectange size, and we choose 
#which node to search accordingly. 
#if searchType is 0 searchBlock exits with 0 error code. The same happens if the root node is empty. 
#searchBlock returns 2, if the value is not found.
# Most times we will be using the 2nd method, the first is not recommended.
def searchBlock(rtree: Rtree, block: RtreeBlock, searchType: int):

    indexPositions = [0, 0]
    counter = 0

    if searchType == 0 or len(rtree.RtreeRoot.blocks) == 0: 
        indexPositions = [None, None]
        return indexPositions

    data = block.data
    rect = block.rect


    if searchType == 1:
        for nodeSelected in rtree.RtreeData:
            for blockSelected in nodeSelected.blocks:
                if blockSelected.data == data:
                    indexPositions = [rtree.RtreeData.index, counter]
                    return indexPositions
                counter += counter
        indexPositions = [None, None]
        return indexPositions

    if searchType == 2:

        nodeSelected = rtree.RtreeRoot
        selectedBlock: RtreeBlock = None
        spaceDifference = MAX_VALUE
        
        while nodeSelected.blocks[0].is_leaf() == False:
            for blockVar in nodeSelected.blocks:
                x = blockVar.rect.spaceNeeded(rect)
                if x < spaceDifference:
                    spaceDifference = x
                    selectedBlock = blockVar

            #parent node selected and checks if it is NULL    
            nodeSelected = selectedBlock.child
            if nodeSelected.blocks == []:
                indexPositions = [None, None]
                return indexPositions 

        if nodeSelected.blocks[0].is_leaf() == True:
            for blockVar in nodeSelected.blocks:
                if blockVar.rect == rect:
                    indexPositions = [rtree.RtreeData.index(nodeSelected), counter]
                    return indexPositions
                counter += counter
            indexPositions = [None, None]
            return indexPositions
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
            block.contained_node = selectedNode    
            quadraticSplit(rtree,selectedNode)
            selectedNode = selectedNode.parent.contained_node
         

    if selectedNode == rootNode and len(selectedNode.blocks) > MAX_ENTRIES:
        print("==============================================")
        print("New root is going to be created")
        print("==============================================")
        newRootCreation(rtree, block)
        print("New root has positions:")
        print("Node number 1 has rectangle:",rtree.RtreeData[0].blocks[0].rect.x_min,",",rtree.RtreeData[0].blocks[0].rect.x_max,",",rtree.RtreeData[0].blocks[0].rect.y_min,",",rtree.RtreeData[0].blocks[0].rect.y_max)
        print("Node number 1 has rectangle:",rtree.RtreeData[0].blocks[1].rect.x_min,",",rtree.RtreeData[0].blocks[1].rect.x_max,",",rtree.RtreeData[0].blocks[1].rect.y_min,",",rtree.RtreeData[0].blocks[1].rect.y_max)
        print("==============================================")
    return

    

def newRootCreation(rtree: Rtree, block: RtreeBlock):

    #the blocks that are inside the node we want to split
    tmpInitialNode: RtreeBlock = None
    tmpInitialNode = copy.deepcopy(rtree.RtreeRoot)
    tmpInitialNode.blocks.append(block)
    nodeTobePlaced: RtreeNode = None
    newNode = RtreeNode(None,0,0)
    counter = 0

    #emptying the existing root to reform it
    rtree.RtreeRoot.blocks.clear()

    firstBlockInNode1: RtreeBlock = None
    firstBlockInNode2: RtreeBlock = None

    tempBlock1 , tempBlock2 = pickSeed(tmpInitialNode)
    firstBlockInNode1 = copy.deepcopy(tempBlock1)
    firstBlockInNode2 = copy.deepcopy(tempBlock2)

    #removing the blocks from the tmpInitialBlocks list and adding them to the new nodes
    tmpInitialNode.blocks.remove(tempBlock1)
    tmpInitialNode.blocks.remove(tempBlock2)

    firstBlockInNode1.contained_node = rtree.RtreeRoot
    firstBlockInNode2.contained_node = newNode
    rtree.RtreeRoot.blocks.append(firstBlockInNode1)
    newNode.blocks.append(firstBlockInNode2)

    #pickNext Stage.
    x = MAX_ENTRIES - 1
    if x > 1:
        for counter in range(x):
            nodeTobePlaced = pickNext(rtree.RtreeRoot, newNode, tmpInitialNode.blocks[counter])
            if nodeTobePlaced ==  rtree.RtreeRoot:
                tmpInitialNode.blocks[counter].contained_node = rtree.RtreeRoot
                rtree.RtreeRoot.blocks.append(tmpInitialNode.blocks[counter])
            else:
                tmpInitialNode.blocks[counter].contained_node = newNode
                newNode.blocks.append(tmpInitialNode.blocks[counter])



    #creating new root node
    newRootNode = RtreeNode(None, 0, 0)
    newRect = Rectangle(0,0,0,0,0,0)
    newBlock1 = RtreeBlock(newRect,"BlockRootContainer", newRootNode)
    newBlock2 = RtreeBlock(newRect,"BlockRootContainer", newRootNode) 

    newBlock2.child = newNode
    newBlock1.child = rtree.RtreeRoot
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
    #First case that the root is still empty
    if len(rtree.RtreeRoot.blocks) == 0:
        selectedNode = rtree.RtreeRoot
        return selectedNode
    
    minSpaceNeeded = MAX_VALUE
    selectedNode = rtree.RtreeRoot
    #while loop checks where we can place the new object in order to create the smallest rectangle.
    
    while selectedNode.blocks[0].is_leaf() == False:
        print("While starts")
        for blockNumber in selectedNode.blocks:
            x = blockNumber.rect.spaceNeeded(block.rect) 
            print("Comparing point:",block.rect.x_min,",",block.rect.y_min)
            print("With point:",blockNumber.rect.x_min,",",blockNumber.rect.x_max,",",blockNumber.rect.y_min,",",blockNumber.rect.y_max)
            print("Block is:",blockNumber.data," and minimun space needed is:",x)
            print("Is ",x," smaller than ",minSpaceNeeded,"?:",x < minSpaceNeeded)
            print("Is block ",selectedNode.blocks[0].data,"a leaf?",selectedNode.blocks[0].is_leaf())
            if x < minSpaceNeeded:
                minSpaceNeeded = x
        else:
            selectedNode = blockNumber.child

    return selectedNode






#If the if statement below fails to enter, it means that the node we 
# are going to insert the new block is full, so it needs
# nodesplitting. For nodesplite I use the the QuadraticSplit method.

def quadraticSplit(rtree: Rtree, node: RtreeNode):
    
    print("Entered Quadric split")
    #the blocks that are inside the node we want to split
    print("Leaving deep copy")
    newNode = RtreeNode(None,0,0)
    nodeTobePlaced = RtreeNode(None,0,0)
    tempBlock1 , tempBlock2 = pickSeed(node)
    blockCounter = 1

    newNode.blocks.append(tempBlock2)
    print("++++++++++++++++++++++")
    print("Node contains blocks:",node.blocks[0].data,",",node.blocks[1].data,",",node.blocks[2].data,",",node.blocks[3].data)
    print("++++++++++++++++++++++")
    
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

    newRect = Rectangle(0,0,0,0,0,0)
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

#print("tempnode memory value is:",blockNumber)
#print("block child has value:",blockNumber.child)

def findParentCoveringRect(node: RtreeNode):
    
    counter = 0
    min_x = MAX_VALUE
    max_x = MIN_VALUE
    min_y = MAX_VALUE
    max_y = MIN_VALUE
    min_z = MAX_VALUE
    max_z = MIN_VALUE
    edgedValues = [min_x, max_x, min_y, max_y, min_z, max_z]
    try:
        while counter < MAX_ENTRIES and node.blocks[counter]:
            min_x, max_x, min_y, max_y, min_z, max_z = node.blocks[counter].rect.findEdgedValues(edgedValues)
            edgedValues = [min_x, max_x, min_y, max_y, min_z, max_z]
            counter += 1
    except IndexError:
        pass
    newRect = Rectangle(min_x, max_x, min_y, max_y, min_z, max_z)

    return newRect





# function that checks where we can create the smallest cube and returns the tree_node to do so.
def pickSeed(node: RtreeNode): 
  
    block_to_pair_with = 1
    block_in_node_selected = 0
    largestCapacityDifference = 0
    pairs_selected = [0,0]
    blocks_selected = [None,None]

    while block_in_node_selected < (MAX_ENTRIES - 1):
        while block_to_pair_with < MAX_ENTRIES:
            x = node.blocks[block_in_node_selected].rect.pairedVolume(node.blocks[block_to_pair_with].rect)
            if x > largestCapacityDifference:
                largestCapacityDifference = x
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




