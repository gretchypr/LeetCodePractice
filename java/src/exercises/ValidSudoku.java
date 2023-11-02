package exercises;

import java.util.HashSet;

public class ValidSudoku {
	public boolean isValidSudoku(char[][] board) {
		for(int row = 0; row < 9; row++) {
			HashSet<Character> content = new HashSet<Character>();
			for(int col = 0; col < 9; col++) {
				if(board[row][col] != '.') {
					if(!content.add(board[row][col]))
						return false;
				}
			}
		}
		for(int col = 0; col < 9; col++) {
			HashSet<Character> content = new HashSet<Character>();
			for(int row = 0; row < 9; row++) {
				if(board[row][col] != '.') {
					if(!content.add(board[row][col]))
						return false;
				}
			}
		}
		for(int row = 0; row < 3; row++) {
			HashSet<Character> content = new HashSet<Character>();
			for(int col = 0; col < 3; col++) {
				if(board[row][col] != '.') {
					if(board[row + 1][(col*3 + 1)%(3*(col + 1))] != '.' && !content.add(board[row][col]))
						return false;
				}
			}
		}
		
		return true;
	}
}
