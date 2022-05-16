def distance(pt1,pt2):
    result = 0
    for i in range(len(pt1)):
        result += abs(pt1[i] - pt2[i])
    return result

def solution(numbers, hand):
    answer = ''
    dic = {1:'14', 2:'24', 3:'34', 4:'13', 5:'23', 6:'33', 7:'12', 8:'22', 9:'32', '*':'11', 0:'21', '#':'31'}
    left = '147'  # 왼손이 누를 수 있는 키패드
    right = '369' # 오른손이 누를 수 있는 키패드
    point = ['*', '#']  # 왼손 현재 위치 , 오른손 현재 위치

    for i in range(len(numbers)):
        if left.find(str(numbers[i])) != -1 : answer += 'L'

        elif right.find(str(numbers[i])) != -1 : answer += 'R'

        else:
            #왼손 거리
            l_dist = distance([int(dic[numbers[i]][0]),int(dic[numbers[i]][1])], [int(dic[point[0]][0]), int(dic[point[0]][1])])

            #오른손 거리
            r_dist = distance([int(dic[numbers[i]][0]), int(dic[numbers[i]][1])] , [int(dic[point[1]][0]),  int(dic[point[1]][1])])

            if(l_dist > r_dist) : answer += 'R'
            elif(l_dist < r_dist) : answer += 'L'
            else:
                 if hand == 'right' : answer += 'R'
                 else: answer += 'L'

        if answer[-1] == 'R': point[1] = numbers[i]
        else: point[0] = numbers[i]

    return answer



numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

#print(solution(numbers, hand))


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers, hand))