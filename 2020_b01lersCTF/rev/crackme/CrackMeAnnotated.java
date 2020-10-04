import java.util.Random;
import java.util.Scanner;

public class CrackMe {
   public static void main(String[] var0) {
      Scanner s = new Scanner(System.in);
      System.out.println("What is the flag?");
      String input = s.nextLine();
      if (input.length() != 22) {
         System.out.println("too short");
      } else {
         char[] var3 = new char[input.length()];

        // for the length of input, fill var 3
         int var4;
         for(var4 = 0; var4 < input.length(); ++var4) {
            var3[var4] = input.charAt(var4);
         }

         // reverse the string and put it in var 3
         for(var4 = 0; var4 < input.length() / 2; ++var4) {
            char var5 = var3[input.length() - var4 - 1];
            var3[input.length() - var4 - 1] = var3[var4];
            var3[var4] = var5;
         }

         int[] var10 = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};
         int[] var11 = new int[var3.length];
         System.out.println(var10.length);

        // set var 11 to var3 but in the order given by var 10
         for(int i = var10.length - 1; i >= 0; --i) {
            var11[i] = var3[var10[i]];
         }
         
         // random num gen = var 12
         Random var12 = new Random();
         var12.setSeed(431289L);

         //store the new "randomized" array in var 7
         int[] var7 = new int[input.length()];

         for(int j = 0; j < input.length(); ++j) {
            var7[j] = var11[j] ^ var12.nextInt(j + 1);
         }

         String flagStr = "";
        // add all values of the array to a string with dots in between
         for(int k = 0; k < var11.length; ++k) {
            flagStr = flagStr + var11[k] + ".";
         }

         System.out.println(flagStr);

         if (flagStr.equals("97.122.54.50.93.66.99.117.75.51.101.78.104.119.90.53.94.36.102.84.40.69.")) {
            System.out.println("Congrats! You got the flag!");
         } else {
            System.out.println("Not the flag :(");
         }

      }
   }
}
    