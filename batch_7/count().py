# count() (Count occurrences of a substring)
s, sub = "banana", "an"
print(sum(1 for i in range(len(s) - len(sub) + 1) if s[i:i+len(sub)] == sub))