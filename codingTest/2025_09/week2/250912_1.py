# BOJ: 13458 시험 감독

N = int(input()) # 시험장 개수
tester = list(map(int, input().split()))
A, B = map(int, input().split()) # 총감독 감시자수, 부감독 감시자수

answer = N
for i in range(N):
    if tester[i] - A > 0:
        if (tester[i]-A) % B == 0:
            answer += (tester[i]-A) // B

        else:
            answer += (tester[i]-A) // B + 1

print(answer)