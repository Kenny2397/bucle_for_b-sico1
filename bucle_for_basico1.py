for i in range(151):
    print(i)

for i in range(5,1001):
    if i%5==0:
        print(i)

for i in range(101):
    if(i%5==0):
        print("Coding")
        if(i%2==0):
            print('Coding Dojo')
    else:
        print(i)



sumImpares=0
for i in range(500000):
    if(i%2!=0):
        sumImpares=sumImpares+i
        
print(sumImpares)        

for i in range(2018,0,-4):
    print(i)
    

def Contador_flexible(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if(i % mult == 0):
            print(i)
            
Contador_flexible(2,9,3)
