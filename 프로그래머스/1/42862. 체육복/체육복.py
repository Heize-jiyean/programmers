
def solution(n, lost, reserve):
    # 1. sorted 함수를 이용한 파이썬 오름차순 정리
    lost = sorted(lost)
    reserve = sorted(reserve)

    # 2. 중복을 확인하고 제거
    # 리스트끼리 뺄 수 있다
    lost_copy = lost[:]  # 중복 제거를 위해 원본 리스트를 복사
    reserve_copy = reserve[:]  # 중복 제거를 위해 원본 리스트를 복사
    for dup in lost_copy:
        for dups in reserve_copy:
            if dup == dups:
                lost.remove(dup)
                reserve.remove(dups)
                break  # 중복된 경우 한 번만 처리하고 루프를 빠져나옴
            
    # 3. 체육복 빌리기
    stolenfinal = []  # 체육복을 빌리는 학생의 정보를 담을 리스트
    for stolen in lost:
        front = stolen - 1
        back = stolen + 1

        if front in reserve:
            stolenfinal.append(front)  # 체육복을 빌리는 학생 추가
            reserve.remove(front)  # 빌린 학생의 여벌 체육복을 제거
        elif back in reserve:
            stolenfinal.append(back)  # 체육복을 빌리는 학생 추가
            reserve.remove(back)  # 빌린 학생의 여벌 체육복을 제거
            
    # 4. 체육수업을 들을 수 있는 학생 수 계산
    answer = n - len(lost) + len(stolenfinal)  # 전체 학생 수에서 체육복을 도난당한 학생 수를 빼고, 체육복을 빌린 학생 수를 더함
    
    return answer

 