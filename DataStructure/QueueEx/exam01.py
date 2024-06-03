# QueueExam01 클래스 선언
class QueueExam01:
    # 생성자 선언
    def __init__(self):
        self.items = []

    # 큐가 비어있는지 확인
    def is_empty(self):
        return not self.items

    # 데이터를 큐에 추가
    def enqueue(self, data):
        self.items.append(data)

    # 데이터를 큐에서 삭제
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    # 큐 크기를 반환 (요소 개수)
    def size(self):
        return len(self.items)


# QueueExam01 클래스의 인스턴스 생성
queue = QueueExam01()
queue.enqueue('test1')
queue.enqueue('test2')
queue.enqueue('test3')

# 큐, 스택 선형인데 단방향이라 순회가 안됨
# 데이터 들어간거 빼면서 하나씩 출력 가능
# 결론은 내부에 있는 데이터 다 보려면 큐 내부에 데이터가 전부 없어짐 (비효율적)
print("Element:", queue.dequeue(), ", Size:", queue.size())
print("Element:", queue.dequeue(), ", Size:", queue.size())
print("Element:", queue.dequeue(), ", Size:", queue.size())
print("Empty:", queue.is_empty())

