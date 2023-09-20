import datetime
from functools import wraps
import inspect
import requests


def function(anny_function):
    @wraps(anny_function)
    def wrapper(*args, **kwargs):
        call_date = str(datetime.datetime.today())
        data = anny_function(*args, **kwargs)
        data_logger = inspect.getargvalues(inspect.currentframe())
        with open(r"logger.txt", 'w') as file:
            file.write(
                f"Время вызова функции: {data_logger[3]['call_date']}" + '\n')
            file.write(
                f"Имя функции: {data_logger[3]['anny_function'].__name__}"
                + '\n')
            file.write(f"Аргументы: {data_logger[3]['args']}" + '\n')
            file.write(
                f"Возвращаемое значение: {data_logger[3]['data']}" + '\n')
            return data

    return wrapper


@function
def get_swapi_person(person_id):
    return requests.get(f'https://swapi.dev/api/people/{person_id}').json()


if __name__ == "__main__":
    get_swapi_person(1)
