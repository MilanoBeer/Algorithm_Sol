# Problem_Def
    # 하나의 vertex -> all vertex에 대해, 최소한의 비용으로 이동하는 방법 & 과정을 출력

# Condtion 
    # 다익스트라 or 벨만포드를 통해 구현 가능
    # 다익스트라는 양의 input만 가능 / 벨만포드는 음수의 input도 가능 

# Input
    # vertex 수 
    # edge 가중치 mat형태 
    # edge  x -> 999
    # 5 <= n <= 20 / 0 < 비용 < 100

    # Test >
    # 6
    # 0 2 4 999 999 999
    # 999 0 1 4 2 999
    # 999 999 0 999 3 999
    # 999 999 999 0 999 2
    # 999 999 999 3 0 2
    # 999 999 999 999 999 0

INF = 999

V = int(input())
mat = [list(map(int, input().split())) for _ in range(V)]
dist = [INF] * V
selected_v = [False] * V
val_list = [INF] * V

def find_shortest_vertext():
    min_dist_vertex = 0

    # 방문하지 않은 vertex 찾기 
    for i in range(V):
        if selected_v[i] == False:
            min_dist_vertex = i
            break 
    # 더 짧은 정점이 있는지 확인하기
    for i in range(min_dist_vertex + 1, V):
        if dist[i] < dist[min_dist_vertex] and selected_v[i] == False:
            min_dist_vertex = i
    
    return min_dist_vertex

def dijkstra(start_vertex):
    cnt = 0
    selected_v[start_vertex] = True

    # dist 초기화 # 출발(1번)노드에서 다른 모든 노드들로의 거리정보를 업데이트 
    dist[start_vertex] = 0
    selected_v[start_vertex] = True

    # @@ O(Vertex 갯수 ) 
    for i in range(V):
        if mat[start_vertex][i] != INF:
            dist[i] = mat[start_vertex][i]
    
    # 모든 노드를 방문할 떄까지 반복 
    # @@ O(Vertex)
    for i in range(V-1):
        # 방문하지 않은 노드들 중, 최단 거리에 있는 노드를 선택 
                # <<< O(Vertex) >>>
        vertex = find_shortest_vertext()

        selected_v[vertex] = True
        val_list[vertex] = dist[vertex]
        cnt += 1

        # Do > print status
        # <<< O(Vertex) >>>
        print(cnt, " : ", end=' ')
        for v in range(1, V):
            print(val_list[v], end= ' ')
        print()

        # 선택된 노드를 바탕으로, 거리정보(dist)를 갱신 
        # <<< O(Vertex) >>>
        for w in range(V):
            if selected_v[w] == False: 
                dist[w] = min(dist[w], dist[vertex] + mat[vertex][w])

# Time Complexity
    # O(Vertex)
    # O( Vertex ( 3*O(Vertex) ))
    # O(3Vertex*Vertex + Vertex)
    # => O(Vertex*Vertex)

dijkstra(0) # 1번
print("dist : ", end='')
print(*dist)