#include <iostream>
#include <string>
#include <bitset>

using namespace std;

int main()
{
	int T, N, M;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> N >> M;

		int mask = (1 << N) - 1;

		if ((M & mask) == mask)
			cout << "#" << i << " " << "ON" << "\n";
		else
			cout << "#" << i << " " << "OFF" << "\n";

	}
	return 0;
}
