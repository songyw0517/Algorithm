# 이진 탐색을 이용한 개수 세기
# 탐색하는 리스트는 정렬되어 있다고 가정
from bisect import bisect_left, bisect_right
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index
if __name__ == '__main__':
    n, x = map(int, input().split())
    array = list(map(int, input().split()))

    # 값이[x,x] 범위에 있는 데이터의 개수 계산
    count = count_by_range(array, x, x)
    if count == 0:
        print(-1)
    else:
        print(count)