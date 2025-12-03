# BOJ: 1924 2007년

x, y = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = 0
for i in range(x - 1):
    n += days[i]

n += y

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(week[n % 7])