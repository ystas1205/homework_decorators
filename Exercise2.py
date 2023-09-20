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
            data_logger = inspect.getargvalues(inspect.currentframe())
            print(data_logger)
            with open(r"logger file.txt", 'w') as file:
                file.write(
                    f"Время вызова функции: {data_logger[3]['call_date']}" +
                    '\n')
                file.write(
                    f"Имя функции: {data_logger[3]['anny_function'].__name__}"
                    + '\n')
                file.write(f"Аргументы: {data_logger[3]['args']}" + '\n')
                file.write(
                    f"Возвращаемое значение: {data_logger[3]['path']}" + '\n')
            return data

        return wrapper

    return function


@template(params='logger.txt')
def foo():
    return inspect.getargvalues(inspect.currentframe().f_back)


if __name__ == "__main__":
    foo()
