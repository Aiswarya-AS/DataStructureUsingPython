def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []


def add_edges(v1, v2):
    # def add_edges(v1,v2,cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        # list1=[v2,cost]
        # list2=[v1,cost]
        # graph[v1].append(list1)
        # graph[v2].append(list2)
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)


def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


def DFS(node, graph):
    visited = set()
    if node not in graph:
        print("The node not in graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, "-->", end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


def BFS(node, graph):
    visited = set()
    if node not in graph:
        print("The node not in graph")
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, "-->", end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)


graph = {}


add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edges("A", "B")
add_edges("A", "C")
add_edges("C", "D")
add_edges("D", "E")
print(graph)


# delete_node('A')
# delete_edge('A','B')
print(graph)
DFS("A", graph)
print()
BFS("A", graph)
