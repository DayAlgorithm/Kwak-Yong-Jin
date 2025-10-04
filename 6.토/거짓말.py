import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
truth_info = list(map(int, input().split()))
knows_truth = truth_info[1:]

parties = []
for _ in range(m):
    party_info = list(map(int, input().split()))
    parties.append(party_info[1:])

parent = [i for i in range(n + 1)]

for party in parties:
    if len(party) > 1:
        first_person = party[0]
        for i in range(1, len(party)):
            union_parent(parent, first_person, party[i])

truth_groups = set()
for person in knows_truth:
    truth_groups.add(find_parent(parent, person))

lie_party_count = 0
for party in parties:
    can_lie = True
    for person in party:
        if find_parent(parent, person) in truth_groups:
            can_lie = False
            break
    if can_lie:
        lie_party_count += 1

print(lie_party_count)
