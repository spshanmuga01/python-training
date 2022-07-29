def function(n):
    return lambda a : a*n
double = function(10)
print(double(11))