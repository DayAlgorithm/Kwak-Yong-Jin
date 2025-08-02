import sys
input = sys.stdin.readline

def update(node, left, right, newIdx, newValue):
    if left == right:
        tree[node] += newValue
        return tree[node]

    mid = (left + right) // 2
    if newIdx <= mid:
        update(node * 2, left, mid, newIdx, newValue)
    else:
        update(node * 2 + 1, mid + 1, right, newIdx, newValue)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return tree[node]

def presum(node, left, right, b, c):
    if right < b or c < left:
        return 0

    if b <= left and right <= c:
        return tree[node]

    mid = (left + right) // 2
    return presum(node * 2, left, mid, b, c) + presum(node * 2 + 1, mid + 1, right, b, c)

n, q = map(int, input().split())
tree = [0] * (4 * n)

for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, n - 1, b - 1, c)

    else:
        print(presum(1, 0, n - 1, b - 1, c - 1))
