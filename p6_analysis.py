from p6_game import Simulator

ANALYSIS = {}

def analyze(design):
    sim = Simulator(design)
    queue = []
    visited = []
    
    state = sim.get_initial_state()
    
    queue.append((state, [state]))
    visited.append(state)
    
    while queue:
        (prevstate, path) = queue.pop(0)
        for next in sim.get_moves():
            newstate = sim.get_next_state(prevstate, next)
            if (newstate is not None and newstate not in ANALYSIS):
                if newstate not in visited:
                    ANALYSIS[newstate] = path
                    queue.append((newstate, path + [newstate]))
                    visited.append(newstate)
                print newstate
    
    # TODO: fill in this function, populating the ANALYSIS dict

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    found = False
    for next in ANALYSIS.keys():
        #print next[0]
        #print (i,j)
        if i is next[0][0] and j is next[0][1]:
            pos, abil = next
            path = ANALYSIS[next]
            for n in range(len(path) - 1):
                found = True
                draw_line(path[n][0], path[n+1][0], color_obj=path[n][1])
            draw_line(path[-1][0], (i,j), color_obj=path[-1][1])
            break
    if not found:
        print "Nothing found"