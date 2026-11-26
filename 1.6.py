n=12345
total=1
while n>0:
    digit=n%10
    total=total*digit

    n=n//10 
print(total)