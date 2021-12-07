# import attr
from dataclasses import dataclass


# @attr.s
# class AttrCard:
#     rank = attr.ib()
#     suit = attr.ib()
#
#
# queen_of_hearts = AttrCard('Q', 'Hearts')
# print(queen_of_hearts.rank)


@dataclass
class DataClases:
    name: str
    value: int


test = DataClases('hello world', 1234)
print(test.name)
print(test.value)
print(type(test))


@dataclass
class Position:
    name: str
    lon: float
    lat: float


pos = Position('Oslo', 10.8, 59.9)
print(pos.lat)
print(pos.lon)
print(pos.name)
print(pos)
print(type(pos))
print(f'{pos.name} is at {pos.lat}N, {pos.lon}E')
