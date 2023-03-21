import sys
import threading

def compute_height(n, parents):

    heights = [0] * n


    for i in range(n):

        if heights[i] != 0:
            continue


        height = 0
        node = i
        while node != -1:

            if heights[node] != 0:
                height += heights[node]
                break

            height += 1
            node = parents[node]

        heights[i] = height


    max_height = max(heights)

    return max_height

def main():

    n = int(input())
    parents = list(map(int, input().split()))


    height = compute_height(n, parents)


    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
