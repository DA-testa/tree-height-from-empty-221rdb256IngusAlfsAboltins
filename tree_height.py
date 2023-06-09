import sys
import threading
import numpy
import os
def compute_height(n, parents):
  
    heights = [0] * n
    for i in range(n):
 

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
  


    text= input().strip()
    if text[0] == "F":
        file_name = input()
        file_path = os.path.join('test', file_name)
        with open(file_path,'r') as f:
            n = int(f.readline())
            parents = numpy.array(f.readline().split(), dtype=int)
            
    elif text[0] == "I":
        n = int(input())
        parents = numpy.array(input().split(), dtype=int)
    else:
        return  

    height = compute_height(n, parents)

    print(height)

sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)   
threading.Thread(target=main).start()
