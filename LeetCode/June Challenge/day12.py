from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.l:
            return False
        self.l.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.l:
            return False
        del self.l[(self.l.index(val))]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.l[randint(0,len(self.l)-1)]