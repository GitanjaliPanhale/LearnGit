def moveapples(input1,input2):
    s=sum(input2)//input1
    c=0
    for i in input2:
        if(i>s):
            c=c+(i-s)
    return c    
def pushzeros(input1,input2):
    c=input1.count(0)
    l=[]
    for i in input1:
        if(i!=0):
            l.append(i)
    for i in range(c):
        l.append(0)
    return l
print(moveapples(5,[2849,1620,705,1,30]))
print(pushzeros([0,3,0,3,0],5))
