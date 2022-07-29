def sum(n):
    if n==1:
        return 1
    else:
        return(sum(n-1)+n)
add = int(input())
res = sum(add)
print(res)


