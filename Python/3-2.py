class Vector(object):
    def __init__(self):
       self.val=[]
       self.length=len(self.val)
    def __init__(self,val):
        self.val = val
        self.length = len(self.val)
    def add(self,vec):
        if self.length != vec.length:
            raise Exception
        return Vector([i + j for i,j in zip(self.val,vec.val)])
    def subtract(self,vec):
        if self.length != vec.length:
            raise Exception
        return Vector([i - j for i,j in zip(self.val,vec.val)])
    def dot(self,vec):
        if self.length != vec.length:
            raise Exception
        return sum([i * j for i,j in zip(self.val,vec.val)])
    def norm(self):
        return (sum([i**2 for i in self.val]))**.5
    def __str__(self):
        return "(" + str((self.val))[1:len(str(self.val))-1] + ")"
    def equals(self,vec):
        if vec == None:
            return False
        return self.val == vec.val
