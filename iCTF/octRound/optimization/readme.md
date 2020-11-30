## Optimization
> I have this new "imaginary" land. I want to make a cool new currency that only uses THREE coins! The things is I'm so tired of having to use so much coins to make change... Can you find the smallest average coins needed to pay any amount of change from 0 to 99?(Note: coins can be of any value from 1 to 99, but they cannot be the same.)(Flag format is ictf{smallest average of coins needed to pay every amount from 0 to 99})

A further explanation of this problem is as following: Given a set of three coin values, find non-negative integer linear combinations that can make the numbers from 0 to 99 such that the number of coins to create the value is minimized. Then, sum the number of coins and divide by 100 to find the average coins.  

As this is bruteforcable and I can't do math, we bruteforce it using a script. In terms of good practice, I probably shouldn't have hardcoded the `lowest` value and the iterations for ints `j` and `k` could definitely be lower, but the runtime wasn't too long.


Main function:
```
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

```


Output:
```
j: 2 k: 3 total: 1683
j: 2 k: 4 total: 1300
j: 2 k: 5 total: 1070
j: 2 k: 6 total: 932
j: 2 k: 7 total: 834
j: 2 k: 8 total: 772
j: 2 k: 9 total: 726
j: 2 k: 10 total: 700
j: 2 k: 11 total: 675
j: 2 k: 12 total: 660
j: 2 k: 13 total: 650
j: 2 k: 15 total: 646
j: 3 k: 11 total: 630
j: 3 k: 12 total: 612
j: 3 k: 13 total: 592
j: 3 k: 14 total: 582
j: 3 k: 15 total: 576
j: 3 k: 16 total: 568
j: 3 k: 18 total: 566
j: 4 k: 15 total: 558
j: 4 k: 17 total: 547
j: 4 k: 18 total: 536
j: 4 k: 22 total: 534
j: 5 k: 22 total: 526
j: 7 k: 18 total: 525
j: 7 k: 23 total: 516
j: 12 k: 19 total: 515
```

The optimal coin values are 1, 12, and 19. Divide the total of 515 by 100 to get the flag.

Flag: `ictf{5.15}`


### Resources 
minCoins function from [here](https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/)

This [paper](https://cs.uwaterloo.ca/~shallit/Papers/change2.pdf) is cool (and confirmed the results of bruteforcing).