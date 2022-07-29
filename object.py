class Student:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def myfunc(self):
    print("Hello my name is " + self.first + self.last)

p1 = Student("peter","john" )
p1.myfunc()
del p1