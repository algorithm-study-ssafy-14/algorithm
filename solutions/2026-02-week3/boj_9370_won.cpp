#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;

int n, m, t;
vector<pair<int, int>> graph[2001];

vector<int> dijkstra(int start) {
	vector<int> d(n + 1, INF);
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

	d[start] = 0;
	pq.push({ 0, start });

	while (!pq.empty()) {
		int cw = pq.top().first;
		int cv = pq.top().second;

		pq.pop();

		if (d[cv] != cw)
			continue;

		for (int i = 0; i < graph[cv].size(); ++i) {
			int nv = graph[cv][i].first;
			int nw = graph[cv][i].second;

			if (d[nv] <= cw + nw)
				continue;

			d[nv] = cw + nw;
			pq.push({ d[nv], nv });
		}
	}
	return d;
}

void solve() {
    int s, g, h;
    cin >> n >> m >> t;
    cin >> s >> g >> h;

    for (int i = 1; i <= n; i++) {
        graph[i].clear();
    }

    int gh_dist = 0; // g와 h 사이의 거리를 저장할 변수

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;

        graph[u].push_back({ v, w });
        graph[v].push_back({ u, w });

        // g와 h를 연결하는 간선의 가중치 저장
        if ((u == g && v == h) || (u == h && v == g)) {
            gh_dist = w;
        }
    }

    // 목적지 후보
    vector<int> candidates(t);
    for (int i = 0; i < t; i++) {
        cin >> candidates[i];
    }

    sort(candidates.begin(), candidates.end());

    // s, g, h 각각에서 다익스트라 3번 실행
    vector<int> dist_s = dijkstra(s);
    vector<int> dist_g = dijkstra(g);
    vector<int> dist_h = dijkstra(h);

    // 목적지 후보 판별 및 출력
    for (int i = 0; i < t; i++) {
        int dest = candidates[i];

        // 도달 불가능한 경우는 패스
        if (dist_s[dest] == INF) continue;

        // s -> g -> h -> dest 경로의 길이
        int path1 = dist_s[g] + gh_dist + dist_h[dest];
        // s -> h -> g -> dest 경로의 길이
        int path2 = dist_s[h] + gh_dist + dist_g[dest];

        // 원래 s에서 dest로 가는 최단 거리가 path1 또는 path2와 같다면
        // 그 경로는 g-h 도로를 반드시 지나가는 최단 경로임
        if (dist_s[dest] == path1 || dist_s[dest] == path2) {
            cout << dest << " ";
        }
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test_case;
    cin >> test_case;

    while (test_case--) {
        solve();
    }

    return 0;
}