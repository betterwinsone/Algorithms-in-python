#sazxcdfv
#01234567
adj=[[1,3],[2],[1],[0,4,5],[3,5,6,7],[3,4,6],[5,4,7],[4,6]] #graph to adjacency list
level={0:0}
parent={0:None}
i=1
frontiter=[0]
print(frontiter)
while frontiter:
    next=[]
    for u in frontiter:
        for v in adj[u]:
            if v not in level:
                level[v]=i
                next.append(v)
                parent[v]=u
    frontiter=next
    print(frontiter)
    i=i+1
print(frontiter)
print(level)
print(parent)