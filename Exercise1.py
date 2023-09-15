import datetime
from functools import wraps
import inspect
import requests


def function(anny_function):
    @wraps(anny_function)
    def wrapper(*args, **kwargs):
        call_date = str(datetime.datetime.today())
        data = anny_function(*args, **kwargs)
        return data

    return wrapper


@function
def get_swapi_person(person_id):
    return (requests.get(f'https://swapi.dev/api/people/{person_id}').json(),
            inspect.getargvalues(inspect.currentframe().f_back))


def file_recording(result):
    with open(r"logger.txt", 'w') as file:
        file.write(f"Время вызова функции: {result[1][3]['call_date']}" + '\n')
        file.write(
            f"Имя функции: {result[1][3]['anny_function'].__name__}" + '\n')
        file.write(f"Аргументы: {(result[1][3]['args'])}" + '\n')
        file.write(f"Возвращаемое значение: {result[0]}" + '\n')


if __name__ == "__main__":
    file_recording(get_swapi_person(1))

