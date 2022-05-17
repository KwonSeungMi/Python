def solution(s):
    answer = ''
    dic = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4',
           "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    dic_num = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four",
           '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}

    find_num = s[0];

    for i in range(1 , len(s) ):
        # s[i]가 숫자인 경우
        if dic_num.get(find_num, "NONE") != "NONE":
            answer += s[i-1]
            find_num = s[i]
        # s[i]가 영어인 경우
        elif  dic.get(find_num,"NONE") == "NONE":
            find_num += s[i]
        else:
            answer += dic.get(find_num)
            find_num = s[i]

    # s[i]가 숫자인 경우
    if dic_num.get(find_num, "NONE") != "NONE":
        answer += s[-1]
    # s[i]가 영어인 경우
    else:
        answer += dic.get(find_num)


    return int(answer)




print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("123"))