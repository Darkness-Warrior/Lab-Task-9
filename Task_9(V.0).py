class Cla(BaseException):
    pass


class Clas(BaseException):
    pass


class Class(BaseException):
    pass


class MyClass:
    def __init__(self, value):
        self.value = value

    def method1(self):
        if self.value <= 0:
            raise Cla("Значение должно быть больше 0")
        return self.value

    def method2(self):
        if self.value > 100:
            raise Clas("Значение должно быть меньше или равно 100")
        return self.value * 2

    def method3(self):
        if self.value % 2 != 0:
            raise Class("Значение должно быть четным")
        return self.value / 2


class ExceptionHandler:
    def __init__(self, obj):
        self.obj = obj

    def handle_exceptions(self):
        try:
            print(self.obj.method1())
            print(self.obj.method2())
            print(self.obj.method3())
        except Cla as e:
            print(f"Error: {e}")
        except Clas as e:
            print(f"Error: {e}")
        except Class as e:
            print(f"Error: {e}")
        except Exception as e:
            print("Unknown error occurred")
            print(e)


obj = MyClass(10)    # Правильный вывод
handler = ExceptionHandler(obj)
handler.handle_exceptions()

obj = MyClass(0)
handler = ExceptionHandler(obj)
handler.handle_exceptions()

obj = MyClass(150)
handler = ExceptionHandler(obj)
handler.handle_exceptions()

obj = MyClass(3)
handler = ExceptionHandler(obj)
handler.handle_exceptions()
