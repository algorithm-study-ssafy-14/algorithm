#include <bits/stdc++.h>

using namespace std;

vector<int> tree[100001];
int dp[100001];

void dfs(int u, int prev_node) {
    dp[u] = 1; // 본인

    for (int v : tree[u]) {
        if (v == prev_node) // 양방향 연결이므로 지나온 노드인지 확인
            continue;
        
        dfs(v, u);

        dp[u] += dp[v]; // dp[본인] += dp[자식 트리]
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, R, Q;
    cin >> N >> R >> Q;

    int a, b;
    for (int i = 0; i < N-1; ++i) { // 간선은 N-1 이므로
        cin >> a >> b;

        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    dfs(R, 0);

    int q;
    while (Q--) {
        cin >> q;
        cout << dp[q] << "\n";
    }
}
