성공코드(못품)

1. 발상: 결합법칙에 의해 영향을 주는 '-'기준으로 나누어서 부분 계산 
2. 구현
    1. 결합법칙에 의해 앞부분 - 가 뒤에 영향 줄 수 있으므로 뒤부터 ``` arrs[:0:-1] ``` 계산
    2. 결합법칙에 의해 가능한 경우는 
        -  -(현재값 + 누적값) 
        -  -현잿값 + 누적값

    **따라서 max계산은 max(현재min-누적min,현재max+누적max) 
    <br/>
    min 계산은 min( 현재min -누적max , 현재min+누적min)**


```python
def solution(arr):
    arrs = ''.join(arr).split('-')
    
    val0 = sum(list(map(int, arrs[0].split('+'))))
    if len(arrs) ==1:
        return val0 # +기호만 있는 경우. 
    
    min_val, max_val = 0,0 
    
    for arr in arrs[:0:-1]:
        x = list(map(int, arr.split('+')))
        _min_val = -(sum(x)) # -(a+b+c)
        _max_val = -x[0]+ sum(x[1:]) # -a+b+c
        # 맨 뒤부터 min max 갱신 # max 값 주의: -(현재값 - 누적값) 이므로 현재값은 자동으로 min값됨 
        min_val, max_val  = min(_min_val + min_val, _min_val - max_val), max(_max_val + max_val, _min_val - min_val)
                              
    return val0 + max_val
    ```