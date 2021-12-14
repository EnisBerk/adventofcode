'''
tools for advent code day 12
'''


from numpy import isin


def load_data(text):
    '''
    load data from file
    '''
    data = text.strip().split('\n')
    data = [line.split('-') for line in data]
    return data


def load_graph(data):
    graph = {}
    for x,y in data:
        graph.setdefault(x,list())
        graph.setdefault(y,list())
        graph[x].append(y)
        graph[y].append(x)

    return graph

                    
def DFS_recursive(graph, start, visited,paths=None):
    '''
    depth first search
    '''
    if start =='end':
        return visited

    visited.append(start)
    
    if paths is None:
        paths = []
    for node in graph[start]:
        if node not in visited or not node.islower():
            out = ((DFS_recursive(graph, node, visited[:])))
            if out and isinstance(out[0],list):
                paths.extend(out)
            else:
                paths.append(out)
    paths = [path for path in paths if path]
    return paths

def DFS_while(graph,start,):
    '''
    depth first search
    '''
    paths=[]
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node=='end':
            paths.append(visited[:])
            visited  = ['start']
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

def DFS_recursive_part2(graph, start, visited,part):
    '''
    depth first search
    '''
    if start =='end':
        visited.append(start)
        return visited

    visited.append(start)
    paths = []
    for node in graph[start]:
        new_part = part
        if node =='start':
            continue
        if node in visited:
            if node.islower():
                if part==1:
                    print('1',node,','.join(visited+[node]))
                    continue
                else:
                    print('2',node,','.join(visited+[node]))
                    new_part=1

        out = DFS_recursive_part2(graph, node, visited[:],new_part)
        if out and isinstance(out[0],list):
            paths.extend(out)
        else:
            paths.append(out)
    paths = [path for path in paths if path]
    return paths

def part1(data):
    '''
    part 1
    '''
    data = load_data(data)
    graph = load_graph(data)
    paths = DFS_recursive(graph, 'start', list())

    return len(paths)
    


def part2(data):
    '''
    part 2
    '''
    data = load_data(data)
    graph = load_graph(data)
    paths = DFS_recursive_part2(graph, 'start', list(),2)
    all_str=[]
    for path in paths:
        l=(','.join(path))
        all_str.append(l)
    all_str.sort()
    for m in all_str:
        print(m)
    return len(paths)


