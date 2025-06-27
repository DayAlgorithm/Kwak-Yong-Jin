import sys
input = sys.stdin.readline
mod = 1000000007
def make_tree(node, left, right):
    if left == right:
        tree[node] = graph[left]
        return tree[node]

    mid = (left + right) // 2

    tree[node] = (make_tree(node * 2, left, mid) * make_tree(node * 2 + 1, mid + 1, right))%mod
    return tree[node]

def update(node, left, right, newIdx, newValue):
    if left == right:
        tree[node] = newValue
        return tree[node]
    
    mid = (left + right) // 2

    if left <= newIdx and newIdx <= mid:
        update(node * 2, left, mid, newIdx, newValue)
    else:
        update(node*2 + 1, mid + 1, right, newIdx, newValue)
    
    tree[node] = (tree[node*2] * tree[node * 2 + 1])%mod
    return tree[node]

def premulti(node, left, right, b, c):
    if c < left or right < b:
        return 1
    
    if b <= left and right <= c:
        return tree[node]

    mid = (left+right)//2
    return (premulti(node*2, left, mid, b, c) * premulti(node * 2 + 1, mid + 1, right, b, c))%mod

n, m, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]
tree = [0] * (4 * n)

make_tree(1, 0, n - 1)

for i in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 0, n - 1, b - 1, c)
    
    else:
        print(premulti(1, 0, n-1, b-1, c-1))
