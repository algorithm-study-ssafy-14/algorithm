# 사탕상자

import sys

input = sys.stdin.readline

n = int(input())

ans_arr = []
seg_tree = [0]* 2048577 #(1024 ^ 2 + 1000001)
for i in range(n):
    input_list = list(map(int, input().split()))

    #세그트리에서 꺼내기
    if input_list[0] == 1:
        sequence = input_list[1] - 1
        node = 1
        while node < 1048576:
            if sequence < seg_tree[node]:
                seg_tree[node] -= 1
                node *= 2

            else:
                sequence -= seg_tree[node]
                seg_tree[node+1] -= 1
                node = (node+1) * 2

        else:
            if sequence < seg_tree[node]:
                seg_tree[node] -= 1
                print(node+-1048576)#1-1048576-2)

            else:
                seg_tree[node+1] -= 1
                print(node-1048575)#1048576+1)

    #세그트리에 집어넣기.
    else:

        node = input_list[1] + 1048576
        cnt = input_list[2]
        while node:
            seg_tree[node] += cnt
            node //= 2

