class student:
  __name = "Debjeet"
  def __init__(self):
    print(f"Hey I am a student, My name is {self.__name}")
    self.__Displayinfo()
  def __Displayinfo(self):
    print(f"My name is {self.__name}")

obj = student()
