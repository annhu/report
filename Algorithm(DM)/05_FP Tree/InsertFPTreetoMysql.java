package yb101_5_project;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.*;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;

// delete a employee data
public class InsertFPTreetoMysql {

	public static void main(String[] args) {
		Connection conn = null;
		try { 
			
			String connUrl = "jdbc:mysql://10.120.28.19:3306/db01";
			conn = DriverManager.getConnection(connUrl, "yb101", "iii");
			
			String insStmt = "INSERT INTO route VALUES(?,?,?)";
			PreparedStatement pstmt = conn.prepareStatement(insStmt);
			
			String dataline = null;
			String[] data;
			int routeid=0;
			
			File readfile = new File("C://Users//BigData//100_project//route//fp_list_5.txt");
			InputStreamReader fr = new InputStreamReader(new FileInputStream(readfile),"UTF-8");
			BufferedReader br = new BufferedReader(fr);
			while ((dataline = br.readLine()) != null) {
				data = dataline.split(" : ");
				routeid++;
				//System.out.println(data[0]);
				//System.out.println(data[1]);
				pstmt.setInt(1, routeid);
				pstmt.setInt(2,Integer.parseInt(data[1]));
				pstmt.setNString(3,data[0]);
				int num = pstmt.executeUpdate();
				System.out.println("insert count = " + num);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} catch (IOException i){
			i.printStackTrace();
		} finally {
			if (conn != null)
				try {
					conn.close();
				} catch(SQLException e) { 
					e.printStackTrace();
				}
		}
	}// end of main()
}// end of class DeleteDemo
