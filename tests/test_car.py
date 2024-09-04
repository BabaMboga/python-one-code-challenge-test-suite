import pytest
# Directly import student's cars.py
import car

def test_car_class(capfd):
    car1 = car.Car(make="Toyota", model="Camry", year=2020)
    car1.display_info()
    out, _ = capfd.readouterr()
    assert "Make: Toyota, Model: Camry, Year: 2020" in out

    car2 = car.Car(make="Honda", model="Civic", year=2018)
    car2.display_info()
    out, _ = capfd.readouterr()
    assert "Make: Honda, Model: Civic, Year: 2018" in out