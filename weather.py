import dht
import machine

PIN = 14

class WeatherData:
  def __init__(self, temperature, humidity):
    self.sensor = dht.DHT22(machine.Pin(PIN))
    self.temperature = temperature
    self.humidity = humidity

def measure():
  sensors.measure()
  return WeatherData(sensor.temperature(), sensor.humidity())

