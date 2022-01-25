# This is file for Exception Handling
class MyException(Exception):
    def __init__(self, value):
        self.value = value


# if __name__ == '__main__':
#     try:
#         raise (MyException("Excep"))
#     except MyException as e:
#         print(e)
#         e = str(e)
