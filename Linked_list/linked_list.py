class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def getLabel (self):
        return self.label

    def setLabe (self , label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

class BinarySeachTree:

    def __init__(self):
        self.root = None

    def insert(self, label):

        # create a new node
        node = Node(label)

        # verify if the tree is empty
        if self.empty():
            self.root = node
        else:
            # tree not empty, insert recursively
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node != None:
                    dad_node = curr_node

                    #verify if goes to left or right
                    if node.getLabel() < curr_node.getLabel():
                        curr_node = curr_node.getLeft()
                    else:
                        curr_node = curr_node.getRight()
                else:
                    #if curr_node is None, then it found where to insert
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)

                    break


    def empty(self):
        if self.root == None:
            return True
        return False

    #show the pre-order(root,left,right)
    def show(self, curr_node):
        if curr_node != None:
            print('%d' % curr_node.getLabel(), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())

    def getRoot(self):
        return self.root

t = BinarySeachTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.getRoot())





























