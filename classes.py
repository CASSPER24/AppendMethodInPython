class MyList:  #List impelementation in python
    def __init__(self,initial_data):
        self.data = initial_data
        self.length = 0
        for item in self.data:
            self.length +=1

    def appendmethod(self,new_item):
        self.data = self.data +[new_item]
        self.length +=1
