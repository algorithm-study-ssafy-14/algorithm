#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    map<int, pair<int, int>> info; // 정보 저장용, solved 계산용
    set<pair<int, int>> problems; // 문제 저장용
    map<int, set<pair<int, int>>> forG; // G 계산용

    int P, L, G;
    for (int i = 0; i < N; ++i) {
        cin >> P >> L >> G;
        info[P] = {L, G};
        problems.insert({L, P});
        forG[G].insert({L, P});
    }

    int M;
    cin >> M;
    
    while (M--) {
        string cmd;
        cin >> cmd;

        if (cmd == "add") {
            int P, L, G;
            cin >> P >> L >> G;
            info[P] = {L, G};
            problems.insert({L, P});
            forG[G].insert({L, P});
        }

        else if (cmd == "solved") {
            int P;
            cin >> P;
            
            auto [L, G] = info[P];
            problems.erase({L, P});
            forG[G].erase({L, P});
            info.erase(P);
        }
        else if (cmd == "recommend") {
            int G, x;
            cin >> G >> x;

            if (x == 1) cout << forG[G].rbegin()->second << endl;
            else cout << forG[G].begin()->second << endl;
        }
        else if (cmd == "recommend2") {
            int x;
            cin >> x;

            if (x == 1) cout << problems.rbegin()->second << endl;
            else cout << problems.begin()->second << endl;
        }
        else if (cmd == "recommend3") {
            int x, L;
            cin >> x >> L;
            
            if (x == 1) {
                auto it = problems.lower_bound({L, 0}); // L 보다 작은 문제 중 가장 앞의 값
                if (it == problems.end()) // iterator 가 problems.end 이면 조건을 만족하는 원소가 없다는 뜻, 
                    cout << -1 << endl;   // end() 는 마지막 원소 다음 위치라서 실제 데이터가 아님

                else 
                    cout << it->second << "\n";
            } 
            else {
                auto it = problems.lower_bound({L, 0});
                if (it == problems.begin()) 
                    cout << -1 << endl;  
                else {
                    --it;
                    cout << it->second << "\n";
                }
            }
        }
    }

    return 0;
}