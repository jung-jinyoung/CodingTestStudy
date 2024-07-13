실패코드
<br/>
---
    발상: 점화식을 사용했으므로 i-2를 기준으로 i, i-1 칸의 값이 채워져 있어야 한다고 생각함

    구현: 0과 1을 세가지 경우의 수로 나누고 (00, 01, 10)
    10의 경우 find(배열, n-=1)로 마지막 칸을 고려하지 않음
-
    문제: 부분해의 값이 최적해가 되지 않음
    ```[10, 2, 2, 100, 2]``` 의 경우 코드에 따라 두칸 전만 고려하므로 실패 
    <b>점화식으로 생각하느라 DP가 구현되지 않음</b>

```python
def solution(money):
    
    def find(dp,n):
        for i in range(2,n):
            dp[i] = max(dp[i-2]+money[i], dp[i-1])
        return max(dp)
    
    n = len(money)
    res = []    
    
    if n <=2:
        return max(money)
    
    dp0 = [0 for _ in range(n)]
    res.append(find(dp0,n))
    
    dp1 = [0 for _ in range(n)]
    dp1[0] = money[0]
    res.append(find(dp1,n-1))
    
    dp2 = [0 for _ in range(n)]
    dp2[1] = money[1]
    res.append(find(dp2,n))
    
    answer = max(res)
    return answer

```
성공 코드
<br/>
---
    1. 배열 특성에 따라 i-2가 음수면 맨 뒤부터의 값 갖게되므로 굳이 i 앞 두칸 채울 필요 x (즉 경우의 수를 00 01 10 으로 나눌필요x)
   
    2. 부분해가 최적해가 되기 위해 기존 dp개념에서 추가 조건을 최소한으로 달기
    -> 처음부터 0칸 또는 -1칸을 제외하고 dp 
    -> 0칸과 -1칸 모두 제외하는 경우는 알아서 걸러짐 

```python
def solution(money):
    n = len(money)
    
    if n <=2:
        return max(money)
    
    def find(money_list):
        dp = [0] * (n-1)
        dp[0] = money_list[0]
        dp[1] = max(money_list[0], money_list[1])
        
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + money_list[i])
        
        return dp[-1]
    
    case1 = find(money[:-1])
    case2 = find(money[1:])
    
    return max(case1, case2)
    ```

# 07.08 java코드 추가
---
    java코드는 리스트 슬라이싱이 없으므로 어레이 두개 만들기 

```java

class Solution {
    public int solution(int[] money) {
        
        // money의 0선택하고 -1선택 안하기 , 0선택안하기
        
        int n = money.length;
        int[] case1 = new int[n];
        case1[0] = case1[1] = money[0];
        
        
        int[] case2 = new int[n];
        case2[0] = 0;
        case2[1] = money[1];
        
        for (int i=2; i<n; i++){
            case1[i] = Math.max(case1[i-2]+money[i], case1[i-1]);
            case2[i] = Math.max(case2[i-2]+money[i], case2[i-1]);
        }
        
        int answer = Math.max(case1[n-2], case2[n-1]);
        return answer;
    }
}
```