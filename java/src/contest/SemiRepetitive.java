package contest;

import java.util.HashSet;

public class SemiRepetitive {
	public int longestSemiRepetitiveSubstring(String s) {
		if(s.length() == 1)
			return 1;
		int maxLength = 1;
		
		for(int i =0; i < s.length(); i++) {
			maxLength = Math.max(maxLength, longestSemiRep(s.substring(i)));
			if(maxLength > s.length()/2)
				return maxLength;
		}
		return maxLength;
		
	}
	private int longestSemiRep(String s) {
		HashSet<Character> nums = new HashSet<Character>();
		int repCount = 0;
		for(int i =0; i < s.length(); i++) {
			
			if(!nums.add(s.charAt(i))) {
				if(repCount == 1) return i;
				repCount++;
			}
		}
		return s.length();
	}
}
