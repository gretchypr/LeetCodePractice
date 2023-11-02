package contest;

public class MinNorMax {
	public int findNonMinOrMax(int[] nums) {
		if(nums.length <= 2)
			return -1;
		int min = 0, max = 0;
		
		for( int i = 0; i < nums.length; i++) {
			min = (nums[min] > nums[i]) ? i : min;
			max = (nums[max] < nums[i]) ? i : max;
		}
		int i = 0;
		while(i == min || i == max)
			i++;
		return nums[i];
		
    }
}
