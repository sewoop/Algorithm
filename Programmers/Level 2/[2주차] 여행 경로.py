def solution(tickets):
    answer = []

    graph = {}
    for ticket in tickets:
        if ticket[0] not in graph.keys():
            graph[ticket[0]] = [ticket[1]]
        else:
            graph[ticket[0]].append(ticket[1])
            graph[ticket[0]].sort()

    print(graph)

    start = "ICN"
    queue = [start]

    while queue:
        node = queue.pop(0)
        answer.append(node)

        if node in graph.keys() and len(graph[node]) > 0:
            queue.append(graph[node].pop(0))
        
        print(queue)

    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"],["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# tickets = [["ICN", "COO"], ["COO", "ICN"],["COO", "ICN"]]
tickets =  [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
print(solution(tickets))