#program to check if the number is primr or not

def prime(n):
    if n==1:
        print("false")
    elif n==2:
        print("true")
    else:
        for i in range(2,n)    :
             if n%i==0 :
                print("false")   

prime(3)      


