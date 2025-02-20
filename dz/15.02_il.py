#1
s = "3" * 207
while '9999' in s or "333" in s:
    if "9999" in s:
        s = s.replace("9999", "3", 1)
    else:
        s = s.replace("333", "99", 1)
print(s)
 # Ответ: 33

 #2

s = "9" * 207
while '9999' in s or "333" in s:
    if "9999" in s:
        s = s.replace("9999", "3", 1)
    else:
        s = s.replace("333", "99", 1)
print(s)

# Ответ: 3999

#3
s = "3" * 194
while '9999' in s or "333" in s:
    if "9999" in s:
        s = s.replace("9999", "3", 1)
    else:
        s = s.replace("333", "99", 1)
print(s)
# Ответ: 993

#4

s = "9" * 194
while '9999' in s or "333" in s:
    if "9999" in s:
        s = s.replace("9999", "3", 1)
    else:
        s = s.replace("333", "99", 1)
print(s)
# Ответ: 3

#5

s = "3" * 185
while '9999' in s or "333" in s:
    if "9999" in s:
        s = s.replace("9999", "3", 1)
    else:
        s = s.replace("333", "99", 1)
print(s)

# Ответ: 9933
