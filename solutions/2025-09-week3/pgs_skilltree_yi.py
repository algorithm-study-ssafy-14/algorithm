def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        tree = []
        for j in i:
            if j in skill:
                tree.append(j)
        flag = True
        for i in range(len(tree)):
            if tree[i] != skill[i]:
                flag = False
        if flag:
            answer += 1
    return answer
