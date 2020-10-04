import java.util.Random;
import java.util.Scanner;

class CrackMeSolve {

  public static void main(String[] args) {
    int[] flagArr = new int[]{97, 122, 54, 50, 93, 66, 99, 117, 75, 51, 101, 78, 104, 119, 90, 53, 94, 36, 102, 84, 40, 69};


    // random num gen = var 12
    Random var12 = new Random();
    var12.setSeed(431289L);

    // XOR flag with random
    int[] var7 = new int[flagArr.length];
    for ( int j = 0; j < flagArr.length; j++ ){
      var7[j] = flagArr[j] ^ var12.nextInt(j+1);
    }

    // set var 11 to corresponding numbers in var10
    int[] var10 = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};
    int[] var11 = new int[flagArr.length];
    for( int i = flagArr.length - 1; i >= 0; i--){
      var11[var10[i]] = var7[i];
    }

    //reverse the array
    char[] var3 = new char[flagArr.length];
    
    int var4;
    for(var4 = 0; var4 < flagArr.length; ++var4) {
      var3[var4] = (char) var11[var4];
    }

    for(var4 = 0; var4 < flagArr.length / 2; ++var4) {
      char var5 = var3[flagArr.length - var4 - 1];
      var3[flagArr.length - var4 - 1] = var3[var4];
      var3[var4] = var5;
    }

    String flagStr = "";
    for(int k = 0; k < var10.length; ++k) {
      flagStr = flagStr + var3[k];
    }

    System.out.println(flagStr);

  }
}