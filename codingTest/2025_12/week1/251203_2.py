# BOJ: 11721 열 개씩 끊어 출력하기

line = input()

while len(line) >= 10:
    print(line[:10])
    line = line[10:]

if len(line) > 0:
    print(line)