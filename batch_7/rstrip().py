# rstrip() (Remove trailing spaces)
s = "Hello, World!   "
while s.endswith(" "):
    s = s[:-1]
print(s)