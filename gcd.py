# iteration
x=int(input("enter number:"))
y=int(input("enter number:"))
gcd=0
for i in range(1,x+1):
    if x%i==0 and y%i==0 :
        gcd=i
print(gcd)

# recursion
def gcd_fun(x,y):
    if x==0 :
        return y
    else:
        return gcd_fun(y%x, x)

num1=gcd_fun(132,320)
print(num1)


# euclidion 
def euclid_hcf(a,b):
    while a>0 :
        a,b=b%a,a
    return b

num2=euclid_hcf(132,320)
print(num2)