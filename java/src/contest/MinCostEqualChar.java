package contest;

public class MinCostEqualChar {
	public long minimumCost(String s) {
		int halfway = s.length()/2;
		int i = halfway;
		int count = 0;
		while(i > 0) {
			if(s.charAt(i) != s.charAt(i-1)) {
				count += i;
			}
			i--;
		}
		i = halfway;
		while(i < s.length() - 1) {
			if(s.charAt(i) != s.charAt(i+1)) {
//				s = flip(s, i + 1, s.length()-1);
				count += s.length() - 1 - i;
			}
			i++;
		}
		return count;
	}
	
}
