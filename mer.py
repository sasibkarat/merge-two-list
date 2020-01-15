a=[]
b=[]
n=int(input("Enter number of elements in first:"))
for i in range(1,n+1):
    c=input("Enter element:")
    a.append(c)
n1=int(input("Enter number of elements in second:"))
for i in range(1,n1+1):
    d=input("Enter element:")
    b.append(d)
new=a+b
new.sort()
print("Sorted list is:",new)
