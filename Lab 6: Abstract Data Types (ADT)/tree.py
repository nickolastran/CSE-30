
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        if self.leftChild == None:
            return ""
        else:
            return self.leftChild

    def getRightChild(self):
        if self.rightChild == None:
            return ""
        else:
            return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        return (f"{self.key}[{self.getLeftChild()}][{self.getRightChild()}]")

if __name__ == "__main__":
    r = BinaryTree("a")
    print(r)
    r.insertLeft("b")
    r.insertRight("c")
    print(r)
    r.getLeftChild().insertLeft("d")
    r.getLeftChild().insertRight("e")
    r.getRightChild().insertLeft("f")
    print(r)
    print(r.getRootVal())
    print(r.getLeftChild())
    print(r.getRightChild())
