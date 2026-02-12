#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N, M;
	cin >> N >> M;

	vector<string> board(N);

	for (int i = 0; i < N; ++i)
		cin >> board[i];

	vector<vector<int>>dp(N, vector<int>(M, -1));

	int sr = -1, sc = -1;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (board[i][j] == 'R') {
				sr = i;
				sc = j;
			}
		}
	}

	dp[sr][sc] = 0;


	for (int c = sc; c < M - 1; c++) {
		for (int r = 0; r < N; r++) {

			if (dp[r][c] == -1) continue;
			if (board[r][c] == '#') continue;

			for (int dr = -1; dr <= 1; dr++) {
				int nr = r + dr;
				int nc = c + 1;

				if (nr < 0 || nr >= N) continue;
				if (board[nr][nc] == '#') continue;

				int value = dp[r][c];
				if (board[nr][nc] == 'C') value++;

				dp[nr][nc] = max(dp[nr][nc], value);
			}
		}
	}

	int answer = -1;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (board[i][j] == 'O')
				answer = max(answer, dp[i][j]);

	cout << answer << "\n";

	return 0;
}