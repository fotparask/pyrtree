from rectangle inmport Rectangle


MAX_ENTRIES = 2

    


class TreeDataBlock():

    def __init__ (self, rect: Rectangle, child: TreeNode, data: str):
        self.rect = rect
        self.child = child
        self.data = data

    def is_pointer (self):
        if self.child:
            return True
        return False

    #if Block does not have a child, it means its a leaf node, so if self.child != NULL then it is not a leaf Block.
    def is_leaf (self):
        if self.child:
            return False
        return True


#TreeNode contains the blocks of the r-tree. Each block has a child of type TreeNode. Also each Node has a parent
#of type TreeDataBlock.

class TreeNode():

    def __init__ (self, parent: TreeDataBlock, blocks: TreeDataBlock[]):
        self.blocks = blocks[MAX_ENTRIES]
        self.parent = parent

    #if Node is not a parent, it means it is the root, so if self.parent != NULL then it is not the root Node.
    @property
    def is_root(self):
        if self.parent:
            return False
        return True
    
    def insertBlocktoNode(self, dataBlock: TreeDataBlock):
        self.blocks.append(dataBlock)

    def searchAvailableNode(self, dataBlock: TreeDataBlock):
        if self.blocks.lenght() < MAX_ENTRIES:
            self.insertBlocktoNode(dataBlock)
        
        minSpaceNeeded = 48866365820000
        blockSelected = None
        while ~self.dataBlock.blocks.is_leaf:
            for blockNumber in self.blocks:
                x = blockNumber.rect.spaceNeeded(dataBlock.rect) 
                if x < minSpaceNeeded:
                    minSpaceNeeded = x
                    blockSelected = blockNumber
            self.insertBlocktoNode(blockSelected)
            #NOT DONE YET    
         






#always use the root node for this algorithm to work. From the root 
#the algorithm start to calculate where to place the Data Block(the rectangle)
def insertDataBlock(root: TreeNode, rect: Rectangle):





    
    





    