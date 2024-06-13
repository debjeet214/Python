# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position.

with open('file.txt', 'r') as f:
  f.seek(10)           # Move to the 10th byte in the file
  data = f.read(5)     # Read the next 5 bytes whatever is in the file.


# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. 

with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)
  current_position = f.tell()      # Save the current position
  f.seek(current_position)         # Seek to the saved position


# The TRUNCATE() function returns n with d decimal places truncated.
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())
