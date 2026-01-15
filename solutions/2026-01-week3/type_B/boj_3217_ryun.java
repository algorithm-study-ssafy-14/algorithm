import java.io.*;
import java.util.*;

public class Main {

    // 메모리 공간 크기(1 ~ MAX)를 1차원 배열처럼 취급
    static final int MAX = 100000;

    // 변수 이름이 a~z 4글자라고 가정하면 경우의 수는 26^4
    // 각 변수를 "정수 id"로 매핑해서 배열로 관리
    static final int VAR_MAX = 26 * 26 * 26 * 26;

    // varStart[id] = 해당 변수가 가리키는 메모리 시작 주소(1-based), 없으면 0
    static int[] varStart = new int[VAR_MAX];
    // varLen[id] = 할당된 길이(크기), 없으면 0
    static int[] varLen = new int[VAR_MAX];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int N = Integer.parseInt(br.readLine().trim());

        // 세그먼트 트리: 구간의 "연속된 빈칸" 정보를 빠르게 관리하기 위한 자료구조
        // 초기에는 전체가 free(1) 상태
        SegTree st = new SegTree(MAX);

        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();

            /*
             * 명령 종류:
             * 1) xxxx=malloc(k);
             * 2) free(xxxx);
             * 3) print(xxxx);
             *
             * 문자열 위치로 빠르게 판별:
             * - "xxxx=..." 이면 line.charAt(4) == '='
             * - "free(" 이면 line.charAt(4) == '('  (f r e e ( => index 4가 '(')
             * - "print(" 는 위 둘에 해당 안 하므로 else
             */
            if (line.charAt(4) == '=') {
                // malloc: 왼쪽 변수명 4글자(0~3)를 id로
                int id = varId(line, 0);

                // malloc 괄호 안 숫자 파싱
                int size = parseSize(line);

                // 세그먼트 트리에서 "size만큼 연속 free"인 가장 왼쪽 시작 위치 찾기
                int pos = st.allocatePos(size);

                // 0이면 할당 불가(연속 공간 없음)
                if (pos == 0) {
                    varStart[id] = 0;
                    varLen[id] = 0;
                } else {
                    // [pos, pos+size-1] 구간을 occupied(0)으로 만들기
                    st.update(pos, pos + size - 1, 0);

                    // 변수에 시작 주소/길이 저장
                    varStart[id] = pos;
                    varLen[id] = size;
                }

            } else if (line.charAt(4) == '(') { // free(var);
                // "free(" 다음에 변수 4글자가 온다고 가정
                // f r e e ( => index 5부터 변수명 시작
                int id = varId(line, 5);

                int s = varStart[id];
                int len = varLen[id];

                // 할당된 적이 있으면(시작 주소 0이 아니면) 반납 처리
                if (s != 0) {
                    // [s, s+len-1] 구간을 free(1)로 만들기
                    st.update(s, s + len - 1, 1);

                    // 변수 상태 초기화
                    varStart[id] = 0;
                    varLen[id] = 0;
                }

            } else { // print(var);
                // "print(" 다음에 변수 4글자: p r i n t ( => index 6부터 변수명 시작
                int id = varId(line, 6);

                // 시작 주소 출력(없으면 0)
                out.append(varStart[id]).append('\n');
            }
        }

        System.out.print(out.toString());
    }

    /*
     * 세그먼트 트리 노드가 들고 있어야 하는 값:
     * - pref[node] : 해당 구간의 "왼쪽부터 연속 free 길이"
     * - suf[node]  : 해당 구간의 "오른쪽부터 연속 free 길이"
     * - best[node] : 해당 구간 내부에서 가능한 "최대 연속 free 길이"
     * - lazy[node] : 구간 통째로 덮어쓰기(0=occupied, 1=free)를 미루는 lazy propagation
     *
     * 이 3개(pref/suf/best)만 있으면,
     * "need만큼 연속으로 비어있는 구간이 존재하는가?"를 best로 O(1)에 판단하고,
     * "가장 왼쪽 시작 위치"도 트리 내려가며 O(log N)에 찾을 수 있음.
     */
    static class SegTree {
        int n;
        int[] pref, suf, best, lazy; // lazy: -1(없음), 0(occupied), 1(free)

        SegTree(int n) {
            this.n = n;
            int sz = 4 * n + 5;
            pref = new int[sz];
            suf  = new int[sz];
            best = new int[sz];
            lazy = new int[sz];
            Arrays.fill(lazy, -1);

            // 초기 상태: 전체가 free(1)
            build(1, 1, n);
        }

        // 트리 초기화: 모든 칸이 free이므로 각 구간의 pref/suf/best = 구간 길이
        void build(int node, int l, int r) {
            int len = r - l + 1;
            pref[node] = suf[node] = best[node] = len;
            if (l == r) return;
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid);
            build(node << 1 | 1, mid + 1, r);
        }

        // 현재 노드 구간 [l,r]을 val(0/1)로 "통째로" 덮어쓸 때 노드값을 어떻게 바꾸는지
        void apply(int node, int l, int r, int val) {
            int len = r - l + 1;
            if (val == 0) { // occupied면 free 연속 길이 전부 0
                pref[node] = suf[node] = best[node] = 0;
            } else { // free면 free 연속 길이 전부 len
                pref[node] = suf[node] = best[node] = len;
            }
            lazy[node] = val; // 이 구간은 통째로 val로 덮였음을 기록
        }

        // lazy가 있으면 자식에게 전파
        void push(int node, int l, int r) {
            if (lazy[node] == -1 || l == r) return;
            int mid = (l + r) >>> 1;
            apply(node << 1, l, mid, lazy[node]);
            apply(node << 1 | 1, mid + 1, r, lazy[node]);
            lazy[node] = -1;
        }

        // 자식 두 노드 정보를 합쳐서 현재 노드(pref/suf/best) 갱신
        void pull(int node, int l, int r) {
            int mid = (l + r) >>> 1;
            int lc = node << 1, rc = node << 1 | 1;

            int leftLen = mid - l + 1;
            int rightLen = r - mid;

            // pref: 왼쪽 자식의 pref가 왼쪽 구간을 전부 채우면, 오른쪽 자식 pref까지 이어붙일 수 있음
            pref[node] = pref[lc];
            if (pref[lc] == leftLen) pref[node] = leftLen + pref[rc];

            // suf: 오른쪽 자식의 suf가 오른쪽 구간을 전부 채우면, 왼쪽 자식 suf까지 이어붙일 수 있음
            suf[node] = suf[rc];
            if (suf[rc] == rightLen) suf[node] = rightLen + suf[lc];

            // best: (왼쪽 내부 best, 오른쪽 내부 best, 경계 걸친 길이 = suf(left)+pref(right)) 중 최대
            best[node] = Math.max(Math.max(best[lc], best[rc]), suf[lc] + pref[rc]);
        }

        // 외부에서 쓰는 update: [ql, qr]를 val(0/1)로 덮기
        void update(int ql, int qr, int val) {
            update(1, 1, n, ql, qr, val);
        }

        void update(int node, int l, int r, int ql, int qr, int val) {
            if (qr < l || r < ql) return; // 겹치지 않음
            if (ql <= l && r <= qr) {     // 완전히 포함됨
                apply(node, l, r, val);
                return;
            }
            push(node, l, r);
            int mid = (l + r) >>> 1;
            update(node << 1, l, mid, ql, qr, val);
            update(node << 1 | 1, mid + 1, r, ql, qr, val);
            pull(node, l, r);
        }

        // need만큼 연속 free 가능한지 먼저 best[1]로 확인 후,
        // 가능하면 가장 왼쪽 시작 위치를 query로 찾음
        int allocatePos(int need) {
            if (best[1] < need) return 0;
            return query(1, 1, n, need);
        }

        // 가장 왼쪽 시작 위치 찾기:
        // 1) 왼쪽 자식 내부에 가능하면 왼쪽으로 내려감
        // 2) 아니면 왼쪽 suffix + 오른쪽 prefix가 need 이상이면 중앙 걸친 구간 시작점 반환
        // 3) 아니면 오른쪽 자식으로 내려감
        int query(int node, int l, int r, int need) {
            if (l == r) return l;
            push(node, l, r);
            int mid = (l + r) >>> 1;
            int lc = node << 1, rc = node << 1 | 1;

            if (best[lc] >= need) {
                return query(lc, l, mid, need);
            }
            if (suf[lc] + pref[rc] >= need) {
                // 중앙을 걸치는 구간의 시작점:
                // 왼쪽의 연속 free가 suf[lc]이므로 mid - suf[lc] + 1
                return mid - suf[lc] + 1;
            }
            return query(rc, mid + 1, r, need);
        }
    }

    // 변수명 4글자(예: abcd)를 0..26^4-1 정수로 바꾸는 함수
    // 'a'->0, 'b'->1 ... 'z'->25
    static int varId(String s, int startIdx) {
        int a = s.charAt(startIdx) - 'a';
        int b = s.charAt(startIdx + 1) - 'a';
        int c = s.charAt(startIdx + 2) - 'a';
        int d = s.charAt(startIdx + 3) - 'a';
        return (((a * 26) + b) * 26 + c) * 26 + d;
    }

    // "xxxx=malloc(1234);" 형태에서 1234만 뽑아오기
    // (네 코드 기준) 숫자 시작 위치를 12로 고정:
    // index: 0..3=변수, 4='=', 5..10="malloc(", 11부터 숫자일 것 같지만
    // 실제로는 "xxxx=malloc("까지 길이가 11이므로 숫자는 11부터가 일반적.
    // 다만 네 로직은 12부터 읽으므로 입력 형식이 딱 맞는다는 전제하에 동작.
    static int parseSize(String s) {
        int i = 12; // 숫자 시작 인덱스(문제 입력 포맷에 의존)
        int val = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (ch == ')') break;
            val = val * 10 + (ch - '0');
            i++;
        }
        return val;
    }
}
