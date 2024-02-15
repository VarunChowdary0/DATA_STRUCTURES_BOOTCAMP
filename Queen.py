def FindThePositionsForQueens(Places,n):
    count =0 
    for x in range(n):
        count+=1
        for z in range(n):
            if Places[x][z] == True:
                while True:
                    if x == z or 
n = 5
Places = [ [True for i in range(n)] for j in range(n) ]
print(Places)