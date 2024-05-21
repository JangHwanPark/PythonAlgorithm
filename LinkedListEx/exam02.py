# 뒤로가기 앞으로가기 (브라우저)
# 음악 플레이어 재생목록

# Linked List
class Node:
    # 생성자 - 파이썬 에서 None = null 인듯
    def __init__(self, data):
        self.data = data
        self.next = None


# SLL : Singly Linked List
class SLL:
    # 생성자
    def __init__(self):
        self.head = None

    # 맨 앞에 노드 삽입 - O(1)
    def insert_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # 맨 뒤에 노드 삽입 - O(n)
    def insert_back(self, data):
        node = Node(data)
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    # n번째 노드 탐색 - O(n)
    def find_node(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return current_node

            current_node = current_node.next
        raise RuntimeError('노드가 존재하지 않습니다.')

    # 특정 노드의 뒤에 삽입 - O(1)
    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    # 특정 노드의 뒤에 삭제 - O(1)
    def delete_after(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next
