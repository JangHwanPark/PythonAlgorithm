# 클래스 생성 (data = 5 초기화)
class CreateClass:
    data = 5


# CreateClass 의 객체 생성
obj1 = CreateClass()
print('obj1.data: ', obj1.data)


# 클래스의 생성자를 이용한 값 초기화 (__init__())
# _init__()함수는 클래스를 사용하여 새 객체를 생성할 때마다 자동으로 호출
# def = oop 에서 메서드(함수)
# self = this
class ClassConstructor:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    # 객체를 문자열로 표현하고 싶으면 __str__ 사용
    def __str__(self):
        return f"{self.data}({self.next_node})"


# ClassConstructor 의 객체 생성
node = ClassConstructor(1)
print("list data: ", node.data)
print("list pointer: ", node.next_node)

str_node = ClassConstructor('Python')
print("list data: ", str_node.data)
print("list pointer: ", str_node.next_node)