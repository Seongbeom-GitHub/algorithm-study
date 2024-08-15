// 백준 2304번 "창고 다각형"
// 문제 분류 : 알고리즘 기초 1/2 (자료구조)
// 풀이 : 답안참고
// 이해도 : 높음
// 소요 시간 : -

using System;

class Program{

    static void Main() {
        int m = 0;
        int m_index = 0;
        int[] pli = new int[1001]; // 기둥

        // 입력
        int n = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < n; _++) {
            string[] input = Console.ReadLine().Split();
            int L = int.Parse(input[0]);
            int H = int.Parse(input[1]);
            pli[L] = H;

            if (m < H) {
                m_index = L;
                m = H;
            }
        }
        
        int curr = 0;
        int result = 0;

        for (int i = 0; i <= m_index; i++) {
            curr = Math.Max(curr, pli[i]);
            result += curr;
        }        
        
        curr = 0;
        for (int i = 1000; i > m_index; i--) {
            curr = Math.Max(curr, pli[i]);
            result += curr;
        }
        
        Console.WriteLine(result);
        
        
        

    }
}