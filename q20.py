sum = 0
l = [0]*1000
l[0] = 1

def mult(l , i):
    num = str(i)
    for digit in range(len(num)-1,-1,-1):
        out = helper()*int(digit)
        
    return l

for i in range(2,101):
    l = mult(l , i)

for i in range(0,len(l)):
    sum = sum + l[i]

print(sum)