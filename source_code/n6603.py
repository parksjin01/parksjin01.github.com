import sys

n = 7
arr = ['1', '2', '3', '4', '5', '6', '7']
tmp = []

def permutation(idx, cnt):
    if cnt == 6:
        sys.stdout.write(' '.join(tmp)+'\n')
        return 0

    if idx == n:
        return 0

    tmp.append(arr[idx])
    permutation(idx+1, cnt+1)
    tmp.pop()
    permutation(idx+1, cnt)

# permutation(0, 0)

while True:
    value = raw_input().split(' ')
    # print value
    if value[0] == '0':
        break
    n, arr = int(value[0]), value[1:]
    permutation(0, 0)
    print
