# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: x[1])
#     camera = -30001

#     for route in routes:
#         if camera < route[0]:
#             answer += 1
#             camera = route[1]
#     return answer

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    camera = -30000

    for route in routes:
        if route[0] <= camera:
            camera = min(camera, route[1])
        else:
            answer += 1
            camera = route[1]

    return answer

if __name__ == "__main__":
    routes = [[-20, 15], [-14,-5], [-18,-13], [-5,-3]]
    print(solution(routes))