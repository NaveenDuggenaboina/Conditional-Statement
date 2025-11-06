# prgm for Accepting Two Numerical value and decide Biggest and check for equlity also
 #SimpleIFstmtEx1.py
a=int(input("enter first value:"))
b=int(input("enter second values:"))
if(a>b):
    print("Big({},{})={}:".format(a,b,a))
if(b>a):
    print("Big({},{})={}:".format(a,b,b))
if(a==b):
    print("Both the values are Equal")