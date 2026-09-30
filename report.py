def create_report(data):

    temperature = data["list"][0]["main"]["temp"]

    rain_chance = data["list"][0]["pop"] * 100

    report = (
        f"Temperature: {temperature:.1f}°C\n"
        f"Chance of Rain: {rain_chance:.0f}%"
    )

    return report