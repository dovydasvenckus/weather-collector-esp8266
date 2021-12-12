import dht
import machine

PIN = 14

class WeatherData:
  def __init__(self, temperature, humidity):
    self.temperature = temperature
    self.humidity = humidity

class WeatherCollector:
  def __init__(self):
    self.sensor = dht.DHT22(machine.Pin(PIN))

  def measure(self):
    self.sensor.measure()
    return WeatherData(self.sensor.temperature(), self.sensor.humidity())

