def solution(absolutes, signs):
    answer = 0
    #chk = False

    # for i in range(len(absolutes)):
    #     #chk = signs[i][0].upper() + signs[i][1:]
    #     if signs[i] == 'true':
    #         print("참")
    #         answer += absolutes[i]
    #     else:
    #         print("거짓")
    #         answer += -absolutes[i]

    # 모범답안에서 본 zip 함수
    # 여러 리스트를 인덱스 별로 묶어줌
    # 아래 print문 실행하면 이렇게 나옴
    # 4 true
    # 7 false
    # 12 true
    #
    for absolute, sign in zip(absolutes, signs):
        print(absolute, sign)
        if sign:
            answer += absolute
        else:
            answer -= absolute

    return answer



absolutes =[4,7,12]
signs = ['true','false','true']

print(solution(absolutes,signs))
