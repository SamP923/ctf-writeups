class Main {
	public static void main(String[] args) {
		int[] numArr = {11, 34, 9,59,90,157,153,154,185,92,157,26,153,153,155,94};
    
		String str = "hey guys this is a leet string which is not related to the flag. Also dont search for ictf{?_?} stuff, you wont find any :) Lets count till 10, right? 123456789. No!! You forgot the 0! Muahahaha! Im tired of this XD";
		String pt = "";
		for (int i = 0; i < numArr.length; i++){
			pt += str.charAt(numArr[i]);
		}

		System.out.println(pt);
  }
}