package exercises;

public class Atoi {
	public int myAtoi1(String s) {
		// Check if empty string
		if(s.isBlank())
			return 0;
		// Index for moving through the string
		int i = 0;
		// Ignore all leading whitespace
		while(s.charAt(i) == ' ')
			i++;
		// Check if positive of negative value
		int sign = (s.charAt(i) == '-') ? -1: 1;
		// Move over if the sign was given 
		if(s.charAt(i) == '-' || s.charAt(i) == '+')
			i++;
		// Save where the number should start
		int start = i;
		// FInd end of the number
		while(i < s.length() && Character.isDigit(s.charAt(i))) {
			i++;
		}
		// Number ends in this position and we reset i
		int stop = i;
		i = start;       
		// Variable for storing result
		int num = 0;
		// Add the number 
		while(i < stop && Math.pow(10, stop - i) >= 1 && num < Integer.MAX_VALUE && num > Integer.MIN_VALUE) {
			num += (s.charAt(i++) - '0') * Math.pow(10, stop - i) * ((sign < 0) ? -1: 1);
		}
		// If overflow we return the maximum or minimum value
		if(num > Integer.MAX_VALUE || num < Integer.MIN_VALUE)
			return (sign < 0) ? Integer.MIN_VALUE: Integer.MAX_VALUE;
		return num;

	}
	public int myAtoi(String s) {
		// Check if empty string
		if(s.isBlank())
			return 0;
		// Index for moving through the string
		int i = 0;
		// Ignore all leading whitespace
		while(s.charAt(i) == ' ')
			i++;
		// Check if positive of negative value
		int sign = (s.charAt(i) == '-') ? -1: 1;
		// Move over if the sign was given 
		if(s.charAt(i) == '-' || s.charAt(i) == '+')
			i++;
		// Variable for storing result
		int num = 0;
		// Add the number 
		while( i < s.length() && Character.isDigit(s.charAt(i)) && num < Integer.MAX_VALUE && num > Integer.MIN_VALUE) {
			// By *10 e add space for the new value to be included
			num = num * 10 + (s.charAt(i++) - '0') * ((sign < 0) ? -1: 1);
		}
		// If overflow we return the maximum or minimum value
		if(num > Integer.MAX_VALUE || num < Integer.MIN_VALUE)
			return (sign < 0) ? Integer.MIN_VALUE: Integer.MAX_VALUE;
		return num;

	}
}
