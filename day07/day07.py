import networkx as nx

input =[]
with open('input.txt') as f:
    input = f.readlines()

def solve(input):
    #G = nx.DiGraph([(s[1],s[7]) for s in map(str.split, input)])
    G = nx.DiGraph()
    for l in input:
        edge = l.split()
        G.add_edge(edge[1],edge[7])
    
    p1= ''.join(nx.lexicographical_topological_sort(G))
    
    #part2
    task_times=[]
    tasks=[]
    time=0
    while task_times or G.number_of_nodes() > 0:
        available_tasks = [t for t in G if t not in tasks and G.in_degree(t)==0]
        if available_tasks and len(task_times) < 5:
            task = min(available_tasks)
            task_times.append(ord(task) - 4)
            tasks.append(task)
        else:
            min_time = min(task_times)
            completed = [tasks[i] for i,v in enumerate(task_times) if v == min_time]
            task_times = [v - min_time for v in task_times if v > min_time]
            tasks = [t for t in tasks if t not in completed]
            time += min_time
            G.remove_nodes_from(completed)
    return [p1,time]        

print(solve(input))
#print(input)
