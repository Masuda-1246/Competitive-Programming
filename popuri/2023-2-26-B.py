n = int(input())
x = map(int, input().split())

new_x = sorted(x)

print(sum(new_x[n:-n]) / (n * 3))