def setGraph(nCount, edges):
    """
    Fastest method to set graph
    returns graph
    :param: nCount number of nodes in graph - n nodes
    :param: edges list of edges in graph
    """
    # setting the nodes
    g=dict()

    for _t,_e in edges:
        if _t not in g.keys():
            g[_t]=[_e]
        else:
            g[_t].append(_e)
        if _e not in g.keys():
            g[_e]=[_t]
        else:
            g[_e].append(_t)
    
    g.update({k:[] for k in range(1,nCount+1) if k not in g.keys()})
    
    return g
