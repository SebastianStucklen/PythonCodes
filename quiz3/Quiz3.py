def BiggestOfThree(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
a = input("give me number a")
b = input("give me number b")
c = input("give me number c")
print(BiggestOfThree(a,b,c))



list1 = []
for i in range (10):
    print("gimme a number", end = " ")
    j = int(input())
    list1.append(j)
print(list1)
list2 = list1.copy()
for i in range(10):
    list2[i] *= 2
print(list2)