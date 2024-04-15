# 상속 (유전자 전달)
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

    def show_class_info(self):
        print('show_class_info:', self.brand_name)


# 서브 클래스 생성 (pass 사용)
class PassSubBrand(Brand):
    pass


# 서브 클래스 생성 (__init__ 사용)
class LexusProducts(Brand):
    # 디폴트 생성자 호출
    def __init__(self, brand_name, model_type, model_name, model_price):
        # 여기에 서브클래스 속성 초기화 해도됨. 부모에다가 해도됨
        self.model_type = model_type
        self.model_name = model_name
        self.model_price = model_price
        Brand.__init__(self, brand_name)


class ToyotaProducts(Brand):
    def __init__(self, brand_name, model_name): # 1. 여기서 부모한테 받은 유전자를
        super().__init__(brand_name)    # 2. super 키워드로 생성자 함수로 전달
        # 자식 클래스에서 새로 받은 속성을 부모 생성자 내부에서 초기화 해도 됨
        self.model_name = model_name


# 슈퍼 클래스 객체 생성 (Brand)
print('\n슈퍼 클래스 객체 생성 (Brand)')
brand = Brand('Lexus')
print('car.name:', brand.brand_name)
brand.show_class_info()

# 서브 클래스 객체 생성 (PassCar)
print('\n서브 클래스 객체 생성 (PassCar)')
pass_car = PassSubBrand('Toyota')
print('pass_car.brand_name:', pass_car.brand_name)
pass_car.show_class_info()

# 서브 클래스 객체 생성 (LexusProducts)
print('\n서브 클래스 객체 생성 (LexusProducts)')
lexus_product = LexusProducts('Lexus', 'SUV', 'RX450', 10900)
print(lexus_product)    # 객체만 호출하면 메모리주소 출력함
print('Brand(super): ', lexus_product.brand_name)
print('Type(sub):', lexus_product.model_type)
print('Name(sub):', lexus_product.model_name)
print('prince(sub):', lexus_product.model_price)
lexus_product.show_class_info()

# 서브 클래스 객체 생성 (ToyotaProducts)
print('\n서브 클래스 객체 생성 (ToyotaProducts)')
toyota_p = ToyotaProducts('Toyota', 'crown')
print('Brand(super):', toyota_p.brand_name)
print('Name(sub):', toyota_p.model_name)
toyota_p.show_class_info()