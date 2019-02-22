import sys
num_steps = int(sys.argv[1])
step = ""
i = 0
n = num_steps
while num_steps > i:
    n -= 1
    i += 1
    step += "#"
    print(" " * n + step)
