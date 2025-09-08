#write a python prgm which accept any Three numerical values and Biggest among them by using SimpleIFStmts
#SimpleIFStmtEx4.py
a=int(input("enter values of a:"))
b=int(input("enter values of b:"))
c=int(input("enter values of c:"))

if(a>b) and (a>c):
    print("Big({},{},and{})={}:".format(a,b,c,a))
if(b>a) and (b>c):
    print("Big({},{},and{})={}:".format(a,b,c,b))
if(c>a) and (c>b):
    print("Big({},{},and{}={}:".format(a,b,c,c))