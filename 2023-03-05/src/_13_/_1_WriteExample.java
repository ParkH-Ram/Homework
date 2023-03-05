package _13_;

import java.io.FileOutputStream;
import java.io.OutputStream;

public class _1_WriteExample {
	public static void main(String[]args) {
		try {
			OutputStream os = new FileOutputStream("C:/Temp/test1.db");
			
			byte a=10;
			byte b=20;
			byte c=30;
			
			
			//1byte 씩 출력 
			os.write(a);          
			os.write(b);
			os.write(c);
			
			// os 내부 버퍼에 잔류하는 바잍느를 출력하고 버퍼를 비움
			os.flush();
			//출력 스트림을 닫아 메모리 해제
			os.close();
			
		}catch(Exception e){
			System.err.println(e.getMessage());
		}
	}
}
