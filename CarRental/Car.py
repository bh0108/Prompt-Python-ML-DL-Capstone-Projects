#*.py file for Car rental with Built-in DateTime Module
# Steps 1 -7 on Project
#1.	Create a module (.py file) for car rental and import the built-in module DateTime to handle the rental time and bill.
#2.	Create a class for renting the cars and define a constructor in it.
#3.	Define a method for displaying the available cars. Also, define methods for renting cars on an hourly, daily and weekly basis, respectively.
#4.	Inside these methods, make sure that the number of requested cars is positive and lesser than the total available cars.
#5.	Store the time of renting a car in a variable, which can later be used in the bill while returning the car. 
#6.	Define a method to return the cars using rental time, rental mode (hourly, daily, or weekly), and the number of cars rented.
#7.	Inside the return method; update the inventory stock, calculate the rental period, and generate the final bill.

# Car rental platform for cars to rent hourly, daily, weekly and availability of cars
from datetime import datetime

class CarRental:
    def __init__(self, available_cars):
        self.available_cars = available_cars

    def display_available_cars(self):
        print("Available cars for rental:")
        for car, quantity in self.available_cars.items():
            print(f"{car}: {quantity}")

    def rent_hourly(self, car, num_cars):
        return self.rent(car, num_cars, "hourly")

    def rent_daily(self, car, num_cars):
        return self.rent(car, num_cars, "daily")

    def rent_weekly(self, car, num_cars):
        return self.rent(car, num_cars, "weekly")

    def rent(self, car, num_cars, rental_mode):
        if car in self.available_cars and self.available_cars[car] >= num_cars and num_cars > 0:
            now = datetime.now()
            print(f"{num_cars} {car}(s) have been rented {rental_mode} at {now}")
            return now
        else:
            print("Sorry, the requested number of cars is not available for rental.")
            return None

    def return_cars(self, car, rental_time, rental_mode, num_cars):
        rental_periods = {"hourly": 1, "daily": 24, "weekly": 168}
        if rental_mode in rental_periods and car in self.available_cars:
            rental_period = (datetime.now() - rental_time).seconds / 3600 / rental_periods[rental_mode]
            bill = rental_period * rental_periods[rental_mode] * num_cars
            print(f"{num_cars} {car}(s) have been returned. Your bill is ${bill}")
            self.available_cars[car] += num_cars
        else:
            print("Invalid rental mode or car.")
