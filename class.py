class Student:
  # Attribute
  name = "default name"
  fone = 113

  # Initializer
  def __init__(self, name, fone):
    self.name = name
    self.fone = fone

  # Public method
  def display_name(self):
    print "Name is: ", self.name
    pass

  def display_fone(self):
    print "Fone is: ", self.fone
    pass

  # Private and Protected method
  # TODO

# Define
student_first = Student("Join", 12345678)
student_last = Student("Mark", 87654321)


# First student info
student_first.display_name()
student_first.display_fone()

# Last student info
student_last.display_name()
student_last.display_fone()