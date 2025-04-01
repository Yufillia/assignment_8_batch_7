# upper() (Convert to uppercase)
s = "Hello, World!"
s = "".join(chr(ord(c) - 32) if "a" <= c <= "z" else c for c in s)
print(s)