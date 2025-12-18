#include <bits/stdc++.h>
using namespace std;

static const int dx[4] = { -1, 1, 0, 0 };
static const int dy[4] = { 0, 0, -1, 1 };

int N;
int board[12][12];
vector<pair<int, int>> cores; // 테두리 제외 코어들

int bestConnected, bestLen;

// 둘 수 있는지
bool canLay(int x, int y, int dir, int& len) {
    int nx = x + dx[dir], ny = y + dy[dir];
    len = 0;

    // 테두리까지 못가면 불가능
    while (0 <= nx && nx < N && 0 <= ny && ny < N) {
        if (board[nx][ny] != 0) return false; 
        nx += dx[dir];
        ny += dy[dir];
    }

    // 테두리 밖으로 나갈 수 있으면 끝까지 갈 수 있는 거임
    nx = x + dx[dir], ny = y + dy[dir];
    while (0 <= nx && nx < N && 0 <= ny && ny < N) {
        len++;
        nx += dx[dir];
        ny += dy[dir];
    }
    return true;
}

// 전선 놓기
void setWire(int x, int y, int dir, int val) {
    int nx = x + dx[dir], ny = y + dy[dir];
    while (0 <= nx && nx < N && 0 <= ny && ny < N) {
        board[nx][ny] = val;
        nx += dx[dir];
        ny += dy[dir];
    }
}

void dfs(int idx, int connected, int length) {
    int remain = (int)cores.size() - idx;

    // 최대 연결 수 갱신 못하면 return
    if (connected + remain < bestConnected) return;

    // 연결 수 같을 때 길이 최소화 못하면 return
    if (connected + remain == bestConnected && length >= bestLen) return;

    // 마지막 idx
    if (idx == (int)cores.size()) {
        // 갱신
        if (connected > bestConnected) {
            bestConnected = connected;
            bestLen = length;
        }
        else if (connected == bestConnected) {
            bestLen = min(bestLen, length);
        }
        return;
    }

    int x = cores[idx].first;
    int y = cores[idx].second;

    // 4방향 시도
    for (int d = 0; d < 4; d++) {
        int wlen = 0;
        if (!canLay(x, y, d, wlen)) continue;

        setWire(x, y, d, 2);
        dfs(idx + 1, connected + 1, length + wlen);
        setWire(x, y, d, 0);
    }

    // 연결을 일부러 안하는 경우
    // 어떤 코어는 일부러 연결하지 않아야 코어들을 더 많거나 짧게 연결할 수 있음
    dfs(idx + 1, connected, length);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cin >> N;
        cores.clear();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> board[i][j];
            }
        }

        // 테두리 제외 코어 찾기
        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < N - 1; j++) {
                if (board[i][j] == 1) cores.push_back({ i, j });
            }
        }

        bestConnected = -1;
        bestLen = INT_MAX;

        dfs(0, 0, 0);

        cout << "#" << tc << " " << bestLen << "\n";
    }
    return 0;
}
