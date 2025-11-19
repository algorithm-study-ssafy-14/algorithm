class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.head = ListNode(data)

    def append(self, data):
        if self.head is None:
            self.head = ListNode(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(data)

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            if node is None:
                return None
            cnt += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index - 1)
        new_node.next = node.next
        node.next = new_node

    def del_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev = self.get_node(index - 1)
        prev.next = prev.next.next

    def to_list_10(self):
        res = []
        cur = self.head
        for _ in range(10):
            if cur is None:
                break
            res.append(cur.data)
            cur = cur.next
        return res


T = 10
for tc in range(1, T + 1):
    n = int(input())
    code = list(map(int, input().split()))

    ans_list = LinkedList()
    for x in code:
        ans_list.append(x)

    s = int(input())
    cmds = input().split()
    i = 0

    while i < len(cmds):
        cmd = cmds[i]

        if cmd == 'I':
            x = int(cmds[i + 1])
            y = int(cmds[i + 2])
            values = list(map(int, cmds[i + 3: i + 3 + y]))
            for v in reversed(values):
                ans_list.add_node(x, v)
            i += 3 + y

        elif cmd == 'D':
            x = int(cmds[i + 1])
            y = int(cmds[i + 2])
            for _ in range(y):
                ans_list.del_node(x)
            i += 3

        elif cmd == 'A':
            y = int(cmds[i + 1])
            values = list(map(int, cmds[i + 2: i + 2 + y]))
            for v in values:
                ans_list.append(v)
            i += 2 + y

    print(f"#{tc}", *ans_list.to_list_10())

# ======================================================= #

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    M = int(input())
    cmds = input().split()

    idx = 0
    while idx < len(cmds):
        cmd = cmds[idx]

        if cmd == 'I':
            x = int(cmds[idx + 1])
            y = int(cmds[idx + 2])
            values = list(map(int, cmds[idx + 3: idx + 3 + y]))
            arr[x:x] = values
            idx += 3 + y

        elif cmd == 'D':
            x = int(cmds[idx + 1])
            y = int(cmds[idx + 2])
            arr[x:x + y] = []
            idx += 3

        elif cmd == 'A':
            y = int(cmds[idx + 1])
            values = list(map(int, cmds[idx + 2: idx + 2 + y]))
            arr.extend(values)
            idx += 2 + y

    print(f"#{tc}", *arr[:10])
