if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr) #turn map into list
    aux=0
    bigNumber=l[aux]
    residuals=[]
    while(aux<n): # while loop to get the biggest number out the list
        if(bigNumber<l[aux]):
            bigNumber=l[aux]
        aux+=1
    aux=0
    while(aux<n): #while loop to get the residuals of every single number
        residuals.append(l[aux]-bigNumber)
        aux+=1
    aux=0
    maxResidual=residuals[aux]
    while(aux<n):
        if(maxResidual==0 or (maxResidual<=residuals[aux] and residuals[aux]!=0)):#conditional to keep exploring the list as long as the participant is the best runner or not the second best runner
            maxResidual=residuals[aux]
            runnerUp=aux
        aux+=1
    print(l[runnerUp])  