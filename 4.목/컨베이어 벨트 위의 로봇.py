import sys
from collections import deque
input = sys.stdin.readline

def rotate_belt():
    belt.rotate(1)
    robots.rotate(1)
    robots[n-1] = False

def move_robots():
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
    
    robots[n-1] = False

def put_robot():
    if not robots[0] and belt[0] > 0:
        robots[0] = True
        belt[0] -= 1

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * (2 * n))

step = 0

while True:
    step += 1
    rotate_belt()
    move_robots()
    put_robot()
    cnt_zero = sum(1 for x in belt if x == 0)
    if cnt_zero >= k:
        break

print(step)
