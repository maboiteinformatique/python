def doublons(a: list):
    b = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return True
    else:
        return False
    
   
print(doublons([1,2,3,4,9]))


           
