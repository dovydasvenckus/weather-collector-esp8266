from weather import WeatherCollector
from machine import Pin
from time import sleep

weather_collector = WeatherCollector()
print(weather_collector.measure())

led = Pin(2, Pin.OUT)
sleep(5)
led.value(1)
