class CountList:

    def __init__(self,*args):

        self.value=[x for x in args]

        self.count={}.fromkeys(range(len(self.value)),0)

    def __len__(self,value):

        return len(self.value)

    def __getitem__(self,key):

        self.count[key] += 1

        return self.value[key]

print("test")
