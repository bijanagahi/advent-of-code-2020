from Day_7_helpers import readInputFile
from Day_7_Classes import Bag, Luggage



def main():
    handler = open("./input2.txt")
    luggage = Luggage()
    allBags = readInputFile(handler, False) # {bagID:[subbag1, ...]}
    for rootBag, subBags in allBags.items():
        # We have a root bag, and potentially some children.
        # If the root bag doesn't exist, create it and add it to the luggage
        # If it already exists, then we're good
        #   UNLESS! It contains our magic bag then we update.
        newRootBag = Bag(rootBag)
        if not luggage.contains(newRootBag.ID):
            luggage.addBag(newRootBag)
        else:
            newRootBag = luggage.getBag(rootBag)
        for subBag in subBags:
            # First, check if we've hit our magic bag
            if subBag == "shiny gold":
                luggage.getBag(rootBag).promote() #!
            # Check if it exists
            if luggage.contains(subBag):
                luggage.getBag(subBag).addParent(newRootBag)
            else:
                newBag = Bag(subBag)
                newBag.addParent(newRootBag)
                luggage.addBag(newBag)
    print(luggage.countMagicBags())

if __name__ == "__main__":
    main()