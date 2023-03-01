package backjun;

import java.util.Scanner;

public class Main_행렬덧셈 {
	Scanner hi = new Scanner(System.in);
	int N=hi.nextInt();
	int M=hi.nextInt();
	
	// 행렬의 크기 지정 
	int [][] array = new int[N][M]        ;
	
	
	for (int i=0; i<2; i++ ) {
		for (int j=0; j<N; j++) {
			for(int ij=0; ij<M; ij++) {
				array[j][ij] = array[i][ij] + hi.nextInt();
			}
			
		}
	}
	
	for (int k = 0; k < N; k++) {
		for (int l = 0; l < M; l++) {
			System.out.print(array[k][l] + " ");
		}
		System.out.println();
	
	//. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
	//  이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
	//  N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
	
	}
	
}
