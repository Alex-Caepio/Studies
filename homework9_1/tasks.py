from dataclasses import dataclass, field
from datetime import datetime


class WeatherForecastMeta(type):
    def __new__(cls, name, bases, attrs):
        if "create_forecast" in attrs and "date" not in attrs:
            attrs["date"] = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
        return super().__new__(cls, name, bases, attrs)


@dataclass
class WeatherForecast(metaclass=WeatherForecastMeta):
    temperature: float
    humidity: int
    description: str
    date: str

    @staticmethod
    def is_cold(temperature):
        return temperature < 10

    @classmethod
    def create_forecast(cls, temperature, humidity, description):
        return cls(temperature, humidity, description)


weather_forecast = WeatherForecast.create_forecast(
    temperature=10,
    humidity=20,
    description="Ясно"
)
print(weather_forecast)
