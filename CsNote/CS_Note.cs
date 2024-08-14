using System;

class MathUtils
{
    public static int Add(int a, int b)
    {
        return a + b;
    }
}

class Program
{
    static void Main()
    {
        // 호출 예
        int result = MathUtils.Add(3, 4); // 객체 생성 없이 호출 가능
        Console.WriteLine(result); // 결과 출력
    }
}
