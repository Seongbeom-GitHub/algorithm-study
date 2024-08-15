using System;

class Program {

    static void Main() {
        
        int[] inputValue = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int n = inputValue[0];
        int m = inputValue[1];

        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                
                if (i != j) {
                    Console.WriteLine($"{i} {j}");

                }


            }
        }

    }
    
    
    
    
    
}