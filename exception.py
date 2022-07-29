x = 4
try:
    print(x)
except:
    print('this is incorrect')
finally:
    print("this is correct")    

#x = -2

#if x < 0:
    #raise Exception("digit is not equal to zero")

a = 123
if not type(a) is str:
    raise TypeError("it is not a string")
