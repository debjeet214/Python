# Custom Exception message print

class CustomException(Exception):
  pass

def causeError():
  raise CustomException("this is a custom exception")  # this custom message will be shown in error box

causeError()
