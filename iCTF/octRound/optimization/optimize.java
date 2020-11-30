class Main {
	public static int minCoins(int[] coins, int m, int V){
    int table[] = new int[V+1];

    table[0] = 0;

    for (int i =1; i <=V; i++){
      table[i] = Integer.MAX_VALUE;
    }

    for (int i =1; i<=V; i++){
      for (int j = 0; j < m; j++) 
        if (coins[j] <= i) { 
          int sub_res = table[i - coins[j]]; 
          if (sub_res != Integer.MAX_VALUE  && sub_res + 1 < table[i]) 
            table[i] = sub_res + 1;              
          } 
    }

    return table[V];
  }

  public static void main(String[] args) {
    
    int coins[] = {3, 2, 1};
    int m = coins.length;
    int lowest = 3000;
    //control second valued coin
    for ( int j = 2; j<97; j++){
      //control highest value coin
      for (int k = 3; k < 97; k++){
        int total = 0;
        coins[0] = k; coins[1] = j;

        //calculate minimum amount of coins for each value
        for ( int i = 1; i <= 99; i++){
          total += minCoins(coins, m, i);  
        }
  
        if ( total < lowest ){
          lowest = total;
          System.out.println("j: " + j + " k: " + k + " total: " + total);
        }
      
      
      }
      
    }

  }
}