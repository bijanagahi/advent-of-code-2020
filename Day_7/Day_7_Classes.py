class Bag(object):

    def __init__(self, ID):
        self.ID = ID
        self.parents = []
        self.children = []
        self.canHoldTheBag = False

    def addParent(self, parent):
        self.parents.append(parent)
        # If we we're trying to add a parent to a bag that currently can hold the magic bag,
        #   we need to update the parent as well
        if self.canHoldTheBag:
            parent.promote()
    
    def addChild(self, child):
        self.children.append(child)
    
    def getChildren(self):
        return self.children
    
    def count(self):
        if len(self.children) < 1:
            return 1
        return 1+sum([int(count)*child.count() for child,count in self.children ])
    
    def promote(self):
        self.canHoldTheBag = True
        for parent in self.parents:
            parent.promote()
    
    def __str__(self):
        return f"{self.ID} bag"
    
class Luggage(object):
    
    def __init__(self):
        self.bagLookup = {}
    
    def addBag(self, bag):
        # print("Adding:", bag.ID)
        self.bagLookup[bag.ID] = bag
    
    def getBag(self, ID):
        return self.bagLookup[ID]
    
    def contains(self, ID):
        return ID in self.bagLookup
    
    def countMagicBags(self):
        counter = 0
        for bag in self.bagLookup.values():
            if bag.canHoldTheBag:
                counter += 1
        return counter
    
    def __str__(self):
        s = ''
        for ID,bag in self.bagLookup.items():
            s += f"BagID: {ID}, parents: {bag.parents}, children: {bag.children}\n"
        return s