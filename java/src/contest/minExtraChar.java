package contest;

import java.util.Arrays;

public class minExtraChar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {3,2,3};
		int[] arr2 = new int[] {4,3,2,5,2};
		// int[][] arr = new int[][] {{1,1,2}, {1,2,4}, {1,1,1}, {2,5,6}};
		// for(Integer i: arr)
		//     System.out.println(i);
		// stuff(arr);
		System.out.println("Return: " + stuff("aakodubkrlauvfkzje", new String[] {"ix","qoqw","ax","ar","v","hxpl","nxcg","thr","kod","pns","cdo","euy","es","rf","bxcx","xe","ua","vws","vumr","zren","bzt","qwxn","ami","rrbk","ak","uan","g","vfk","jxmg","fhb","nqgd","fau","rl","h","r","jxvo","tv","smfp","lmck","od"}));
		System.out.println("Return: " + stuff("sayhelloworld", new String[] {"hello", "world"}));


		// for(Integer i: arr)
		//     System.out.println(i);
	}

	public static int stuff(String s, String[] dictionary) {
		Arrays.sort(dictionary, (a, b)->Integer.compare(a.length(), b.length()));
		String substrings = s;
		for(int i = dictionary.length - 1; i >= 0; i--) {

			if(s.contains(dictionary[i]))
				substrings = s + "-" + substrings.replace(dictionary[i], "#") + "-" + s.replace(dictionary[i], "#");
		}
		String[] p = substrings.strip().replace("#", "").split("-");
		String shortest = p[1];
		for(int i = 1; i < p.length; i++)
			shortest = (p[i].length() < shortest.length()) ? p[i] : shortest;
		return shortest.length();
	} 
	/*
	 * "aakodubkrlauvfkzje"
["ix","qoqw","ax","ar","v","hxpl","nxcg","thr","kod","pns","cdo","euy","es","rf","bxcx","xe","ua","vws","vumr","zren","bzt","qwxn","ami","rrbk","ak","uan","g","vfk","jxmg","fhb","nqgd","fau","rl","h","r","jxvo","tv","smfp","lmck","od"]
	 */
}
