// 백준 2178번 "미로 탐색"
// 문제 분류 : DFS, BFS 필수 유형
// 풀이 : 답안참고
// 이해도 : 높음
// 소요 시간 : -


using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string[] inputNM = Console.ReadLine().Split();
        int n = int.Parse(inputNM[0]);
        int m = int.Parse(inputNM[1]);

        int[,] graph = new int[n, m];

        for (int i = 0; i < n; i++)
        {
            string line = Console.ReadLine();


            for (int j = 0; j < m; j++)
            {
                graph[i, j] = line[j] - '0'; // 아스키코드 값을 빼서 정수형으로 변환
            }
        }

        // 방문 횟수를 기록할 2차원 배열 생성
        int[,] visited = new int[n, m];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                visited[i, j] = -1; // -1로 초기화하여 방문하지 않은 상태로 설정
            }
        }

        Queue<(int, int)> q = new Queue<(int, int)>();
        q.Enqueue((0, 0));
        visited[0, 0] = 1; // 시작 위치는 방문 횟수 1로 설정

        // 이동 방향 설정
        int[] dx = { 0, 0, 1, -1 };
        int[] dy = { 1, -1, 0, 0 };

        // BFS 탐색
        while (q.Count > 0)
        {
            var (x, y) = q.Dequeue(); // 튜플 값을 var로 받음
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m)
                {
                    // 경로가 있고, 아직 방문하지 않은 경우
                    if (graph[nx, ny] == 1 && visited[nx, ny] == -1)
                    {
                        q.Enqueue((nx, ny));
                        visited[nx, ny] = visited[x, y] + 1; // 이동 횟수 기록
                    }
                }
            }
        }

        // 도착지점의 방문 횟수 출력
        Console.WriteLine(visited[n - 1, m - 1] != -1 ? visited[n - 1, m - 1] : -1); // 도착지점에 도달하지 못한 경우
    }
}
