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