def solution(num_list, n):
    #간격에 따라 담은 원소 리턴하기 예) 3이면 0,3,6...반환
    answer = []
    
    for idx,value in enumerate(num_list):
        if (idx==0 or idx%n==0):
            answer.append(value)
        
    return answer