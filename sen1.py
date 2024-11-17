def sort1(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a


name="ghanu"
a=10

def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum


