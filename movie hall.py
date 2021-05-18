nc=int(input())
com=[]
for i in range(nc):
    com.append(input())
c1='add-screen'
c2='reserve-seat'
c3='get-unreserved-seats'
c4='suggest-contiguous-seats'

all ={}
ais={}

#to add a screen(has rows, columns and aisles)
def co1(name,row,col,aisle):
    if (row==0 and len(aisle)>0) or max(aisle)>col :
        print('failure')
        return
    x=[]
    for i in range(row):
        x.append([0]*col)
    all[name]=x
    ais[name]=aisle
    print('success')
    return

#to reserve seats
def co2(name,row,slist):
    x=[]
    try:
        x=all[name][row-1]
    except KeyError:
        print('failure')
        return
    for i in slist:
        if x[i-1]==1 :
            print('failure')
            return 
        x[i-1]=1
    print('success')
    return

#to get unreserved seats
def co3(name,row):
    x=[]
    try:
        x=all[name][row-1]
    except KeyError:
        print('')
        return
    for i in range(len(x)):
        if x[i]==0: print(i+1,end=' ')
    print('')
    return

#to get continuous unreserved seats
def co4(name,n,row,c):
    x=[]
    try:
        x=all[name][row-1]
    except KeyError:
        print('none')
        return
    ai=ais[name]
    le=len(x)
    if (c-n<0 and c+n-1>le): 
        print('none')
        return
    par=True
    if c-n<0 : par=False
    elif c-n>=0:
        for i in range(c-n,c):
            if x[i]==1 or ((i+1 in ai) and i!=c-n and i!=c-1)  :
                par=False
                break
        if par : 
            for i in range(c-n,c):
                print(i+1,end=' ')
            print('')
    if c+n-1<=le and par==False:
        par=True
        for i in range(c-1,c+n-1):
            if x[i]==1  or ((i+1 in ai) and i!=c-1 and i!=c+n-2):
                par=False
                break
        if par : 
            for i in range(c-1,c+n-1):
                print(i+1,end=' ')
            print('')
    if par ==False:
        print('none')
    return
        
#Main class
for i in com:
    div=i.split(' ')
    if div[0]==c1:
        r=int(div[2])
        c=int(div[3])
        aisse=[]
        for j in range(4,len(div)):
            aisse.append(int(div[j]))
        co1(div[1],r,c,aisse)
    if div[0]==c2:
        r=int(div[2])
        rse=[]
        for j in range(3,len(div)):
            rse.append(int(div[j]))
        co2(div[1],r,rse)
    if div[0]==c3:
        co3(div[1],int(div[2]))
    if div[0]==c4:
        co4(div[1],int(div[2]),int(div[3]),int(div[4]))

#sample input
# 9
# add-screen Screen1 12 10 4 5 8 9
# add-screen Screen2 20 25 3 4 12 13 17 18
# reserve-seat Screen1 4 5 6 7
# reserve-seat Screen2 13 6 7 8 9 10
# reserve-seat Screen2 13 4 5 6
# get-unreserved-seats Screen2 13
# suggest-contiguous-seats Screen1 3 3 4
# suggest-contiguous-seats Screen2 4 12 4
# suggest-contiguous-seats Screen2 4 10 3

#sample output
# success
# success
# success
# success
# failure
# 1 2 3 4 5 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 2 3 4
# 4 5 6 7
# none


