class Node:

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.middleList = []

    def adjustMiddle(self):
        for x in self.middleList: #for every value in middleList check if its in right position
            if self.leftChild and x < self.leftChild.data:
                self.middleList.remove(x)
                self.leftChild.__insertFloat(x)
            elif self.rightChild and x > self.rightChild.data:
                self.middleList.remove(x)
                self.rightChild.__insertFloat(x)
        return


    def __insertFloat(self,data):
        if self.leftChild and self.leftChild.data > data: #find node to add float in its middleList
            return  self.leftChild.__insertFloat(data)
        if self.rightChild and self.rightChild.data < data:
            return  self.rightChild.__insertFloat(data)
        self.middleList.append(data) #found proper node, append float in middleList
        self.middleList.sort()
        return True

    def __insertInt(self,data):
        if data < self.data:    #find proper position to attach node
            if not self.leftChild:
                self.leftChild = Node(data)
                self.adjustMiddle()
                return True
            else:
                return self.leftChild.__insertInt(data)
        elif data >= self.data:
            if not self.rightChild:
                self.rightChild = Node(data)
                self.adjustMiddle()
                return True
            else:
                return self.rightChild.__insertInt(data)
        return False

    def insert(self,data):
        if isinstance(data,int): #check which insert to call
            return self.__insertInt(data)
        elif isinstance(data,float):
            return self.__insertFloat(data)
        else:
            print('Invalid Data')
        return

    def print(self):
        printedRoot = False #flag for printing root naive approach*
        if self.leftChild:
            self.leftChild.print()
        if len(self.middleList) > 0:
            for x in self.middleList:
                if x > self.data and not printedRoot:
                    print(self.data,end=' ')
                    printedRoot = True
                print(x,end=' ')
            if not printedRoot:
                print(self.data,end=' ')
        else:
            print(self.data,end=' ')
        if self.rightChild:
            self.rightChild.print()


    def __searchInt(self,data):
        if self.data == data:   #if int data found
            return  True
        else:
            if self.leftChild and data < self.data: #keep traversing for finding required node
                return self.leftChild.__searchInt(data)
            if self.rightChild and data > self.data:
                return  self.rightChild.__searchInt(data)
            return False

    def __searchFloat(self,data):
        if self.leftChild and self.leftChild.data > data: #keep traversing for finding proper node whose middle list might contain reqd data
            return  self.leftChild.__searchFloat(data)
        if self.rightChild and self.rightChild.data < data:
            return  self.rightChild.__searchFloat(data)
        if data in self.middleList: #found node and if data in middle list
            index = self.middleList.index(data)
            return True
        return False

    def search(self,data):
        if isinstance(data,int):#which search to call
            return self.__searchInt(data)
        elif isinstance(data,float):
            return self.__searchFloat(data)
        else:
            print('Invalid Value')
   
    def __removeFloat(self,data):
        if self.leftChild and self.leftChild.data > data:#keep trversing nodes to find reqd data in middle list
            return  self.leftChild.__removeFloat(data)
        if self.rightChild and self.rightChild.data < data:
            return  self.rightChild.__removeFloat(data)
        if data in self.middleList: #found node and data in middle list remove it
            self.middleList.remove(data)
            return True
        return False

   
    def __removeInt(self,data):
        if self.data == data:   #if node found
            if self.leftChild:  #if has left child make left child value as node's value and adjust accrodingly
                self.data = self.leftChild.data
                result = self.leftChild.__removeInt(self.data)
                if isinstance(result,tuple):
                    leftC = result[0]
                    mList = result[1]
                    self.leftChild = leftC
                    self.middleList = self.middleList + mList
                    return (self,[])
                else:
                    return result
            if self.rightChild:#if doesn't has left and has rightChild make right as node and change accordingly
                self.data = self.rightChild.data
                result = self.rightChild.__removeInt(self.data)
                if isinstance(result,tuple):
                    rightC = result[0]
                    mList = result[1]
                    self.rightChild = rightC
                    self.middleList = self.middleList + mList
                    return (self,[])
                else:
                    return result
            if len(self.middleList) > 0:    #if only middleList exist return middlelist to its parent
                return (None,self.middleList)

            return (None,[])    #if no left,right and middlelist
        else:
            if self.leftChild and data < self.data: #keep traversing for finding reqd node
                result = self.leftChild.__removeInt(data)
                if isinstance(result,tuple):
                    leftC = result[0]
                    mList = result[1]
                    self.leftChild = leftC
                    self.middleList = self.middleList + mList
                    return (self,[])
                else:
                    return result
            if self.rightChild and data > self.data:
                result = self.rightChild.__removeInt(data)
                if isinstance(result,tuple):
                    rightC = result[0]
                    mList = result[1]
                    self.rightChild = rightC
                    self.middleList = self.middleList + mList
                    return (self,[])
                else:
                    return result
            return False

    def remove(self,data):
        if isinstance(data,int):#which node to call
            return self.__removeInt(data)
        elif isinstance(data,float):
            return self.__removeFloat(data)
        else:
            print('Invalid Value')

    def printLevelOrder(self):
        nodes = []
        nodes.append(self)
        while len(nodes) > 0:
            x = nodes[0]
            nodes.remove(x)
            if isinstance(x,Node):
                print(x.data,end=' ')
                if x.leftChild:
                    nodes.append(x.leftChild)
                if x.middleList:
                    nodes.append(x.middleList)
                if x.rightChild:
                    nodes.append(x.rightChild)
            elif isinstance(x,list):
                for f in x:
                    print(f,end=' ')
        return