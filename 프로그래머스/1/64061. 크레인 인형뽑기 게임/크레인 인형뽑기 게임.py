def solution(board, moves):
    
    stacks = [[] for _ in range(len(board[0]))]  # 보드의 열 수만큼 빈 스택을 생성
    for row in board:
        for idx, doll in enumerate(row):
            if doll != 0:
                stacks[idx].append(doll)  # 해당 열의 스택에 인형 추가
    
    basket = []  # 바스켓 스택
    answer = 0  # 카운트 변수
    
    for stacknumber in moves:
        if stacks[stacknumber-1]:  # 해당 위치의 스택이 비어있지 않은 경우
            doll = stacks[stacknumber-1].pop(0)  # 스택에서 인형 뽑기
            if basket and basket[-1] == doll: 
                # 바구니에 인형이 있고, 바구니 맨 위의 인형과 같은 경우
                basket.pop()  # 인형 제거
                answer += 2  # 점수 추가
            else:
                basket.append(doll)  # 인형을 바구니에 추가
    
    return answer