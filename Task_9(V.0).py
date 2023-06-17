class CustomException1(BaseException):
    pass
class CustomException2(BaseException):
    pass
class CustomException3(BaseException):
    pass
class MyClass:
    def __init__(self, value):
        self.value = value
    def method1(self):
        if self.value < 0:
            raise CustomException1("Value should be greater than 0")
        return self.value
    def method2(self):
        if self.value > 100:
            raise CustomException2("Value should be less than or equal to 100")
        return self.value * 2
    def method3(self):
        if self.value % 2 != 0:
            raise CustomException3("Value should be even")
        return self.value / 2
class ExceptionHandler:
    def __init__(self, obj):
        self.obj = obj
    def handle_exceptions(self):
        try:
            print(self.obj.method1())
            print(self.obj.method2())
            print(self.obj.method3())
        except CustomException1 as e:
            print(f"Error: {e}")
        except CustomException2 as e:
            print(f"Error: {e}")
        except CustomException3 as e:
            print(f"Error: {e}")
        except Exception as e:
            print("Unknown error occurred")
            print(e)
obj = MyClass(-5)
handler = ExceptionHandler(obj)
handler.handle_exceptions()
