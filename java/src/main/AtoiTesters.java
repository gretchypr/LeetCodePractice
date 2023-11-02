package main;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;

import exercises.Atoi;

public class AtoiTesters {
	
	@Test
	public void test1() {
		Atoi a = new Atoi();
		assertEquals(42, a.myAtoi("42"));
	}
	@Test
	public void test2() {
		Atoi a = new Atoi();
		assertEquals(-42, a.myAtoi("-42"));
	}
	@Test
	public void test3() {
		Atoi a = new Atoi();
		assertEquals(42, a.myAtoi("      +42jihikni"));
	}
	@Test
	public void test4() {
		Atoi a = new Atoi();
		assertEquals(-2147483648, a.myAtoi("-91283472332"));
	}
	@Test
	public void test5() {
		Atoi a = new Atoi();
		assertEquals(2147483647, a.myAtoi("91283472332"));
	}
	@Test
	public void test6() {
		Atoi a = new Atoi();
		assertEquals(-90, a.myAtoi("   -90.1"));
	}
	@Test
	public void test7() {
		Atoi a = new Atoi();
		assertEquals(0, a.myAtoi(""));
	}
	@Test
	public void test8() {
		Atoi a = new Atoi();
		assertEquals(0, a.myAtoi("    "));
	}
	@Test
	public void test9() {
		Atoi a = new Atoi();
		assertEquals(0, a.myAtoi(".158"));
	}
	@Test
	public void test10() {
		Atoi a = new Atoi();
		assertEquals(-2147483647, a.myAtoi("-2147483647"));
	}
	@Test
	public void test11() {
		Atoi a = new Atoi();
		assertEquals(2147483646, a.myAtoi("2147483646"));
	}

}
