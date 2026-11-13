# 클로저(Closure) 데코레이터(Decorator)

# 클로저 : 내부 함수가 자신이 정의된 이부 함수의 변수들을 기억하고, 외부
'''
print('=== 1단계: 함수 안에 함수 만들기 ===')
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print('inner 함수가 실행되었습니다.')

    return  inner


func = outer()
func()

print('\n===2단계: 클로저 ===')
# 
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역함수

    def multiplier(n):
        # 내부 함수 multipier는
        # 바깥 함수의 변수 x를 사용할 수 있다.
        return x * n

    return multiplier

times3 = make_multiplier(3)
print(times3(10))
print(times3(5))

print('\n=== 3단계: 데코레이터 기본 구조 ===')

# 데코레이터는 '함수를 꾸며주는 함수'
# 내부 구조는 클로저와 매우 유사

def decorator(func):
    # fune는 꾸며줄 함수

    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')

    return wrapper

def say_hello():
    print('안녕하세요')

decorated = decorator(say_hello)
decorated()

print('\n=== 4단계: 매개변수가 있는 데코레이터 ===')

def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')

    return wrapper
'''
