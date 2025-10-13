def solution(lines):
    logs = []
    for line in lines:
        date, time, duration = line.split()
        h, m, s = time.split(':')
        end = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        duration = float(duration[:-1]) * 1000
        start = end - duration + 1 
        logs.append((start, end))

    max_count = 0
    for _, end_time in logs:
        start_window = end_time
        end_window = end_time + 999
        count = 0
        for s, e in logs:
            if s <= end_window and e >= start_window:
                count += 1
        max_count = max(max_count, count)

    return max_count
