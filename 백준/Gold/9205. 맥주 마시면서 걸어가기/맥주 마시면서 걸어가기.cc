#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std; 

// bfs - deque 구현방법
// import queue / 선언 방법 / 추가방법
#include <queue>

// struct
struct point
{
    int x; 
    int y; 
}; 

// global 
bool visited[100] = {false, }; 
point pHome;
point pEnd;
point peon[100]; 
int macju = 20 * 50; 

// 절댓값 계산 함수 구현하기
int abs(int val) {
    if (val < 0)
        return -val ; 
    return val;  
}

void dfs(int N)
{
    queue<pair<int, int>> dq; 
    dq.push({pHome.x, pHome.y}); 

    while (!dq.empty()) {
        int x = dq.front().first; 
        int y = dq.front().second; 
        dq.pop(); 

        if (abs(x - pEnd.x) + abs(y - pEnd.y) <= macju){
            cout << "happy" << endl; 
            return; 
        }

        for(int i = 0; i < N; i ++) {
            if (visited[i] == false) {
                if (abs(x - peon[i].x) + abs(y - peon[i].y) <= macju){
                    visited[i] = true; 
                    dq.push({peon[i].x, peon[i].y}); 
                }
            }
        }     
    }
    cout << "sad" << endl; 
}

int main() {

    // init
    // ios_base::sync_with_studio(0); 
    cout.tie(0), cin.tie(0); 

    int T, n; 
    cin >> T; 

    for(int i = 0; i < T; i ++) {
        cin >> n; 

        cin >> pHome.x >> pHome.y; 

        for(int i = 0; i < n; i ++) {
            cin >> peon[i].x >> peon[i].y; 
        }

        cin >> pEnd.x >> pEnd.y; 

        dfs(n);

        // bool visited[100] = {false, }; 
        // fill(visited, visited.size(), false);
        // 초기화
        memset(visited, 0, sizeof(visited));
    }

}