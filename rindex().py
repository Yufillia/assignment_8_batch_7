# rindex() (Find last occurrence of a substring)
s, sub = "banana", "an"
for i in range(len(s) - len(sub), -1, -1):
    if s[i:i+len(sub)] == sub:
        print(i)
        break