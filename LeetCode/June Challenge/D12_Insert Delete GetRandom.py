import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nums = []
        self._positions = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._positions:
            return False
        self._nums.append(val)
        self._positions[val] = len(self._nums)-1
        return True;
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self._positions:
            return False;
        
        pos = self._positions[val]
        self._nums[pos] = self._nums[-1]
        self._positions[self._nums[pos]] = pos
        self._nums.pop()
        self._positions.pop(val)
        return True;
        

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return self._nums[random.randint(0, len(self._nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()