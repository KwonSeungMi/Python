def solution(N, stages):
    answer = []
    dic = {}
    stage_count = len(stages)
    count_list = []

    # 아래 17 line에 count 함수를 쓰면 이중for문이 되기 때문에 n^2에서 2n이 되도록 다시 바꿔봤음!
    for i in range(0, N+2):
        count_list.append(0)
    print(count_list)

    for i in stages:
        count_list[i] += 1
    print(count_list)

    for i in range(1, N + 1):
        # count = stages.count(i)
        count = count_list[i]

        # 분모가 0일때 예외 처리 해줘야 함
        # 결과 = A if 조건 else B
        # 예시 dog if animal is dog else cat
        dic[i] = count / stage_count if stage_count else 0
        stage_count -= count

    # 리스트로 변환됨
    sort_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for i in range(0, len(sort_list)):
        answer.append(sort_list[i][0])

    return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
#
# N = 5
# stages =
# print(solution(N, stages))