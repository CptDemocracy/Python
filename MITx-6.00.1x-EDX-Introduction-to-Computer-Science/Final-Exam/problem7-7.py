"""
Final Exam Problem 7-7

Consider the class definitions contained in FamilyTree.py:

[ref.href] https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_6+2T2015+type@asset+block/FamilyTree.py

Class Member is a class that represents a single person in the 
family, and Class Family represents the whole family tree.

You are to write code for the method cousin of the class Family 
according to the docstring in FamilyTree.py and the definitions 
for degree removed and cousin type right before Problem 7-4.

Paste your entire definition of the Family class in the following 
box. You may assume that the class Member is defined for you. You 
should not alter Member in any way, but may alter any part of Family 
that you deem necessary.
"""

class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        # raise NotImplementedError()
        
        nodeA = self.names_to_nodes.get(a, -1)
        nodeB = self.names_to_nodes.get(b, -1)
        cousinType = -1
        if nodeA == -1 or nodeB == -1:
            raise ValueError("children not related")

        if nodeA == nodeB:
            return (cousinType, 0)

        areNonCousins  = False
        PARENTS_A_LIST = []
        parentA = nodeA.get_parent()
        while parentA != None:
            PARENTS_A_LIST.append(parentA)
            if parentA == nodeB:
                areNonCousins = True
            parentA = parentA.get_parent()

        PARENTS_B_LIST = []
        parentB = nodeB.get_parent()
        while parentB != None:
            PARENTS_B_LIST.append(parentB)
            if parentB == nodeA:
                areNonCousins = True
            parentB = parentB.get_parent()

        COMMON_ANCESTORS_LIST = []
        smallestParentsList  = PARENTS_A_LIST
        biggestParentsList = PARENTS_B_LIST
        if len(PARENTS_B_LIST) > len(PARENTS_A_LIST):
            smallestParentsList  = PARENTS_B_LIST
            biggestParentsList = PARENTS_A_LIST
        for parent in smallestParentsList:
            try:
                ind = biggestParentsList.index(parent)
                COMMON_ANCESTORS_LIST.append(biggestParentsList[ind])
            except ValueError:
                pass

        if not areNonCousins:
            cousinType = len(biggestParentsList) - len(COMMON_ANCESTORS_LIST)
        degreesRemoved = abs(len(biggestParentsList) - len(smallestParentsList))
            
        return (cousinType, degreesRemoved)
