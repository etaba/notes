import sys, os

ARRANGEMENTS = {
    #L
    "L":[
        [(0,0),(0,1),(0,2),(1,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(1,0),(1,-1),(1,-2)],
        [(0,0),(1,0),(2,0),(2,1)],
        ]
    ,
    "R":[
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(1,0),(2,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(2,0),(2,-1)],
        ]
    ,
    "S":[
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(1,-1)],
        ]
    ,
    "2":[
        [(0,0),(1,0),(1,-1),(2,-1)],
        [(0,0),(0,1),(1,1),(1,2)],
        ]
    ,
    "I":[
        [(0,y) for y in range(4)],
        [(x,0) for x in range(4)]
    ],
    "T":[
        [(0,0),(1,0),(2,0),(1,-1)],
        [(0,0),(1,0),(1,1),(1,-1)],
        [(0,0),(1,0),(2,0),(1,1)],
        [(0,0),(0,1),(0,2),(1,1)],
    ],
    "O":[
        [(x, y) for x in range(2) for y in range(2)]
    ]}



def solve(pieces, grid):
    if len(pieces) == 0:
        #base case
        return []
    for piece in pieces:
        for p in ARRANGEMENTS[piece]:
            #place piece
            fits = True
            placed = []
            for coor in p:
                placement = (coor[0]+grid[0][0],coor[1]+grid[0][1])
                if placement not in grid:
                    fits = False
                    break
                placed.append(placement)
            if fits:
                remainingGrid = [c for c in grid if c not in placed]
                i = pieces.find(piece)
                remainingPieces = pieces[:i]+pieces[i+1:]
                remainingPlacements = solve(remainingPieces,remainingGrid)
                if remainingPlacements != None:
                    return [(piece,placed)] + remainingPlacements
    return None

def render(pieces,grid_x,grid_y):
    grid = [["*" for _ in range(int(grid_x))] for _ in range(int(grid_y))]
    for p in pieces:
        for x,y in p[1]:
            grid[y][x] = p[0]
    grid.reverse()
    for row in grid:
        print("".join(row))

if len(sys.argv) < 3:
    print("\nUSAGE: python talosTetrisSolver.py <grid_length x> <grid_length_y> <pieces>\n \
            EXAMPLE: python talosTetrisSolver.py 4 6 LROTS2I \n \
            PIECES: \n \
            L-Piece -> 'L'\n \
            Reverse L-Piece -> 'R'\n \
            Square Piece -> 'O'\n \
            T-Piece -> 'T'\n \
            S-Piece -> 'S'\n \
            Reverse S-Piece -> '2'\n \
            Bar Piece -> 'I'")
else:
    grid_x = sys.argv[1]
    grid_y = sys.argv[2]
    grid = [(x, y) for x in range(int(grid_x)) for y in range(int(grid_y)) ]
    pieces = sys.argv[3]

    solution = solve(pieces,grid)
    render(solution,grid_x,grid_y)


    
