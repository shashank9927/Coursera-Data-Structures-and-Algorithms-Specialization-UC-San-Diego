def calc_fib(n):
    li=[]
    li.append(0)
    li.append(1)
    if n<=1:
        return n
    else:
        for i in range(2,n+1):
            li.append(li[i-1]+li[i-2])
    return li[-1]

print(calc_fib(int(input("Enter n? "))))
