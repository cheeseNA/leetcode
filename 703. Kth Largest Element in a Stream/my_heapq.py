class MyHeap:
    def __init__(self):
        self.heap = []
        return

    def __len__(self):
        return len(self.heap)

    def _get_parent_index(self, index: int):
        return (index - 1) // 2

    def _has_parent(self, index: int):
        return index > 0

    def _has_right_child(self, index: int):
        return index * 2 + 2 < len(self.heap)

    def _has_left_child(self, index: int):
        return index * 2 + 1 < len(self.heap)

    def _get_smaller_child_index(self, index: int):
        if self._has_right_child(index):
            right_child_index = index * 2 + 2
            left_child_index = index * 2 + 1
            if self.heap[right_child_index] < self.heap[left_child_index]:
                return right_child_index
            return left_child_index
        elif self._has_left_child(index):
            return index * 2 + 1
        else:
            return None

    def is_empty(self):
        return not self.heap

    def push(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while self._has_parent(index):
            parent_index = self._get_parent_index(index)
            if self.heap[parent_index] <= self.heap[index]:
                break
            smaller_child_index = self._get_smaller_child_index(parent_index)
            self._swap(parent_index, smaller_child_index)
            index = parent_index
        return

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        return

    def pop(self):
        if self.is_empty():
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        index = 0
        while self._has_left_child(index):
            smaller_child_index = self._get_smaller_child_index(index)
            if self.heap[smaller_child_index] >= self.heap[index]:
                break
            self._swap(index, smaller_child_index)
            index = smaller_child_index
        return min_value

    def top(self):
        if self.is_empty():
            return None
        return self.heap[0]
