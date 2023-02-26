from dataclasses import dataclass


@dataclass
class MyData:
    id: int
    name: str
    is_active: bool
    other: str


def update_data(
        data: MyData,
        update_param: str,
        new_data: str | bool):
    if hasattr(data, update_param):
        data.__setattr__(update_param, new_data)
    else:
        print("Нет такого параметра")


if __name__ == '__main__':
    my_data = MyData(
        id=123,
        name="Dima",
        is_active=True,
        other="bla-bla"
    )
    print(my_data.__dict__)
    update_data(my_data, "is_active", False)
    print(my_data.__dict__)
