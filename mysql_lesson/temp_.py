class Base:
    pass


class Weather(Base):
    pass


print(isinstance(Weather, Base))
print(Base in Weather.mro())
