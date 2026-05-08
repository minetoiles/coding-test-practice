# BOJ 1018 체스판 다시 칠하기
# 코드 다시 보고 이해하기

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

check = ['WBWBWBWB', 'BWBWBWBW']
min_cnt = 64
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for l in range(8):
                if (board[i+k][j+l] != check[k%2][l]):
                    cnt1 += 1
                if (board[i+k][j+l] != check[(k+1)%2][l]):
                    cnt2 += 1
        min_cnt = min(min_cnt, cnt1, cnt2)
print(min_cnt)