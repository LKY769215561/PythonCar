def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

a = my_abs(-1098)
print(a)

def power(x):
    return x * x

print(power(255))

def power2(x,n):
    r = 1
    while n > 0:
        r = r * x
        n = n - 1
    return r

print(power2(4,3))

def log(name,gender):
    print('name:',name)
    print("gender:",gender)

log('carey',1)

def log2(name,gender,age=6,city="nanyang"):
    print('name',name)
    print('gender',gender)
    print('age',age)
    print('city',city)


log2('carey2',1,city='nanyang2')

def add_end(L=[]):
    L.append('end')
    print(L)
add_end([1,2,3])
add_end([4,5,6])

