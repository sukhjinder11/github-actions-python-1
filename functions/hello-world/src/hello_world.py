
class Greetings:
    def __init__(self):
        print('initializing class')

    @staticmethod
    def hello_world():
        return "hello world"

    @staticmethod
    def goodbye():
        return "goodbye!"


def handler():
    greet_obj = Greetings()
    greet_obj.hello_world()
    greet_obj.goodbye()


if __name__ == "__main__":
    handler()

