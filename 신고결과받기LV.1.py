# def solution(id_list, report, k):
#     answer = []
#
#     # 1. report로 누가 누굴 신고했는지 카운팅해서 id_list랑 매핑해서 저장
#     #    이 때, 동일한 사람을 여러번 신고한 경우는 카운팅에서 제외됨
#
#     # 딕셔너리 선언
#     rpt_dic = {} #신고 당한 횟수 기록
#     id_dic = {} #동일한 사람 여러번 신고한 경우 거르기 위한 dic
#     id_list_count = {} # 결과
#
#
#     # print("input ID List : ",id_list)
#     # print("input Report : ",report)
#     for i in report:
#         rpt_list = []
#         tmp = i.split(" ")
#         tmp0 = tmp[0]
#         tmp1 = tmp[1]
#         # print(tmp)
#
#         # print(tmp1 in rpt_dic)
#         # if 여러번 신고하면
#         if tmp0 in id_dic:
#             # print(id_dic[tmp0])
#             # print(rpt_list)
#             if tmp1 in id_dic[tmp0]:
#                 # print("aaaaa",tmp1)
#                 continue
#
#             rpt_list = id_dic[tmp0]
#             rpt_list.append(tmp1)
#             id_dic[tmp0] = rpt_list
#             # print(rpt_list)
#             # print(tmp0, "는 한명 이상 신고 했고, 여태까지 신고한 사람 : ", id_dic.get(tmp0),", 또 신고 할 사람 : ", tmp1)
#
#
#         else:
#             rpt_list.append(tmp1)
#             # print("rpt_list: ", rpt_list)
#             id_dic[tmp0] = rpt_list
#             # print(id_dic[tmp0])
#             # print(tmp0, "가 처음으로 신고 한 id : ", id_dic.get(tmp0))
#
#         # print("id dic : ",id_dic)
#
#         if tmp1 in rpt_dic:
#              rpt_dic[tmp1] = rpt_dic.get(tmp1) + 1
#         else:
#             rpt_dic[tmp1] = 1
#
#     print("rpt_dic : " ,rpt_dic)
#     for i in rpt_dic:
#         if rpt_dic[i] >= k: #k번 이상 신고당한 유저
#             # print("k번 이상 신고당한 유저 :",i)
#
#             for key in id_dic:
#                 # print(key,"가 신고한 리스트 :",id_dic[key])
#                 # if key == i:
#                 # print(i, "를 신고 한 유저 : ", key)
#                 # print("id_list_count : ", id_list_count)
#
#                 if i in id_dic[key]:
#                     if key in id_list_count:
#                         id_list_count[key] = id_list_count[key] + 1
#                     else:
#                         id_list_count[key] = 1
#                     print("aaaa id_list_count : ", id_list_count)
#
#     for i in id_list:
#         if i in id_list_count:
#             answer.append(id_list_count[i])
#         else:
#             answer.append(0)
#
#     # 2. id_list를 가져와서 K번보다 많이 신고된 사람을 찾기
#
#     # 3. K번보다 많이 신고된 사람을 신고한 사람 찾기
#
#
#     return answer
#
#
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
#
# print(solution(id_list,report,k))
#
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
#
# print(solution(id_list,report,k))
#

# 모범답안
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
        print(reports)

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list,report,k))

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list,report,k))
