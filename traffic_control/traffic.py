import random
import time
from collections import deque
from threading import Thread


class Plane:
    def __init__(self, flight_number, speed, altitude):
        self.flight_num = flight_number
        self.altitude = altitude
        self.speed = speed

    def descend(self, descent_rate):
        self.altitude -= descent_rate

    def reduce_speed(self, speed_reduction):
        self.speed -= speed_reduction


class Airport:
    def __init__(self, name, runway_capacity):
        self.name = name
        self.runway_capacity = runway_capacity
        self.available_runways = runway_capacity
        self.landing_queue = deque()

    def request_landing(self, plane):
        print(
            f"📞 {plane.flight_number} requesting permission to land at {self.name}")
        if self.available_runways > 0:
            self.available_runways -= 1
            return True
        else:
            self.landing_queue.append(plane)
            return False

    def land_plane(self, plane):
        if plane.altitude != 0 or plane.speed != 0:
            print(f"🛬 {plane.flight_number} has landed at {self.name}")
            self.available_runways += 1
            if self.landing_queue:
                next_plane = self.landing_queue.popleft()
                Thread(target=self.process_landing, args=(next_plane,)).start()
        else:
            print(f"{plane.flight_number} cannot land, current altitude is {plane.altitude} feet, speed is {plane.speed} knots")

    def process_landing(self, plane):
        permission_granted = self.request_landing(plane)
        if permission_granted:
            while plane.altitude > 0 or plane.speed > 0:

                # Descend
                descent_rate = random.randint(500, 1000)
                plane.descend(descent_rate)
                print(
                    f"{plane.flight_number} is descending, current altitude is {plane.altitude} feet")

                # Slow Speed
                speed_reduction = random.randint(10, 50)
                plane.reduce_speed(speed_reduction)
                print(
                    f"{plane.flight_number} is reducing speed, current speed is {plane.speed} knots")

                time.sleep(1)
            self.land_plane(plane)


if __name__ == "__main__":
    airport = Airport("ABC International Airport", 2)

    planes = [
        Plane("Flight 123", 8000, 200),
        Plane("Flight 456", 6000, 180),
        Plane("Flight 789", 9000, 100),
    ]

    for plane in planes:
        t = Thread(target=airport.process_landing, args=(plane,))
        t.start()
        time.sleep(2)
