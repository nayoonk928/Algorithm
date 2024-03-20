def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    # DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]
    
    # 첫 번째 행과 열은 그대로 유지
    for i in range(n):
        dp[i][0] = board[i][0]
        answer = max(answer, dp[i][0])
    for j in range(m):
        dp[0][j] = board[0][j]
        answer = max(answer, dp[0][j])
    
    # DP 진행
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                # 현재 칸의 값이 1인 경우
                # 좌, 상, 좌상 대각선 방향의 값 중 최소값에 1을 더해 현재 칸의 값으로 설정
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                answer = max(answer, dp[i][j])
                
    # 최대 정사각형의 넓이 반환
    return answer ** 2