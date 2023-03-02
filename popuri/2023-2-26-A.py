s = input()

for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        print(i + 1)