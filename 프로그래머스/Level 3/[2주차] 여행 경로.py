from collections import defaultdict


def solution(tickets):
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)

        for r in routes:
            routes[r].sort()

        return routes

    # DFS
    def nextRoute():
        stack = ['ICN']
        path = []  # 가려고하는 경로를 저장하는 변수

        while stack:
            top = stack[-1]

            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    answer = nextRoute()

    return answer


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"],["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# tickets =  [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
# tickets = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'K']]
tickets = [['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]
# tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]
# tickets = [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]
print(solution(tickets))
