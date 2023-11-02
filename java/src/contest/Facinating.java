package contest;

import java.util.HashSet;

public class Facinating {
	public boolean isFacinating(int n) {
		String concat = n + "" + n*2 + "" + n*3;
		if(concat.length() > 9 || concat.contains("0"))
			return false;
		HashSet<Character> nums = new HashSet<Character>();
		for(int i = 0; i < concat.length(); i++) {
			if(!nums.add(concat.charAt(i)))
				return false;
		}
		return true;
	}
}
