'''def is_even_num(lt):
    enum = []
    for n in lt: 
        if n % 2 == 0:
            enum.append(n)
    return enum
li = [1,2,3,4,5,6,7,8,9]
print(is_even_num(li))'''

def even(l1):
    for i in l1:
        if i%2==0:
            print(i)

even([2,4,2,2,2,22,2,2,2,2,2,5,6] )
