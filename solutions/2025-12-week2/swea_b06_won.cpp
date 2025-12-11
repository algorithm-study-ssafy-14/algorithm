#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const int MOD = 1000000007;

// dp[day][mask] day번째 날에 참석자 집합이 mask일 때, 경우의 수
long long dp[10001][16];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        string managers;   // 각 날의 책임자 (A, B, C, D)
        cin >> managers;
        int N = managers.size();

        // dp 배열 초기화
        memset(dp, 0, sizeof(dp));

        // 1일차
        int firstManagerMask = 1 << (managers[0] - 'A'); // 첫째 날 책임자
        int A_MASK = 1 << 0;                             // a 는 1 << 0번, b 는 1 << 1, c 는 1 << 2, d 는 1 << 3

        for (int mask = 1; mask < 16; ++mask) {          // 0 은 아무도 안온거니까 안봄
            if ((mask & A_MASK) && (mask & firstManagerMask)) { // a 가 포함되고 책임자도 포함되어야함
                dp[0][mask] = 1;
            }
        }

        // 이후
        for (int day = 1; day < N; ++day) {
            int managerMask = 1 << (managers[day] - 'A');

            for (int prevMask = 1; prevMask < 16; ++prevMask) {
                long long eve = dp[day - 1][prevMask]; // 전날
                if (eve == 0) continue;                // 이전 날이 불가능한 경우는 패스

                for (int curMask = 1; curMask < 16; ++curMask) {
                    if ((curMask & managerMask) == 0) continue; // 오늘 책임자가 포함돼야함
                    if ((curMask & prevMask) == 0) continue;    // 전날과 오늘의 참여자가 겹쳐야함

                    dp[day][curMask] += eve;
                    if (dp[day][curMask] >= MOD) dp[day][curMask] %= MOD;
                }
            }
        }

        // 정답 계산
        long long ans = 0;
        for (int mask = 1; mask < 16; ++mask) {
            ans += dp[N - 1][mask];
            if (ans >= MOD) ans %= MOD;
        }

        cout << "#" << tc << " " << ans << '\n';
    }

    return 0;
}
