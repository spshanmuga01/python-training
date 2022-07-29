import re
t = open("test.txt","r")
print(t.read())
lst = re.findall('[^,;\s] + @[^,;s]',t)