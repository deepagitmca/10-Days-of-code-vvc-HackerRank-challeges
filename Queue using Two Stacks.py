# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
c =[]
for i in range(int(n)):
    a =input()
    b =int(a[0])
    if(b==1):
        t = a.split(' ')[-1]
        c.append(t)
    elif(b==2):
        c.pop(0)
    elif(b==3):
        print(c[0])