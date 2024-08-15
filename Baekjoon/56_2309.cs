// 백준 2304번 "창고 다각형"
// 문제 분류 : 알고리즘 기초 2/2
// 풀이 : 답안참고
// 이해도 : 높음
// 소요 시간 : -

using System;
using System.Collections.Generic;
using System.Linq; 

class Program 
{
    static void Main()
    {
        List<int> heights = new List<int>();

        for (int _ = 0; _ < 9; _++) 
        {
            heights.Add(int.Parse(Console.ReadLine()));
        }

        int total = heights.Sum();
        int one = 0;
        int two = 0;

        for (int i = 0; i < 9; i++)
        {
            for (int j = i + 1; j < 9; j++)
            {
                if (total - (heights[i] + heights[j]) == 100)
                {
                    one = heights[i];
                    two = heights[j];
                    break;
                }
            }
            if (one != 0 && two != 0)
            {
                break;
            }
        }

        heights.Remove(one);
        heights.Remove(two);
        heights.Sort();

        foreach (var height in heights)
        {
            Console.WriteLine(height);
        }
    }
}