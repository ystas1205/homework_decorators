import os
import inspect
from functools import wraps
import datetime



def template(params):
    def function(anny_function):
        @wraps(anny_function)
        def wrapper(*args, **kwargs):
            call_date = str(datetime.datetime.today())
            path = os.path.abspath(params)
            data = anny_function(*args, **kwargs)
            return data

        return wrapper

    return function


@template(params='logger.txt')
def foo():
    return inspect.getargvalues(inspect.currentframe().f_back)


def file_recording(result):
    with open(r"logger file.txt", 'w') as file:
        file.write(f"Время вызова функции: {result[3]['call_date']}" + '\n')
        file.write(
             f"Имя функции: {result[3]['anny_function'].__name__}" + '\n')
        file.write(f"Аргументы: {(result[3]['args'])}" + '\n')
        file.write(f"Возвращаемое значение: {result[3]['path']}" + '\n')


if __name__ == "__main__":
    file_recording(foo())

