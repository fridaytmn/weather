from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    return (f"Город {weather.city}\nТемпература {weather.temperature} C, "
            f"{weather.weather_type.value}\n"
            f"Восход {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат {weather.sunset.strftime('%H:%M')}")