package exercises;

import java.util.HashMap;

public class TwoSum {
	public int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> values = new HashMap<Integer, Integer>();
		for(int i = 0; i < nums.length; i++) {
			Integer a = values.get(target - nums[i]);
			if(a != null)
				return new int[] {a, i};
			values.put(nums[i], i);
		}
		return new int[] {0, 1};
	}
}
