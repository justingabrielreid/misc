#!/usr/bin/python3

''' How to setup objects of classes to use comparison operators: 
    ===, <, > 

    In python objects need to be of the same type and support the comparison operators to be compared with each other. The physical feature class below will be an example of setting up objects for comparison. 

'''

class physicalFeatures(object):
    #this class represents the height, weight and name of the person
    def __init__(self, name , height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight

def main():
    donovan = physicalFeatures('Donovan Reid', '5\'10', 155)
    justin = physicalFeatures('Justin Reid', '5\'10', 165)
    justin2 = justin
    print (justin > donovan)
    print (justin < donovan)
    print (justin == justin2)
if __name__ == '__main__':
    main()
