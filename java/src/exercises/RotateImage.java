package exercises;

public class RotateImage {
	public void rotateImage(int[][] matrix) {
		for(int r = 0; r < matrix.length/2; r++) {
			for(int c = r; c < matrix.length-1-r; c++) {
				int temp = matrix[r][c];
				matrix[r][c] = matrix[matrix.length - 1 - c][r];
				matrix[matrix.length - 1 - c][r] = matrix[matrix.length  - 1 - r][matrix.length - 1 - c];
				matrix[matrix.length  - 1 - r][matrix.length - 1 - c] = matrix[c][matrix.length - 1 - r];
				matrix[c][matrix.length - 1 - r] = temp;
			}
		}
	}
}
