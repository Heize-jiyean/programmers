import java.util.Scanner;

public class Main {
    public static int useDay(int L, int P, int V) {
        int quotient = V / P;  // 휴가 기간 동안의 휴가 주기
        int remainder = V % P; // 휴가 기간 동안의 나머지 날짜

        int result = quotient * L;  // 휴가 주기에 따른 사용 가능한 일수
        result += Math.min(remainder, L); // 나머지 날짜 중 사용 가능한 일수

        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int caseNum = 1;
        while (true) {
            // L, P, V 입력
            int L = in.nextInt();
            int P = in.nextInt();
            int V = in.nextInt();

            // 종료 조건 확인
            if (L == 0 && P == 0 && V == 0) {
                break;
            }

            // 결과 출력
            int answer = useDay(L, P, V);
            System.out.println("Case " + caseNum + ": " + answer);

            caseNum++;
        }
    }
}
