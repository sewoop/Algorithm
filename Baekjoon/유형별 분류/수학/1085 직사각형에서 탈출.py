x, y, w, h = map(int, input().split())

# 경우의 수
# len = x # 좌
# len = h - y # 상
# len = w - x # 우
# len = y # 하

data = [x, h - y, w - x, y]
print(min(data))

