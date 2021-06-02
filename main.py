# my very first recursive function with help!

# by oran collins & max
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210602


# Node Class
class Node:
    """Binary tree node class """
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
 
    def __repr__(self) -> str:

        return f"Node here {self.data}"   

class Tree:
    def __init__(self):
        self.root = Node()

    def display(self):
        self.__display__(self.root)

    def __display__(self, node):
        if node is None:
            return
        
        if node.data is None:
            return
        print(node.data)


        self.__display__(node.right)
        self.__display__(node.left)

    # helper function + data passing variable
    def __insert__(self, node, data):
        """insert data into the binary tree"""
        

        # base case 1 Something but empty
        if node.data is None:
            node.data = data
            # IMPORTANT!!!!
            # exit early
            return

        # recursive cases
        if node.data > data:
            if node.left is None:
                node.left = Node() 
            self.__insert__(node.left, data)
        else:
            if node.right is None:
                node.right = Node()
            self.__insert__(node.right, data)

    # main function
    def insert(self, data):
            # if not find()
            self.__insert__(self.root, data)
        
        # base case
        # Base case 1:


    
    def find(self):
        pass



library = Tree()

library.insert(5)
library.insert(10)
library.insert(4)


library.display()
# print(library.root)
# print(library.root.right)
# print(library.root.left)
# print(library.root.right.right)
# print(library.root.right.left)

# library.insert(7)
# print(library.root)

# 