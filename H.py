def compute_gcd(x, y):
    if y!=0:
        return(compute_gcd( y, x % y))
    else:
        return int(x)

def compute_lcm(x, y):
    c=compute_gcd(x,y)
    lcm = (x*y)//c
    return lcm

a,b=input().split()
a=int(a)
b=int(b)
print(compute_gcd(a,b)+compute_lcm(a,b))