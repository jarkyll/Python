#!/usr/bin/env python
import sys



class User:
    name = ""
    age = 0
    height = 0
    weight = 0

    def display(self):
        print("")
        print('User Information:')
        print('User Name  :', self.name)
        print('User Age   :', self.age)
        print('User Height:', self.height)
        print('User Weight:', self.weight)

    def readinput(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.height = input("Height: ")
        self.weight = input("Weight: ")

    def save(self):
        t = open("user.info", "w")
        t.write(self.name + "\n")
        t.write(self.age + "\n")
        t.write(self.height + "\n")
        t.write(self.weight + "\n")
        t.close()

    def file(self):
        f = open("user.info", "r")
        self.name = f.readline().rstrip()
        self.age = int(f.readline())
        self.weight = int(f.readline())
        self.height = int(f.readline())

theUser = None

if len(sys.argv) > 1 and sys.argv[1] == "READ":
    theUser = User()
    theUser.loadFromFile()
else:
    theUser = User()
    theUser.readinput()
    theUser.save()
    
theUser.display()
