if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr) #turn map into list
    lindex=len(l)-1
    runnerUp=l[lindex]
    while(lindex<0): # while loop to get the runner-Up
        if(runnerUp>l[lindex]):
            runnerUp=l[lindex]
        lindex-=1
    print(runnerUp)