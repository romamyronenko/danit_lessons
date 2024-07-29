from dataclasses import dataclass


@dataclass
class Base:
    @classmethod
    def create(cls, data) -> "Base":
        annotations = cls.__annotations__
        params = {}
        for field, type_ in annotations.items():
            if Base in type_.mro():
                params[field] = type_.create(data.get(field))
            else:
                params[field] = data.get(field)
        return cls(**params)


@dataclass
class Coord(Base):
    lon: float
    lat: float


@dataclass
class Weather(Base):
    id: int
    main: str
    description: str
    icon: str


@dataclass
class Wind(Base):
    speed: float
    deg: int
    gust: float


@dataclass
class Rain(Base):
    value_1h: float


@dataclass
class Clouds(Base):
    all: float


@dataclass
class Sys(Base):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int


@dataclass
class Main(Base):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: float
    humidity: float
    sea_level: float
    grnd_level: float


@dataclass
class OpenWeatherData(Base):
    coord: Coord
    weather: list[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    rain: Rain
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
