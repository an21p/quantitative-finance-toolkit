class Heap(object):
    def __init__(self, max=False):
        self.max = max
        if max:
            self.heapify_up = self.max_heapify_up
            self.heapify_down = self.max_heapify_down
        else:
            self.heapify_up = self.min_heapify_up
            self.heapify_down = self.min_heapify_down
        self.items = []

    @staticmethod
    def left_child_index(index):
        return 2 * index + 1

    @staticmethod
    def right_child_index(index):
        return 2 * index + 2

    @staticmethod
    def parent_index(index):
        return (index - 1) // 2

    def has_left_child(self, index):
        return self.left_child_index(index) < len(self.items)

    def has_right_child(self, index):
        return self.right_child_index(index) < len(self.items)

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.left_child_index(index)]

    def right_child(self, index):
        return self.items[self.right_child_index(index)]

    def parent(self, index):
        return self.items[self.parent_index(index)]

    def swap(self,idx1, idx2):
        self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]

    def peek(self):
        if not self.items:
            return None
        else:
            return self.items[0]

    def insert(self, key, value=None):
        self.items.append(key)
        self.heapify_up()

    def remove(self, key):
        top = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.heapify_down()
        return top

    def min_heapify_up(self):
        index = len(self.items) -1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def min_heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smallest_child_index = self.left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smallest_child_index = self.right_child_index(index)

            if self.items[index] < self.items[smallest_child_index]:
                break
            else:
                self.swap(index, smallest_child_index)
            index = smallest_child_index

    def max_heapify_up(self):
        index = len(self.items) - 1
        while self.has_parent(index) and self.parent(index) < self.items[index]:
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def max_heapify_down(self):
        index = 0
        while self.has_left_child(index):
            largest_child_index = self.left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                largest_child_index = self.right_child_index(index)

            if self.items[index] > self.items[largest_child_index]:
                break
            else:
                self.swap(index, largest_child_index)
            index = largest_child_index


if __name__ == "__main__":
    max_heap = Heap(max=True)
    max_heap.insert(3)
    max_heap.insert(4)
    max_heap.insert(9)
    max_heap.insert(5)
    max_heap.insert(2)
    print("Max-Heap array: " + str(max_heap.items))
    max_heap.remove(4)
    max_heap.remove(9)
    print(max_heap.peek())
    print("After deleting an element: " + str(max_heap.items))

    min_heap = Heap()
    min_heap.insert(3)
    min_heap.insert(4)
    min_heap.insert(9)
    min_heap.insert(5)
    min_heap.insert(2)
    print("Min-Heap array: " + str(min_heap.items))
    min_heap.remove(2)
    print(min_heap.peek())
    print("After deleting an element: " + str(min_heap.items))
