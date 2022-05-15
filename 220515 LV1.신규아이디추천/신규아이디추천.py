# import re
# def dotRemove(answer):
#     if (len(answer) != 0 and answer[0] == '.'):
#         answer = answer[1:]
#     if (len(answer) != 0 and answer[-1] == '.'):
#         answer = answer[:-1]
#     return answer
#
#
# def solution(new_id):
#     answer = ''
#
#     # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
#     answer = new_id.lower()
#     #print("1단계 : " , answer)
#
#     # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
#
#     answer = re.sub('[^\w.-]',"",answer)
#     #print("2단계 : ",answer)
#
#     # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#     answer = re.sub('\.{2,}', ".", answer)
#     #print("3단계 : ", answer)
#
#     # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다
#     answer = dotRemove(answer)
#     #print("4단계 : ", answer)
#
#     # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#     if(len(answer) >= 16):
#         answer = answer[:15]
#     #print("6단계 : ", answer)
#
#     #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
#     answer = dotRemove(answer)
#
#     # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
#     if (answer == ""):
#         answer = "a"
#     #print("5단계 : ", answer)
#
#     # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
#     if(len(answer) <= 2 ):
#         answer = answer.ljust(3,answer[-1])
#
#     #print("7단계 : ", answer)
#
#     return answer
#
# print("1번 : " , solution("...!@BaT#*..y.abcdefghijklm_-" ),"답 : bat.y.abcdefghi")
# print("2번 : " , solution("z-+.^."),"답 : z--")
# print("3번 : " , solution("=.="),"답 : aaa")
# print("4번 : " , solution("123_.def"),"답 : 123_.def")
# print("5번 : " , solution("abcdefghijklmn.p"),"답 : abcdefghijklmn")
#

# 모범답안
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st