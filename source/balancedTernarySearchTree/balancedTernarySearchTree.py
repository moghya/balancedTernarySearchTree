from balancedTernarySearchTree.Node import Node


class balancedTernarySearchTree:
    def __init__(self):
        self.rootNode = None
        return

    def push(self,data):
        if not self.rootNode:
            self.rootNode = Node(data)
            print('Inserted ' + str(data))
            return True
        elif self.rootNode.insert(data):
                print('Inserted ' + str(data))
                return  True
        return False

    def print(self):
        if self.rootNode:
            print('\nPrinting Tree')
            self.rootNode.print()
        else:
            print('Empty Tree')
        return

    def search(self,data):
        if not self.rootNode:
            print('Empty Tree')
        elif self.rootNode.search(data):
            print('Data value ' + str(data) + ' found in search')
            return True
        else:
            print('Data value ' + str(data) + ' not found in search')
            return False

    def remove(self,data):
        if not self.rootNode:
            print('Empty Tree')
        elif self.rootNode.remove(data) != False:
            print('Removed Data Value '+ str(data))
            return True
        else:
            print('Data value '+str(data)+' not found to remove')
        return False

    def printLevelOrder(self):
        if self.rootNode:
            print('\nPrint Level Order Traversal')
            self.rootNode.printLevelOrder()
        else:
            print('Empty Tree')