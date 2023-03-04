def to16(num):
    if num <= 9:
        return str(num)
    else:
        return chr(num + 55)

n = int(input())

print(to16(n // 16) + to16(n % 16))