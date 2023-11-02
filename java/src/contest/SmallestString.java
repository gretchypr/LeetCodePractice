package contest;

public class SmallestString {
	public String smallestString(String s) {
		int i = 0;
		char[] str = s.toCharArray();
		while(i < s.length() && str[i] == 'a') {
			i++;
		}
		
		if(i == s.length())
			str[i-1] = 'z';
		for(; i < s.length(); i++) {
			if(str[i] == 'a')
				break;
			str[i]= (char) (((str[i] - 'a' - 1) % 26) + 'a');
		}
		return new String(str);
	}
}
