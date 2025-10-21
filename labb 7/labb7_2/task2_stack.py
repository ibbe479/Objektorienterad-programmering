class Stack:
    def __init__(self):
        self.itmes = []

    def push(self, item):
        """lägger till på topen av stack"""
        self.itmes.append(item)

    def pop(self):
        """tar bort och returnerar topen av stack"""
        if not self.is_empty():
            return self.itmes.pop()
        raise IndexError("empty stack")

        

    def top(self):
        """returnerar topen av stack utan att ta bort den"""
        if not self.is_empty():
            return self.itmes[-1]
        raise IndexError("empty stack")
        
    def is_empty(self):
        return len(self.itmes) == 0

    def size(self):
        return len(self.itmes)

