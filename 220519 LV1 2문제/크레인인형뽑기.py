def solution(board, moves):
    answer = 0
    crane = []
    boards = list(map(list, zip(*board)))
    # 위에랑 같은 뜻 np.swapaxes(boards, 0, 1)

    # for move in moves:
    #   for j in range(len(board)):
    #       board[j][i-1] 이렇게 해도 됨 ㅠㅠㅠ 왜케 for문을 잘 못쓸까

    for move in moves:
        chk = 0
        if not boards[move-1]:
            continue

        while chk == 0:
            chk = boards[move-1].pop(0)

        # if len(crane) == 0:
        #     crane.append(chk)
        # else:
        #     if crane[-1] != chk:
        #         crane.append(chk)
        #     else:
        #         crane.pop()
        #         answer += 2
        print("crane :",crane)

        # 모범답안 보고 리팩토링
        crane.append(chk)
        if len(crane) > 1:
            if crane[-1] == crane[-2]:
                crane.pop(-1)
                crane.pop(-1)
                answer += 2

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))

