package contest;

public class MatrixQueries {
	public long matrixSumQueries(int n, int[][] queries) {
		int[][] result = new int[n][n];
		long c = 0;
		
		for(int i = 0; i < queries.length; i++) {
			if(queries[i][0] == 0) {
				for(int j = 0; j < n; j++) {
					c = c - result[queries[i][1]][j] + queries[i][2];
					result[queries[i][1]][j] = queries[i][2];
				}
				
			}
			else {
				for(int j = 0; j < n; j++) {
					c = c - result[j][queries[i][1]] + queries[i][2];
					result[j][queries[i][1]] = queries[i][2];
				}
			}
		}
		return c;
	}
}
