#include<bits/stdc++.h>

using namespace std;

const int MAX = 1000000;

long long candyBox[MAX + 1]; // fenwick 트리

// i가 담당하는 구간 길이 구하기
int lowbit(int i) {
	int len = 1;
	while (i % (len * 2) == 0)
		len *= 2;
	return len;
}

// 값이 추가되면, 해당 idx 이후에도 추가해줘야함. 누적합이므로.
void updateBox(int idx, int num) {
	while (idx <= MAX) {
		candyBox[idx] += num;
		idx += lowbit(idx);
	}
}

// 누적합
long long prefix_sum(int idx) {
	long long sum = 0;

	while (idx > 0) {
		sum += candyBox[idx];
		idx -= lowbit(idx);
	}
	return sum;
}

int findCandy(int num) {
	int left = 1, right = MAX;
	int result = 0;

	while (left <= right) {
		int mid = (left + right) / 2;

		if (prefix_sum(mid) >= num) {
			result = mid;
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}

	return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	while (n--) {
		int a;
		cin >> a;

		if (a == 1) {
			long long b;
			cin >> b;

			int candy = findCandy(b);
			cout << candy << "\n";

			updateBox(candy, -1);
		}
		else {
			int b, c;
			cin >> b >> c;
			updateBox(b, c);
		}
	}

	return 0;
}