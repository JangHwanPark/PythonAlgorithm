def dfs(graph, start, vis):
    # 현재 노드를 방문 처리
    vis[start] = True

    # depth 출력
    print(start)

    # 현재 가리키고있는 노드와 연결된 다른 노드 재귀적으로 방문
    for i in graph[start]:
        if not vis[i]:
            dfs(graph, i, vis)


graph = [
    [],
    [1, 3, 2],
    [1, 4, 5],
    [3, 5, 6],
    [3, 4, 7],
    [3, 4],
    [5, 6, 7],
    [1, 5, 8],
    [1, 9]
]
vis = [False] * 9

dfs(graph, 1, vis)