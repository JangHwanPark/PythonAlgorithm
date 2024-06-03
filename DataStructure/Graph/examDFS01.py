def dfs(graph, start):
    # 기본적으로 두개의 리스트를 별도로 관리(pair)
    need_vis, vis = list(), list()

    # 시작 노드 설정
    need_vis.append(start)

    # 방문해야할 노드가 있다면 루프 실행
    while need_vis:
        # 스택을 활용해 가장 마지막 데이터 추출
        node = need_vis.pop()

        # 만약 노드가 방문한 목록에 없으면?
        if node not in vis:
            # 방문한 목록에 추가
            vis.append(node)

            # 추가된 노드에 연결된 노드들
            need_vis.extend(graph[node])
    return vis


graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs(graph, 'A'))
print(dfs(graph, 'B'))