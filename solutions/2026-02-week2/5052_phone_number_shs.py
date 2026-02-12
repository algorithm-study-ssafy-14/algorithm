import sys
sys.stdin = open("input/5052_input.txt", 'r')
input = sys.stdin.readline
# [중요] 대량의 데이터 입력 시 input()보다 sys.stdin.readline()이 훨씬 빠릅니다.

def main(Phone_numbers):
    # [핵심 로직]
    # 전화번호 리스트를 정렬했기 때문에, 접두어 관계가 형성된다면 반드시 "인접한 두 번호" 사이에서 발생합니다.
    # 예: ['123', '1234', '789'] -> '123' 바로 뒤에 '1234'가 위치함.
    # 따라서 모든 번호를 비교할 필요 없이(O(N^2)), 인접한 번호들만 비교하면 됩니다(O(N)).
    for i in range(len(Phone_numbers) - 1):
        # [주의] 정렬을 하면 짧은 문자열이 앞에 옵니다. (예: "123", "12345")
        # 따라서 항상 뒷 번호(i+1)가 앞 번호(i)로 시작하는지 검사해야 합니다.
        if Phone_numbers[i+1].startswith(Phone_numbers[i]):
            return 'NO'

    return 'YES'


T = int(input())
answer = []
for test_case in range(1, T + 1):
    N = int(input())
    
    # [주의] 입력받을 때 공백 제거(.strip())가 필수입니다.
    # 개행 문자(\n)가 포함되어 있으면 접두어 비교나 정렬 순서에 영향을 줄 수 있습니다.
    Phone_numbers = [input().strip() for _ in range(N)]
    
    # [필수] 정렬을 해야 인접 비교 로직이 성립합니다.
    # 문자열 정렬: 사전 순 (Lexicographical Order)
    # "911" < "91125" < "976" 순서로 정렬됨
    Phone_numbers.sort()

    answer.append(main(Phone_numbers))
    
print('\n'.join(answer))
