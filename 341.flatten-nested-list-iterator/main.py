# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        #flatten list recursive
        '''
        def flatten(nestedList):
            res = []
            for i in nestedList:
                if i.isInteger():#if is interger
                    res.append(i.getInteger())
                else:#if is not interger
                    res.extend(flatten(i.getList()))
            return res
        '''
        #flatten while loop
        i = 0
        while True:
            #break point
            if i>=len(nestedList):
                break

            iter = nestedList[i]
            if iter.isInteger():#is int check next
                i+=1
            else:#is list flaten it 
                nestedList = nestedList[:i]+nestedList[i].getList()+nestedList[i+1:]

        #initialize
        self.index = -1
        self.flatList = nestedList
        self.size = len(self.flatList)
    

    def next(self) -> int:
        self.index+=1
        return self.flatList[self.index]
    
    def hasNext(self) -> bool:
        if self.index+1>=self.size:
            return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())