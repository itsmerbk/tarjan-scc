def tarjan_scc(graph):
    idx, indices, low, stack, on_stack, sccs = 0, {}, {}, [], set(), []
    def dfs(u):
        nonlocal idx
        indices[u] = low[u] = idx; idx += 1; stack.append(u); on_stack.add(u)
        for v in graph.get(u, []):
            if v not in indices: dfs(v); low[u] = min(low[u], low[v])
            elif v in on_stack: low[u] = min(low[u], indices[v])
        if low[u] == indices[u]:
            comp = []
            while True:
                w = stack.pop(); on_stack.remove(w); comp.append(w)
                if w == u: break
            sccs.append(comp)
    for node in graph:
        if node not in indices: dfs(node)
    return sccs

if __name__ == "__main__":
    g = {0: [1], 1: [2], 2: [0, 3], 3: []}
    assert len(tarjan_scc(g)) == 2
    print("[PASS] 015_tarjan_scc")
