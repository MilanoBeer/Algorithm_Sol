# 23.09.17 ~ / 16:00 ~ 

# 코스 : 4 ~ 12킬로미터
# 풀, 지면, 언덕, 평펴
# 성적 -> 팀의 점수

# 6명 한팀
# 팀점수 : 상위 4명 주자의 점수 sum
# 점수 -> 자격갖춘 팀 주자 / 결승점 통과순서

# Condition : 이 점수들을 더해서 가장 낮은 점수 얻는 팀이 우승
# 여섯명참가만 포함됨

from collections import Counter, defaultdict
import sys

T = int(input())

for t in range(T):
    N = int(input()) 
    _list = list(map(int, input().split()))

    # 전처리 : 6명이 되지 않는 팀의 등수점수는 안 쳐준다 
    # 1 : 6 / 2: 2 / 3 : 6 / 4 : 1
    # - 포함되지 않는 팀의 번호 알아내기 -> 해당 팀 false처리 
    
    max_team_num = max(_list)
    _tmp = Counter(_list)
    _outs = [0] * (max_team_num+1)

    for i in range(1, max_team_num+1):
        if _tmp[i] < 6:
            _outs[i] = 1

    cnt = 1
    _dd = defaultdict(int)
    # 각 팀에서 몇명까지 더했는지 카운트해야함
    _rank = defaultdict(int)
    _fif_rank = defaultdict(int)

    for i in range(len(_list)):
        if _outs[_list[i]] == 1:
            continue
        else:
            if _rank[_list[i]] < 4:
                _dd[_list[i]] += cnt
                _rank[_list[i]] += 1
                cnt += 1
            elif _rank[_list[i]] == 4:
                _fif_rank[_list[i]] = cnt
                _rank[_list[i]] += 1
                cnt += 1
            else:
                cnt += 1
    # _dd에 대해 정렬
    _dd = sorted(_dd.items(), key = lambda x:(x[1]))
    min_val = _dd[0][1]
    _result = [e[0] for e in _dd if e[1] == min_val]

    min_fif_val = sys.maxsize
    answer = 0
    for e in _result:
        if min_fif_val > _fif_rank[e]:
            answer = e
            min_fif_val = _fif_rank[e]
    print(answer)
    # DS : 팀마다 점수 저장하고 확인할 것 
    # _list 순회 
        # 팀이 false라면
            # continue
        # 팀이 true라면
            # 해당 팀 총점에 + cnt 
            # cnt + 1해주기 
    # 5번째 선수의 순서 고려하는 방법? 

    
    # 팀 렝크 가리기 
    

