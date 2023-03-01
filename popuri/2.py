def myfunc(number):
    if number <= 26:
        return chr(number + 64)
    elif number % 26 == 0:
        return myfunc(number // 26 - 1) + chr(90)
    else:
        return myfunc(number // 26) + chr(number % 26 + 64)

n = int(input())
print(myfunc(n))