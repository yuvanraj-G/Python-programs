# reverse by words 
str = "raj yuvan am i "
word = ""
rev = ""
for i in str:
    if i != " ":
        word = word + i
    else:
        rev=word+" "+rev
        word=""
print(rev)            