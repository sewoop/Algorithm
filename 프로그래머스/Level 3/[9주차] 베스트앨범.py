from collections import defaultdict
from functools import reduce


def solution_0(genres, plays):
    answer = []
    album = defaultdict(list)

    for i, v in enumerate(zip(genres, plays)):
        album[v[0]].append((v[1], i))

    album_list = []
    for genre in set(genres):
        album[genre].sort(key=lambda x: (-x[0], x[1]))
        temp = reduce(lambda x, y: x + y[0], album[genre], 0)
        album_list.append((temp, album[genre]))

    album_list.sort(reverse=True)

    for i in album_list:
        for idx, j in enumerate(i[1]):
            if idx < 2:
                answer.append(j[1])

    return answer


def solution(genres, plays):
    answer = []

    album = {}
    for i, v in enumerate(zip(genres, plays)):
        if v[0] not in album:
            album[v[0]] = [v[1], [(v[1], i)]]
        else:
            album[v[0]][0] += v[1]
            album[v[0]][1].append((v[1], i))

    for genre in set(genres):
        album[genre][1].sort(key=lambda x: (-x[0], x[1]))

    album_list = list(album.values())
    album_list.sort(reverse=True)

    for i in album_list:
        for j in i[1][:2]:
            answer.append(j[1])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# genres = ["classic", "classic", "classic", "pop"]
# plays = [500, 200, 200, 2500]

print(solution(genres, plays))
