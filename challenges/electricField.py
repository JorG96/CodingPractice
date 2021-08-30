'''
Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

It's been several weeks, and Ratiorg already feels how much stronger he has become. However, Ratiorg is about to face his first really exciting challenge: the Electric Field. It works like this: the bot stays in the top left corner of a rectangular grid. In one move he can walk to one of the nearest cells (directly above, below, to the left or to the right of his current position). Ratiorg's goal is to get to the bottom right corner in the least possible number of moves. However, it's not as simple as it seems: there are electric wires running through the grid. If Ratiorg steps on a wire, his microchips will be burnt to a crisp, so Ratiorg, prudent bot that he is, wants to do his best to avoid them.

You want to give Ratiorg a hint by telling him the least possible number of moves required to get to the destination. Given the grid and the wires, return the minimum number of moves required to get to the bottom right corner from the top left corner. If it's not possible to get there, return -1 instead.

Example

For grid = [4, 8] and

wires = [[1, 0, 1, 3], [3, 1, 3, 2], [4, 1, 4, 3], [4, 2, 4, 4],
         [1, 3, 3, 3], [2, 1, 7, 1], [2, 2, 7, 2], [5, 3, 8, 3]]
the output should be
electricField(grid, wires) = 26.
'''

def electricField(s, w):
    b = range
    r, t = s

    p = q = {(0, 0)}
    c = 0
    while q:        
        if (r-1, t-1) in q:
            return c
        p |= q
        q = {n for i, o in q for n in (
            (i + d, o + a)
            for d, a in ([0, 1], [0, -1], [1, 0], [-1, 0])
            if i + d in b(r) and o + a in b(t)
                and not any(
                    d and x == 1+ i + d//2 and o in b(z, c)
                    or a and z == 1 + o + a//2 and i in b(x, v)
                    for z,x,c,v in ([min(a, c), min(b, d), max(a, c), max(b, d)] for a, b, c, d in w)
                        )
        ) if n not in p}
        c += 1
    return -1