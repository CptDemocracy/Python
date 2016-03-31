"""
Problem 6.
For this exercise, you will be coding your very first class, a Queue class.
"""

class Queue(object):
    
    def __init__(self):
        self.vals = []
    
    def insert(self, e):
        self.vals.insert(0, e)
        
    def remove(self):
        try:
            elem = self.vals[len(self.vals) - 1]
            self.vals.remove( elem )
            return elem
        except (ValueError, IndexError) as e:
            raise ValueError()
