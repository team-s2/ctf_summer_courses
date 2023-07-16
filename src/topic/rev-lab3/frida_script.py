#!/usr/bin/env python

import frida
import sys

# Spawn and attach to process
pid = frida.spawn('./level2')
session = frida.attach(pid)

# Create and load the instrumentation script
script = session.create_script(open('./frida_hook_script.js', 'r').read())

def solve_maze(data):
    GRID_SIZE = 4
    HEIGHT = 9
    WIDTH = 9
    
    ascii_maze = [['+' for _ in range(WIDTH * 4 + 1)] for _ in range(HEIGHT * 2 + 1)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            idx = (i * WIDTH + j) * GRID_SIZE
            grid = data[idx: idx + 4]
            ascii_maze[i * 2 + 1][j * 4 + 1:(j + 1) * 4] = [' '] * 3
            
            # up wall
            if grid[0] == 0:
                ascii_maze[i * 2][j * 4 + 1:(j + 1) * 4] = ['-'] * 3
            else:
                ascii_maze[i * 2][j * 4 + 1:(j + 1) * 4] = [' '] * 3
            
            # down wall
            if grid[1] == 0:
                ascii_maze[(i + 1) * 2][j * 4 + 1:(j + 1) * 4] = ['-'] * 3
            else:
                ascii_maze[(i + 1) * 2][j * 4 + 1:(j + 1) * 4] = [' '] * 3
                
            # left wall
            if grid[2] == 0:
                ascii_maze[i * 2 + 1][j * 4] = '|'
            else:
                ascii_maze[i * 2 + 1][j * 4] = ' '
            
            # right wall
            if grid[3] == 0:
                ascii_maze[i * 2 + 1][(j + 1) * 4] = '|'
            else:
                ascii_maze[i * 2 + 1][(j + 1) * 4] = ' '

    print(' Map '.center(WIDTH * 4 + 1, '='), end='\n\n')
    for line in ascii_maze:
        print(''.join(line))

    # depth first search
    path = []
    stack = [(0, 0)]
    steps = ['w', 's', 'a', 'd']
    dires = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    record = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    while(len(stack) > 0):
        cur = stack.pop()
        if cur == (HEIGHT - 1, WIDTH - 1):
            break
        record[cur[0]][cur[1]] = 1 # visited
        
        all_visited = True
        for i in range(4):
            idx = (cur[0] * WIDTH + cur[1]) * GRID_SIZE
            nx = cur[0] + dires[i][0]
            ny = cur[1] + dires[i][1]
            if data[idx + i] == 1 and record[nx][ny] == 0:
                all_visited = False
                path.append(steps[i])
                stack.append(cur)
                stack.append((nx, ny))
                break
        
        if all_visited:
            path.pop()
    
    print("\nPath:", ''.join(path))

def on_message(message, data):
    if data != None:
        data = bytearray(data)
        solve_maze(data)

if __name__ == '__main__':
    try:
        script.on('message', on_message)
        script.load()
        frida.resume(pid)
        sys.stdin.read()
    except KeyboardInterrupt:
        print('[+] Frida script exit by user')
        frida.kill(pid)
        sys.exit(0)
    except Exception as e:
        print('[-] Error', e)
        frida.kill(pid)
        sys.exit(1)