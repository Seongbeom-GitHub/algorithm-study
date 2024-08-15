// 백준 15649번 "N과 M(1)"
// 문제 분류 : NHN 코딩테스트 기출 유형
// 풀이 : 답안참고
// 이해도 : 높음
// 소요 시간 : -

using System;
using System.Collections.Generic;

class Program {

    static int n, m;
    static List<int> array = new List<int>();

    static void Main() {

        string[] inputValue = Console.ReadLine().Split(" ");
        n = int.Parse(inputValue[0]);
        m = int.Parse(inputValue[1]);

        BackTacking();

    }


    // 재귀 호출 할 백트래킹 메서드
    static void BackTacking() {
        if (array.Count == m) {
            Console.WriteLine(string.Join(" ", array));
            return;
        }

        for (int i = 1; i < n + 1; i++) {
            if (!array.Contains(i)) { // i가 이미 선택되지 않았는지 체크
                array.Add(i); // 배열에 i값 추가
                BackTacking(); // 재귀 호출
                array.RemoveAt(array.Count - 1); // 배열의 마지막 값 삭제
            }
        }
    }
}