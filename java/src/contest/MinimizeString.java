package contest;

public class MinimizeString {
	public int minimizedStringLength(String s) {
		for(int i = 1; i < s.length(); i++) {
			Character c = s.charAt(i);
			s = s.replace(c.toString(), "");
			s = c + s;
		}
		return s.length();
    }
}
