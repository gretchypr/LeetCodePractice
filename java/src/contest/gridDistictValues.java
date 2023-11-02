package contest;

import java.util.HashSet;
import java.util.Set;

public class gridDistictValues {
	public int[][] differenceOfDistinctValues(int[][] grid) {
		int[][] result = new int[grid.length][grid[0].length];
		for(int i = 0; i < grid.length; i++) {
			for(int j = 0; j < grid[i].length; j++) {
				Set<Integer> setL = new HashSet<Integer>();
				Set<Integer> setR = new HashSet<Integer>();
				int c = j - 1, r = i - 1;
				while(c >= 0 && r >= 0) {
					setL.add(grid[r--][c--]);
				}
				c = j + 1;
				r = i + 1;
				while(r < grid.length && c < grid[0].length) {
					setR.add(grid[r++][c++]);
				}
				
				result[i][j] = Math.abs(setL.size() - setR.size());
			}
		}
		return result;
	}
}
