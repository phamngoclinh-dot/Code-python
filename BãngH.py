arr=[]
for _ in range(int(input())):
    n=input()
    b,s=map(int,input().split())
    d={'name':n,'bailam':b,'submit':s}
    arr.append(d)

arr.sort(key= lambda x:(-x['bailam'],x['submit'],x['name']))
for x in arr:
    print(x['name'],x['bailam'],x['submit'])