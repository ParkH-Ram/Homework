package backjun;

import java.util.Scanner;

public class Main_행렬 {
	
	public static void main(String[]args) {
	Scanner hi = new Scanner(System.in);
	int N=hi.nextInt();
	int M=hi.nextInt();
	
	// 행렬의 크기 지정 
    // A,B 2차배열 생성
    int [][] A = new int[N][M];
    int [][] B = new int[N][M];
    
    //A 2차배열 값 입력
    //각 배열 번지에 값 저장  A[0][0], A[0][1], A[0][2]  ~ A[2][2] 까지 입력  받음
    for(int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < M ; j++) {
            A[i][j] = hi.nextInt();
        }
    }
    //B 2차배열 값 입력
    //각 배열 번지에 값 저장  B[0][0], B[0][1], B[0][2]  ~ B[2][2] 까지 입력  받음
    for(int i = 0 ; i < N ; i++) {
        for (int j = 0; j < M; j++) {
            B[i][j] = hi.nextInt();
        }
    }
    // A와 B의 각각의 인덱스 값 합 출력  A[0][0] + B[0][0]   ==> 각 번지에 있는 값들의 합을  저
    for(int i = 0 ; i < N ; i++) {
         for (int j = 0 ; j < M ; j++) {
            System.out.print(A[i][j]+B[i][j]+" ");
            
            // 개행을 하기 위한.  행의 작성이 끝나고 다음 열로 이동해 다음 행의 작성을 시작.... 
            if(j == M-1)
                System.out.println();
         }
     }
	}
}
