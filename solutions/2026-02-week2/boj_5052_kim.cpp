#include<bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t, n;
	cin >> t;

	while (t--) {
		cin >> n;
		vector<string>numbers(n);

		for (int i = 0; i < n; ++i)
			cin >> numbers[i];

		sort(numbers.begin(), numbers.end()); // 정렬

		bool ok = true;

		for (int i = 0; i < n - 1; ++i) {
			if (numbers[i + 1].substr(0, numbers[i].length()) == numbers[i]) { // 비교, 현재 번호의 길이만큼을 다음 번호의 0번째 부터 비교
				ok = false;
				break;
			}
		}

		cout << (ok ? "YES\n" : "NO\n");
	}

	return 0;
}
