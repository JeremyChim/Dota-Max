def try_decorator(func):
    """
    :param func: 需要try运行的函数
    :return: 封装函数，报错会打印
    """

    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except Exception as e:
            print(e)

    return wrapper


if __name__ == '__main__':
    @try_decorator
    def say_hi(name: str):
        print(f'say hi. {name}')


    say_hi('Jeremy')
    say_hi('Jeremy', 'Max')
    say_hi()
