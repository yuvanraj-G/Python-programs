#String palindrome

s = "amma"
rev = ""
for i in s:
    rev = i + rev
print(rev)

if s == rev :
    print("Palindrome")
else:
    print("Not Palindrome")

        