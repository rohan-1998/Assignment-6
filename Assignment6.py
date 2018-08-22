#Question 1
def area_circle(r):
    area=float(4*3.14*r*r)
    print(area)
radius=int(input("enter the radius"))
area_circle(radius)

#Question 2
def perfect(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(num==sum):
        print(sum)
for i in range(1,1000):
    perfect(i)

#Question 3
a=int(input("enter the number"))
for i in range(1,11):
    print("{} * {} = {}".format(a,i,a*i))

#Question 4
def power(n,p):
    if(p==1):
        return n
    else:
        return n*power(n,p-1)
r=int(input("enter the number"))
p=int(input("enter the power"))
print(power(r,p))
