import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//23309번

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        //2단 배열로 만들어서 시간초과난거같음 -> 그래서 1단 배열로 전역과 다음역을 나타내는 역 2개만듬
        int[] preArr = new int [1000001];
        int[] postArr = new int [1000001];

        //첫역 넣기
        int firstStation = Integer.parseInt(st.nextToken());
        int prevStation = firstStation;

        //두번째역부터 마지막역 전까지 넣기
        for (int i = 1; i < N-1; i++) {
            int station = Integer.parseInt(st.nextToken());
            preArr[station] = prevStation;
            postArr[prevStation] = station;
            prevStation = station;
        }
        //마지막역 넣기
        int LastStation = Integer.parseInt(st.nextToken());
        postArr[prevStation] = LastStation;
        preArr[LastStation] = prevStation;
        postArr[LastStation] = firstStation;
        preArr[firstStation] = LastStation;

        StringBuilder sb = new StringBuilder();
        //이제 이전역과 다음역이 정리된 역배열을 토대로 공사시작
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            int curStation = Integer.parseInt(st.nextToken());
            if(str.contains("BN")){  //BN일시 다음역 고유번호 출력후 그 사이에 고유번호 j인 역 생성
                int newStation = Integer.parseInt(st.nextToken());
                int nextStation = postArr[curStation];
                sb.append(nextStation).append("\n");
                //arr[newStation][0]=현재역 [1]= arr[curSation][1] 로 설정한다
                //현재역의 다음역을 newStation으로 설정 그리고
                //그러면 다음역의 이전역을 새로운 역으로 설정 arr[arr[curSation][1]][0] = newStation
                postArr[curStation] = newStation;
                preArr[newStation] = curStation;
                postArr[newStation] = nextStation;
                preArr[nextStation] = newStation;
            }
            else if(str.contains("BP")){  //BP일시 이전역 고유번호 출력후 그 사이에 고유번호 j인 역 생성
                int newStation = Integer.parseInt(st.nextToken());
                int beStation = preArr[curStation];
                sb.append(beStation).append("\n");
                //이전역의 [1] = newStation이 되고
                //newSation[0] = 이전역,   [1] = curStation
                //curSation[0] =  newStation이 된다.
                postArr[beStation] = newStation;
                preArr[newStation] = beStation;
                postArr[newStation]  = curStation;
                preArr[curStation] = newStation;
            }
            else if(str.contains("CN")){  //CN일시 다음역 폐쇄 후 그 역 번호 출력
                //폐쇄할거면 arr[curStation][1] = arr[[arr[curStation][1]][1]이되야함 다음역의 다음역
                int nextStation = postArr[curStation];
                sb.append(nextStation).append("\n");
                int nextNextStation = postArr[nextStation];
                postArr[curStation] = nextNextStation;
                preArr[nextNextStation] = curStation;
            }
            else if(str.contains("CP")){  //CP일시 이전역 폐쇄 후 그 역 번호 출력
                int beStation = preArr[curStation];
                sb.append(beStation).append("\n");
                int beBeStation = preArr[beStation];
                preArr[curStation] = beBeStation;
                postArr[beBeStation] = curStation;
            }
        }
        System.out.println(sb);
    }
}