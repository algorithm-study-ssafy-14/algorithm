#include <iostream>
#include <string>

using namespace std;

int solve(int N) {
	int num = 0, count = 0;

	while (true) {
		count++;

		int current_num = N * count;

		for (char digit : to_string(current_num))
			num |= (1 << (digit - '0'));

		if (num == (1 << 10) - 1)
			return current_num;
	}
}

int main(int argc, char** argv)
{
	int T, input;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> input;
		int result = solve(input);

		cout << "#" << i << " " << result << "\n";
	}
	return 0;