from collections import deque


def solution(skill, skill_trees):
    count = 0
    if len(skill) == 1:
        return len(skill_trees)
    
    for order in skill_trees:

        #첫 스킬을 배울 수 있는 스킬트리에 등록
        ables = [skill[0]]
        
        #밑에 있는 스킬을 배운다면 윗 스킬트리에 등록, 그 전까지는 배울 경우 cnt를 올리지 않고 break로 탈출
        disables = deque(skill[1:])
        
        check = False
        
        for spell in order:
            if spell == ables[-1]:
                ables.append(disables.popleft())
                
                if not disables:
                    count += 1
                    break
                    
            elif spell in disables:
                break
            
            
        else:
            count += 1
                
    return count