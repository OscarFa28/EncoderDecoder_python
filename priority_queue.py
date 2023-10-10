import math

class HeapNode:
    def __init__(self, key, value=None):
        self.key = key          # Node key
        self.value = value      # Value associated with the node (optional)

class Heap:
    def __init__(self):
        self.heap = []           # Initialize the list that will contain the heap
        self.size = 0            # Initialize the size of the heap
    
    def parent(self, idx):
        return idx // 2          # Calculate the index of a node's parent

    def left_child(self, idx):
        return idx * 2          # Calculate the index of a node's left child
    
    def right_child(self, idx):
        return idx * 2 + 1      # Calculate the index of a node's right child
    
    def heapify(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        largest_idx = idx

        # Compare the node with its children and find the index of the largest one
        if left_idx <= self.size and self.heap[left_idx].key > self.heap[idx].key:
            largest_idx = left_idx

        if right_idx <= self.size and self.heap[right_idx].key > self.heap[largest_idx].key:
            largest_idx = right_idx

        if largest_idx != idx:
            # Swap the current node with the largest node
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            self.heapify(largest_idx)

    def build_heap(self, elements):
        self.heap = elements
        self.size = len(elements)
        self.heap.insert(0, HeapNode(-math.inf))  # Insert an "infinite" node at position 0

        # Apply heapify to nodes from the middle backward to build the heap
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)
    
    def heap_max(self):
        if self.size == 0:
            return None  # The heap is empty
        return self.heap[1]  # Return the node with the maximum value

    def heap_extract_max(self):
        if self.size == 0:
            return None  # The heap is empty

        max_node = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)  # Restore the heap property

        return max_node
        
    def heap_increase_key(self, index, value):
        if value <= self.heap[index].key:
            return None  # The new key is not greater than the current one

        self.heap[index].key = value

        while index > 1:
            parent = self.parent(index)

            if self.heap[index].key > self.heap[parent].key:
                # Swap the node with its parent if the key is greater
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def heap_insert(self, value):
        if self.size >= len(self.heap) - 1:
            self.heap.append(HeapNode(-math.inf, value))
        else:
            self.size += 1
            self.heap[self.size] = HeapNode(-math.inf, value)

        self.heap_increase_key(self.size, value)

    def get_size(self):
        return self.size

    def print_heap(self):
        for node in self.heap[1:]:
            print("Key:", node.key, "Value:", node.value)
