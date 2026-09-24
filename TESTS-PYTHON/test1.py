def somme_pair(b: list):
    a = 0
    for i in b:
        if i % 2 == 0:
            a += i
    return a

print(somme_pair([1,2,3,4,5,6]))