from typing import Any

# jeito errado

fifo = []

fifo.append("A")
print(fifo)
fifo.append("B")
print(fifo)
fifo.pop(0)
print(fifo)
fifo.pop(0)
print(fifo)

# low level

# EMPYT_NODE_VALUE = '__EMPTY_NODE_VALUE__'


# class EmptyQueueError(Exception):
#     ...

# class Node:
#     def __init__(self, value: Any) -> None:
#         self.value = value
#         self.next = Node

#     def __repr__(self) -> str:
#         return f'{self.value}'


#     def __bool__(self) -> bool:
#         return bool(self.value != EMPYT_NODE_VALUE)


# class Queue:
#     def __init__(self) -> None:
#         self.first: Node = Node(EMPYT_NODE_VALUE)
#         self.last: Node = Node(EMPYT_NODE_VALUE)
#         self._count = 0

#     def push(self, node_value: Any) -> None:
#         new_node = Node(node_value)

#         if not self.first:
#             self.first - new_node

#         if not self.last:
#             self.last = new_node

#         else:
#             self.last.next = next_node
#             self.last = new_node

#     self._count += 1

    
#     def pop(self) -> None:
#         if not self.first:
#             raise EmptyQueueError('Empyt Queue')

#         first = self.first

#         if hasattr(self.first, 'next'):
#             self.first = self.first.next
#         else:
#             self.first = Node(EMPYT_NODE_VALUE)

#         self._count -= 1
#         return first


#     def peek(self) -> Node:
#         return self.first

    
#     def __len__(self) -> int:
#         return self._count

#     def __bool__(self) -> bool:
#         return bool(self._count)

#     def __iter__(self) -> Queue:
#         return self

#     def __next__(self) -> Any:
#         try:
#             next_value = self.pop()
#             return next_value
#         except EmptyQueueError:
#             raise StopIteration

#     def __repr__(self) -> str:
#         return f'Queue({self.first, self.last})'

# if __name__ == "__main__":
#     queue = Queue()
#     queue.push('A')
#     print(queue)
#     queue.push('B')
#     print(queue)

