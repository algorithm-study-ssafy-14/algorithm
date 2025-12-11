#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
using namespace std;

const int MAX_N = 300;

int N;
vector<string> board;               // 지뢰판      
int adj[MAX_N][MAX_N];              // 주변 칸의 지뢰 개수
bool vis[MAX_N][MAX_N];             // 방문한 칸

int dx[8] = { -1,-1,-1, 0, 0, 1, 1, 1 };
int dy[8] = { -1, 0, 1,-1, 1,-1, 0, 1 };

// 주변 칸을 여는 함수
void bfs(int sx, int sy) {
    queue<pair<int, int> > q;

    vis[sx][sy] = true;              // 시작칸 방문
    q.push(make_pair(sx, sy));       // 큐에 넣기

    while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        int x = cur.first;
        int y = cur.second;

        // 주변 칸 확인
        if (adj[x][y] == 0) {
            for (int dir = 0; dir < 8; ++dir) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (vis[nx][ny]) continue;
                if (board[nx][ny] == '*') continue;

                vis[nx][ny] = true;

                // 현재 칸이 0 이라면 큐에 넣음
                if (adj[nx][ny] == 0) {
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	for (int tc = 1; tc <= T; ++tc) {
		cin >> N;
        board.assign(N, "");

		for (int i = 0; i < N; ++i) {
			cin >> board[i];
		}

        memset(adj, 0, sizeof(adj));
        memset(vis, false, sizeof(vis));

        // 근처 지뢰 수 계산
        for (int x = 0; x < N; ++x) {
            for (int y = 0; y < N; ++y) {

                if (board[x][y] == '*') { // 현재 위치가 폭탄이라면
                    adj[x][y] = -1;
                    continue;
                }

                int cnt = 0;
                for (int dir = 0; dir < 8; ++dir) { // 아니라면
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                    if (board[nx][ny] == '*') cnt++;
                }
                adj[x][y] = cnt;
            }
        }

        int answer = 0;

        // 0 은 누르고 봄
        for (int x = 0; x < N; ++x) {
            for (int y = 0; y < N; ++y) {
                if (board[x][y] == '.' && !vis[x][y] && adj[x][y] == 0) {
                    answer++;       
                    bfs(x, y);
                }
            }
        }

        // 나머지는 0 이 아닌 숫자 칸이므로 1번씩 클릭
        for (int x = 0; x < N; ++x) {
            for (int y = 0; y < N; ++y) {
                if (board[x][y] == '.' && !vis[x][y]) {
                    answer++;
                }
            }
        }

        cout << "#" << tc << " " << answer << "\n";
	}

	return 0;
}
