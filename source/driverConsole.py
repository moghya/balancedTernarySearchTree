from balancedTernarySearchTree.balancedTernarySearchTree import balancedTernarySearchTree

def myTree():
    div = balancedTernarySearchTree()
    div.push(5)
    div.push(7)
    div.push(2)
    div.push(4)
    div.push(5.5)
    div.push(4.4)
    div.push(3.3)
    div.push(3)
    div.remove(5.5)
    div.remove(5.5)
    div.printLevelOrder()
    div.print()
    return

if __name__ == '__main__':
    myTree()