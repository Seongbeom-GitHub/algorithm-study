using System;
using System.Collections.Generic;

class Program {

    static int n, m;
    static List<int> array = new List<int>();

    static void Main() {

        string[] inputValue = Console.ReadLine().Split(" ");
        n = int.Parse(inputValue[0]);
        m = int.Parse(inputValue[1]);

        BackTracking();

    }


    // 재귀 호출 할 백트래킹 메서드
    static void BackTracking() {
        if (array.Count == m) {
            Console.WriteLine(string.Join(" ", array));
            return;
        }

        for (int i = 1; i < n + 1; i++) {
            if (!array.Contains(i)) { // i가 이미 선택되지 않았는지 체크
                array.Add(i); // 배열에 i값 추가
                BackTracking(); // 재귀 호출
                array.RemoveAt(array.Count - 1); // 배열의 마지막 값 삭제
            }
        }
    }
}