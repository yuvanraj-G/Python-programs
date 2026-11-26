a = 4584924843414
n = 4
result = 0
place = 1

while a > 0 :
    digit = a % 10
    if digit != n:
        result = digit * place + result
        place = place * 10

    a = a // 10   
print(result)        