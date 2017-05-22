n, m, v = map(int, input().split())

a = []

for i in range(n+1):
    a.append([])
    
for i in range(m):
    j, k = map(int, input().split())
    a[j].append(k)
    a[k].append(j)

for i in range(n+1):
    a[i].sort()

check = [False] * (n+1)    
def dfs(a, check, now):
    if check[now] == True:
        return
    check[now] = True
    print(now, end=' ')
    for next_vertex in a[now]:
        dfs(a, check, next_vertex)
dfs(a, check, v)
print()

def bfs(a, start):
    check = [False] * (n+1)
    queue = []
    queue.append(start)
    check[start] = True
    
    while queue:
        now = queue[0]
        queue.pop(0)
        print(now, end=' ')
        for next_vertex in a[now]:
            if check[next_vertex] == True:
                continue
            queue.append(next_vertex)
            check[next_vertex] = True

bfs(a, v)