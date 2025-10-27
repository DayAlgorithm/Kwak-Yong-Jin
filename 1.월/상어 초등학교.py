import sys
input = sys.stdin.readline

n = int(input())
grid = [[0] * n for _ in range(n)]
favorites = {}
students_order = []

for _ in range(n * n):
    data = list(map(int, input().split()))
    student_id = data[0]
    fav_list = set(data[1:])
    
    students_order.append(student_id)
    favorites[student_id] = fav_list

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for student_id in students_order:
    best_criteria = (-1, -1, -n, -n) 
    best_seat_coords = (n, n) # (r, c)
    
    for r in range(n):
        for c in range(n):
            
            if grid[r][c] != 0:
                continue
                
            current_fav_count = 0
            current_empty_count = 0
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                if 0 <= nr < n and 0 <= nc < n:
                    neighbor_id = grid[nr][nc]
                    
                    if neighbor_id == 0:
                        current_empty_count += 1
                    elif neighbor_id in favorites[student_id]:
                        current_fav_count += 1
            
            current_criteria = (current_fav_count, current_empty_count, -r, -c)
            
            if current_criteria > best_criteria:
                best_criteria = current_criteria
                best_seat_coords = (r, c)

    final_r, final_c = best_seat_coords
    grid[final_r][final_c] = student_id
    
total_score = 0
score_map = [0, 1, 10, 100, 1000]

for r in range(n):
    for c in range(n):
        student_id = grid[r][c]
        student_favs = favorites[student_id]
        
        fav_neighbor_count = 0

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                neighbor_id = grid[nr][nc]
                if neighbor_id in student_favs:
                    fav_neighbor_count += 1

        total_score += score_map[fav_neighbor_count]

print(total_score)
