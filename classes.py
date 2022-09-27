class MyList:  #List impelementation in python
    def __init__(self,initial_data):
        self.data = initial_data
        self.length = 0
        for item in self.data:
            self.length +=1

    def appendmethod(self,new_item):
        self.data = self.data +[new_item]
        self.length +=1

my_list = MyList([1,2,3,4,5])
print(my_list.data)
print(my_list.length)
my_list.appendmethod(6)
print(my_list.data)
print(my_list.length)

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x): #appends item twice
        self.add(x)
        self.add(x)

bag1 = Bag() #Instance 1 of the bag class
bag1.add([1,2,3])
print(bag1.data)
bag1.addtwice([2,3,4])
print(bag1.data)