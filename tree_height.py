import sys
import threading
import numpy
def compute_height(n, parents):
    # Create a list to store the height of each node in the tree
    heights = [0] * n

    # Find the height of each node in the tree
    for i in range(n):
        
        if heights[i] != 0:
            continue

        # Traverse up the tree until we find the root node
        height = 0
        node = i
        while node != -1:
      
            if heights[node] != 0:
                height += heights[node]
                break

            # Otherwise, we need to continue traversing up the tree
            height += 1
            node = parents[node]

        # Store the height of the current node
        heights[i] = height

    # Find the maximum height in the tree
    max_height = max(heights)

    return max_height

def main():
 
    user_input = input().strip().split('\\r\\n')
    if user_input[0] == "F":
        filename = "test/" + user_input[1]
        with open(filename) as f:
            n = int(f.readline())
            parents = numpy.array(f.readline().split(), dtype=int)
    elif user_input[0] == "I":
        n = int(user_input[1])
        parents = numpy.array(user_input[2].split(), dtype=int)
    else:
        return  # exit if input format is incorrect

    # compute the height of the tree
    height = compute_height(n, parents)


    print(height)

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
