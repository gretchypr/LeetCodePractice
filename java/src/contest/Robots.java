package contest;

import java.util.HashMap;

public class Robots {
	public int sumDistance(int[] nums, String s, int d) {
		for(int i = 0; i < d; i++) {
//			collisionCheck(nums, s);
			for(int j = 0; j < nums.length; j++) {
				if(s.charAt(j) == 'R')
					nums[j]++;
				else
					nums[j]--;
			}
		}
		int modulo = 1000000007;
		long res = 0;
		for(int i = 0; i < nums.length; i++) {
			for(int j = i + 1; j < nums.length; j++) {
				res += ((Math.abs(nums[i] - nums[j]) % modulo) + modulo) % modulo;
			}
		}
		return (int) res;
		
	}
	private void collisionCheck(int[] nums, String s) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		StringBuilder sb = new StringBuilder(s);
		for(int i = 0; i < nums.length; i++) {
			Integer position = 0;
			if((position = map.putIfAbsent(nums[i], i)) != null) {
				if(sb.charAt(position) == 'R')
					sb.setCharAt(position, 'L');
				else
					sb.setCharAt(position, 'R');
				if(sb.charAt(i) == 'R')
					sb.setCharAt(i, 'L');
				else
					sb.setCharAt(i, 'R');
			}
		}
	}
}
