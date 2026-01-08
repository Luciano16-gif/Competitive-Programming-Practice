import sys
from collections import deque
from array import array

def main():
    n: int = int(input())

    total = n * n
    dist = array('i', [-1]) * total  
    dist[0] = 0

    moves = ((2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1))

    q = deque([0])
    append = q.append
    popleft = q.popleft
    nn = n
    dists = dist

    while q:
        idx = popleft()
        r, c = divmod(idx, nn)
        nd = dists[idx] + 1

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < nn and 0 <= nc < nn:
                nidx = nr * nn + nc
                if dists[nidx] == -1:
                    dists[nidx] = nd
                    append(nidx)

    out_lines = []
    for r in range(nn):
        off = r * nn
        out_lines.append(' '.join(str(dists[off + c]) for c in range(nn)))
    print('\n'.join(out_lines))

if __name__ == "__main__":
    main()
