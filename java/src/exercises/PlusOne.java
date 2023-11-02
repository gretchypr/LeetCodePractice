package exercises;

public class PlusOne {

	public int[] plusOne(int[] digits) {
		int carry = 0;
        int i = digits.length -1;
        digits[i]++;
        while(i >= 0) {
            digits[i] += carry;
            carry = digits[i]/10;
            digits[i] = digits[i]%10;
            i--;
        }
        
        if(carry > 0) {
            int[] res = new int[digits.length+ 1];
            res[0] = carry;
            for(int j = 0; j < digits.length; j++)
                res[j+1] = digits[j];
            digits = res;
        }
        return digits;
	        
	}
}
