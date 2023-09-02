# 15:14 ~ 

# 시뮬, 구현느낌

# 플레이어수, 방의 정원숫자
P, M = map(int, input().split())

# init DS : 딕셔너리로하면 
_room = {}
_members = {}
room_idx = 1
for p in range(P):
    # 레벨, 닉네임
    l, n = input().split()
    l = int(l)

    # 매칭가능한 방이 없으면
    # 새로운 방 생성
    # 방 생성 & 방의 레벨 범위 저장 & 방이 생성된 시점 저장

    if len(_room) == 0:
        _room[room_idx] = [l-10, l+10]
        _members[room_idx] = [[l, n]]
    else:
        # 순회 : 매칭가능한 방 찾기 
        possible_room = []
        for i in range(1, len(_room)+1):
            # l과 방의 레벨 비교 & 정원이 남았는지
            if _room[i][0] <= l <= _room[i][1] and len(_members[i]) < M:
                possible_room.append(i)

        if len(possible_room) > 0:
            tmp = _members[possible_room[0]]
            tmp.append([l, n])
            _members[possible_room[0]] = tmp
        else: # 방 없으면 -> 새로 생성하기
            room_idx += 1
            _room[room_idx] = [l-10, l+10]
            _members[room_idx] = [[l, n]]

for i in range(1, room_idx + 1):
    if len(_members[i]) == M:
        print("Started!")
        _members[i].sort(key = lambda x:(x[1]))
        for j in range(len(_members[i])):
            print(_members[i][j][0], _members[i][j][1])
    else:
        print("Waiting!")
        _members[i].sort(key = lambda x:(x[1]))
        for j in range(len(_members[i])):
            print(_members[i][j][0], _members[i][j][1])

# 매칭가능한 방이 있다
    # 입장 후, 정원이 모두 찰 때까지 대기
# 입장가능한 방 여러개면
    # 먼저 생성된 방
# => 추가된 index자체가 먼저 생성된 방임. 
# Output
    # 최종적으로 만들어진 방의 상태, 플레이어들 출력

