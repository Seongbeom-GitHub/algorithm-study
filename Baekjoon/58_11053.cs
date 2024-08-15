// 백준 11053번 "가장 긴 증가하는 부분 수열"
// 문제 분류 : 알고리즘 기초 1/2 (다이나믹 프로그래밍)
// 풀이 : 답안참고
// 이해도 : 보통
// 소요 시간 : -

using System;

class Program {

    static void Main() {
        int N = int.Parse(Console.ReadLine());
        int[] A = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        int[] dp = new int[N];

        // dp 테이블 초기화
        for (int i = 0; i < N; i++) {
            dp[i] = 1;
        }
        
        // LIS (Longest Increasing Subsequence) 구하기
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (A[i] > A[j]) {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
        }
        
        int maxLength = 0; // 최장 길이
        for (int i = 0; i < N ; i++) {
            maxLength = Math.Max(maxLength, dp[i]);
        }

        Console.WriteLine(maxLength);
        
    }

    
}