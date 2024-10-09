class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()

    def fullname(self):
        return f"{self.fname} {self.lname}"
    
    def initials(self):
        return f"{self.fname[0].upper()}.{self.lname[0].upper()}"
    
a1 = Name("john", "SMITH")
print(a1.fname)
print(a1.lname)
print(a1.fullname)
print(a1.initials)