import re
z = "He is lives in France"
x = re.findall("France",z) #finds the match and print the value
print(x)
y = re.split("\s",z) #split the all string separtely and returns as list
print(y)
c = re.search("France",z) #will search the word given 
print(c.span())