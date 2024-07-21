'''import sys
sys.setrecursionlimit(10000) # 재귀 허용깊이 임의로 지정

def solution(k, room_number):
    rooms = dict() # {방번호: 바로 다음 빈방 번호}
    for num in room_number:
        chk_in = find_emptyroom(num,rooms)
    return list(rooms.keys())

def find_emptyroom(chk, rooms): # 재귀함수
    if chk not in rooms.keys(): # 빈 방이면
        rooms[chk] = chk+1 # rooms에 새 노드 추가
        return chk # 요청한 방
    empty = find_emptyroom(rooms[chk], rooms) # 재귀함수 호출
    rooms[chk] = empty+1 # (배정된 방+1)을 부모노드로 변경
    return empty # 새로 찾은 빈 방

k = 10
room_number = [1,3,4,1,3,1]
result = solution(k, room_number)
print(result)'''

from collections import defaultdict

def solution(k, room_number):
    answer = []
    roomDict = defaultdict()
    for num in room_number:
        index = num
        visit = {index}
        while index in roomDict:
            index = roomDict[index]
            visit.add(index)
        for room in visit:
            roomDict[room] = index + 1
        answer.append(index)
    return answer
k = 10
room_number = [1,3,4,1,3,1]
result = solution(k, room_number)
print(result)