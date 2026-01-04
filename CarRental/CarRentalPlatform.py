
#8.	Create a class for customers and define a constructor in it.
#9.	Define methods for requesting the cars and returning them. 
class Customer:
    def __init__(self, name):
        self.name = name

    def request_cars(self, rental, car, num_cars, rental_mode):
        if rental_mode == "hourly":
            return rental.rent_hourly(car, num_cars)
        elif rental_mode == "daily":
            return rental.rent_daily(car, num_cars)
        elif rental_mode == "weekly":
            return rental.rent_weekly(car, num_cars)

    def return_cars(self, rental, car, rental_time, rental_mode, num_cars):
        rental.return_cars(car, rental_time, rental_mode, num_cars)
