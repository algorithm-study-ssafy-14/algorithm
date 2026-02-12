import sys
# sys.setrecursionlimit(10**6) # 필요시 재귀 깊이 설정 (N이 500만이므로 고려해야 함)
sys.stdin = open('input/1517_input.txt', 'r')
input = sys.stdin.readline

'''
[문제 해결 핵심]
1. 버블 소트의 Swap 횟수 = 배열의 Inversion 개수 (나보다 뒤에 있는 작은 숫자의 개수)
2. N이 최대 500,000이므로 O(N^2) 버블 소트는 시간 초과가 발생합니다.
   -> O(N log N)인 합병 정렬(Merge Sort)을 사용하여 해결해야 합니다.
3. Merge 과정에서 "뒤쪽 배열의 값이 앞쪽보다 작아서 앞으로 이동할 때",
   그 이동 거리만큼(왼쪽 배열에 남아있는 원소 개수) Swap이 발생했다고 간주합니다.
'''

def main(n, arr):
    global answer
    answer = 0
    # [중요] 원본 배열의 변형을 막기 위해 복사본 사용
    # arr[:] 슬라이싱은 새로운 리스트 객체를 생성하므로 원본 배열에 영향이 없습니다.
    # 함수 인자로 넘기는 것이 전역 변수보다 가독성, 재사용성 면에서 좋습니다.
    copy_arr = arr[:] 
    merge_sort(copy_arr, 0, n - 1)
    return answer

def merge_sort(arr, start, end):
    # [종료 조건] 리스트의 크기가 1 이하이면 더 이상 쪼갤 수 없습니다.
    if start >= end:
        return
    
    mid = (start + end) // 2
    
    # [분할] 절반으로 나누어 재귀 호출
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    
    # [정복 & 결합] 두 부분 리스트를 합치며 Swap 횟수 계산
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    global answer
    temp = []
    left = start
    right = mid + 1
    
    # 두 리스트(left ~ mid, right ~ end)를 비교하며 합침
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            # 왼쪽 값이 작거나 같으면 정상적인 순서 -> 그냥 넣음
            temp.append(arr[left])
            left += 1
        else:
            # [핵심] 오른쪽 값이 왼쪽 값보다 작음 -> 앞으로 이동해야 함!
            # 버블 소트에서 Swap이 발생하는 상황과 동일합니다.
            temp.append(arr[right])
            right += 1
            
            # [Swap 횟수 계산]
            # 왼쪽 리스트의 남은 원소들(mid - left + 1)은 모두 현재 오른쪽 값보다 큽니다.
            # 따라서 이 개수만큼 뒤로 밀려나야 하므로(또는 오른쪽 값이 앞으로 점프해야 하므로)
            # 그만큼을 Swap 횟수에 더해줍니다.
            answer += (mid - left + 1)
            
    # 남은 원소 처리
    if left <= mid:
        temp.extend(arr[left:mid + 1])
        
    if right <= end:
        temp.extend(arr[right:end + 1])
        
    # [반영] 정렬된 임시 리스트(temp)를 원본(복사본) 배열에 반영
    # 이 과정을 거치지 않으면 정렬된 결과가 유지되지 않습니다.
    for i in range(len(temp)):
        arr[start + i] = temp[i]

N = int(input())
A = list(map(int, input().split()))
print(main(N, A))
