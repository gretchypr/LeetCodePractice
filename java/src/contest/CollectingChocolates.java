package contest;

import java.util.LinkedList;

public class CollectingChocolates {
	public long minCost(int[] nums, int x) {
		int sum = 0;
		LinkedList<Integer> positions = new LinkedList<Integer>();
		
		for(int i = 0; i < nums.length; i++) {
			positions.addLast(i);
		}
		while(!positions.isEmpty() ) {
			int pos = positions.getFirst();
			if(nums[pos] < x) {
				sum += nums[pos];
			}
			else {
				positions.addLast((pos == 0) ? -1:pos-1);
				
			}
			positions.removeFirst();
		}
		return sum;
		
	}
}
