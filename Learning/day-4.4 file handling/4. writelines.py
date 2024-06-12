# Way 1 to add lines

x = open('myf.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

# way 2 to add lines 

x = open('myf.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
f.writelines(lines + '\n')
f.close()

