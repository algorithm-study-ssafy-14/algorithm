#include <bits/stdc++.h>

using namespace std;

vector<int> parent;

int findParent(int x) {
	if (parent[x] == x)
		return x;
	return parent[x] = findParent(parent[x]);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N, M, K;

	cin >> N >> M >> K;

	vector<int> cards(M);
	for (int i = 0; i < M; ++i)
		cin >> cards[i];

	// 민수가 들고 있는 카드 뭉치 정렬
	sort(cards.begin(), cards.end());

	// 유니온파인드를 위한 parent 초기화
	parent.resize(M + 1);

	for (int i = 0; i < M; ++i)
		parent[i] = i;

	for (int i = 0; i < K; ++i) {
		int chulsu;
		cin >> chulsu;

		// upper_bound 는 iterator 를 반환, - cards.begin() 으로 인덱스로 전환
		int idx = upper_bound(cards.begin(), cards.end(), chulsu) - cards.begin();

		idx = findParent(idx);

		cout << cards[idx] << "\n";

		parent[idx] = findParent(idx + 1);
	}


	return 0;
}