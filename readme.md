##Balanced Ternary Search Tree is implemented with following conditions:
    -1. Left child should be smaller than right child
    -2. Left / Right child should contain only integer
    -3. Middle child should contain a sorted list of floats greater than left child and less than right child
    -4. Implement push , remove and print for any given level operations
    -5. It should read inputs from a text file, values separated by a newline

##Methods in balacedTernarySearchTree class:
    -a)push(data) <br/>
        push element in tree if it is float in appropriate middleList else new node attached as child.
    -b)search(search_value)<br/>
        find search value
    -c)remove(remove_value)<br/>
        remove remove_value
    -d)print()<br/>
        prints tree in Left - MiddleList - Nodedata - Right of every node basically depth first traversal
    -e)printLevelOrder()<br/>
        prints level order traversal of tree

<br/><br/>
Implemented method to read input from files line by line in driver.py.<br/>
Required format of input text file is as given in input.txt.<br/>
Console based interaction in driverConsole.py
