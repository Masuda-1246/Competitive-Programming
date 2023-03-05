N, K = map(int, input().split())
ans = 1
for i in range(1,N+1):
  if i == 1:
    ans *= K
  else:
    ans *= K-1
print(ans)