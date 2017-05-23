from balancedTernarySearchTree.balancedTernarySearchTree import balancedTernarySearchTree

def errorHandle(value=None):
    print('Invalid Instruction')

tree = balancedTernarySearchTree()
actions = {
    "push":     tree.push,
    "remove":   tree.remove,
    "search":   tree.search,
    "print":    tree.print,
    "printLevelOrder": tree.printLevelOrder
}

def readInput():
    with open('input.txt','r') as file: #change name of input file to have other file as input
        for line in file:
            values = line.split()
            function = values[0]
            if len(values) > 1:
                value = values[1]
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                actions.get(function,errorHandle)(value)
            else:
                actions.get(function,errorHandle)()
    file.close()

if __name__ == '__main__':
    readInput()