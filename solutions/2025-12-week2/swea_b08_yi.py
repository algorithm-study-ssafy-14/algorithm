def lca(a, b, parent):
    temp = set()
    while a != 0:
        temp.add(a)
        a = parent[a]
    while b != 0:
        if b in temp:
            return b
        b = parent[b]
    return 1 

def tree_size(root, children):
    num = 1
    if root in children:          
        for child in children[root]:
            num += tree_size(child, children)
    return num

T = int(input()) 
for test_case in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    nlist = list(map(int, input().split()))
    
    parent = [0] * (V + 1) 
    children = {}           
    
    for i in range(0, len(nlist), 2):
        p, c = nlist[i], nlist[i+1]
        # 자식 c의 부모 저장
        parent[c] = p
        if p not in children:
            # 리스트에 append하기 위해 빈리스트 먼저 만들어둠
            children[p] = []
        # 부모 p에 자식 c append
        children[p].append(c)
    
    res = lca(a, b, parent)
    size = tree_size(res, children)
    
    print(f"#{test_case} {res} {size}")
