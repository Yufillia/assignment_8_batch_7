# removesuffix() - Remove a specific suffix
s = "example.txt"
suffix = ".txt"
if s.endswith(suffix):
    s = s[:-len(suffix)]
print(s)