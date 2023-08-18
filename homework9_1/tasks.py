from dataclasses import dataclass
from datetime import datetime


@dataclass
class WeatherForecast:
    date: str
    temperature: float
    humidity: int
    description: str

    @staticmethod
    def is_cold(temperature):
        return temperature < 10

    @classmethod
    def create_forecast(cls, date, temperature, humidity, description):
        return cls(date, temperature, humidity, description)

    @staticmethod
    def todays_date(self):
        return datetime.now().strftime("%Y-%m-%d")


weather_forecast = WeatherForecast.create_forecast(
    date=WeatherForecast.todays_date(WeatherForecast),
    temperature=10,
    humidity=20,
    description="Ясно"
)
print(weather_forecast)
