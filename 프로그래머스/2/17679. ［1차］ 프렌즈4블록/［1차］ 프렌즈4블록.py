def solution(m, n, board):
    answer = 0
    # 보드를 리스트로 변환
    board = [list(row) for row in board]
    
    while True:
        # 지워질 블록 좌표를 저장할 집합
        removed = set()
        
        # 지워질 블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '.':
                    removed |= {(i, j), (i+1, j), (i, j+1), (i+1, j+1)}
        
        # 더 이상 지워질 블록이 없으면 종료
        if not removed:
            break
        
        # 지워질 블록을 '.'으로 표시하고 지워진 블록의 개수를 증가
        for i, j in removed:
            board[i][j] = '.'
            answer += 1
        
        # 블록을 아래로 떨어뜨리기
        for j in range(n):
            for i in range(m-1, -1, -1):
                if board[i][j] == '.':
                    for k in range(i-1, -1, -1):
                        if board[k][j] != '.':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
    
    return answer