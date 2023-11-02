package contest;

public class SemiOrderedPermutations {
	public int semiOrderedPermutation(int[] nums) {
//		int i = 0;
//		int count = 0;
//		while(nums[i] != 1) i++;
//		while(i > 0) {
//			swap(nums, i, i - 1);
//			i--;
//			count++;
//		}
//		i = nums.length - 1;
//		while(nums[i] != nums.length) i--;
//		while(i < nums.length - 1) {
//			swap(nums, i + 1, i);
//			i++;
//			count++;
//		}
//		return count;
		int i = 0, j = nums.length - 1;
		while(nums[i] != 1 || nums[j] != nums.length) {
			if(nums[i] != 1) i++;
			if(nums[j] != nums.length) j--;
		}
		return i + (nums.length - 1 - j) + ((i > j) ? -1 : 0);
	}
	private void swap(int[] nums, int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}
}
