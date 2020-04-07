# coding = utf-8
class MyTestWith:
    def __enter__(self):
        print("__enter__ called")
        return self

    def dosomething(self):
        x = 1/0
        print("do some thing")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit called1")
        print("type(exc_type)")
        print(type(exc_type))
        print("type(exc_val)")
        print(type(exc_val))
        print("type(exc_tb)")
        print(type(exc_tb))
        print("__exit called2")

with MyTestWith() as sample:
    sample.dosomething()
