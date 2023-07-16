# Rev Lab 3: 迷宫问题

逆向分析的过程虽然是较为枯燥甚至是让人头大的，但从一团乱麻毫无头绪到“复行数十步，豁然开朗”这一过程又何尝不让人神往。希望大家在本课程的逆向部分都能有所收获，体会到拆解程序的乐趣。

本节 Lab 是逆向专题的最后一次作业，内容较为轻松，希望大家玩得愉快。

## はちみ (100 points)

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/rev-lab3/attachment.tar.gz)

はちみを舐めると～ 蜂巢里有好多蜂蜜，完成题目并提交：

1. flag 内容及 Writeup (100 points)

## Reference

课上给大家演示了如何用 gdb script 与 frida 解迷宫类题目，这里附上代码：

### gdb script

[gdb_script.py](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/rev-lab3/gdb_script.py)

```python
#!/usr/bin/env python3
import re

GRID_SIZE = 4
HEIGHT = 9
WIDTH = 9
MAZE_SIZE = HEIGHT * WIDTH

# initialize
gdb.execute("file level2")
gdb.execute("set confirm off")
gdb.execute("set pagination off") # set height unlimited (--batch)
gdb.execute("starti")
gdb.execute("pie b 0x156B") # first function malloc
gdb.execute("pie b 0x1BED") # first function memset

commands = "continue\n"
commands += "ni\n"
commands += "p $rax\n"
commands += "continue\n"
commands += "x/%dbx $1" % (MAZE_SIZE * GRID_SIZE)

data = []
for cmd in commands.split('\n'):
    if cmd.startswith("x/"):
        r = gdb.execute(cmd, to_string=True)
        for item in re.findall(r"(0x[0-9a-f]{2})[\t\n]", r):
            data.append(int(item, 16))
    else:
        gdb.execute(cmd)

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
```

### frida

使用命令 `pip install frida-tools` 安装依赖，执行 `sudo sysctl kernel.yama.ptrace_scope=0` 允许对 non-child 进程 ptrace：

[frida_script.py](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/rev-lab3/frida_script.py)

```python
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
```

[frida_hook_script.js](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/rev-lab3/frida_hook_script.js)

```javascript
console.log('Frida script has been loaded successfully.');

const MAZE_SIZE = 9 * 9;
const GRID_SIZE = 4;

var malloc_cnt = 0;
var puts_cnt = 0;
var map_address;

Interceptor.attach(Module.findExportByName(null, 'malloc'), {
    // When entering malloc, print its argument as an integer to the console.
    onEnter: function (args) {
        // console.log("malloc(" + args[0].toInt32() + ")");
    },

    // When returning from malloc, print the return value (pointer) as a hexadecimal string.
    onLeave: function (retval) {
		if (malloc_cnt == 0) {
            map_address = '0x' + retval.toString(16);
			console.log("\nMap address -> " + map_address);
		}
		malloc_cnt += 1;
    }
});

Interceptor.attach(Module.findExportByName(null, 'puts'), {
    // When entering malloc, print its argument as an integer to the console.
    onEnter: function (args) {
        if (puts_cnt == 0) {
            // console.log(ptr(map_address).toString(16));
            send(map_address, ptr(map_address).readByteArray(MAZE_SIZE * GRID_SIZE));
        }
        puts_cnt += 1;
    }
});
```