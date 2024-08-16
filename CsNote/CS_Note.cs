using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()); // 컴퓨터 개수
        int v = int.Parse(Console.ReadLine()); // 연결선 개수

        List<int>[] graph = new List<int>[n + 1]; // 그래프 초기화
        for (int i = 0; i <= n; i++)
        {
            graph[i] = new List<int>();
        }

        bool[] visited = new bool[n + 1]; // 방문한 컴퓨터인지 표시

        for (int i = 0; i < v; i++) // 그래프 생성
        {
            var input = Console.ReadLine().Split();
            int a = int.Parse(input[0]);
            int b = int.Parse(input[1]);

            graph[a].Add(b); // a에 b 연결
            graph[b].Add(a); // b에 a 연결 -> 양방향
        }

        // DFS 메서드 정의
        void Dfs(int node)
        {
            visited[node] = true; // 현재 노드 방문 표시

            foreach (int next in graph[node])
            {
                if (!visited[next]) // 방문하지 않은 노드에 대해 DFS 호출
                {
                    Dfs(next);
                }
            }
        }

        Dfs(1); // 1번 컴퓨터에서 DFS 시작

        // 방문한 컴퓨터 수 출력 (1번 컴퓨터 제외)
        Console.WriteLine(visited.Count(v => v) - 1);
    }
}
