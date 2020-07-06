class Flight:

    counter=1

    def __init__(self,origin,destination,duration):
        self.id=Flight.counter
        Flight.counter +=1

        self.passengers = []

        self.origin=origin
        self.destination=destination
        self.duration=duration

    def print_info(self):
        print(self.origin)
        print(self.destination)
        print(self.duration)

        print()
        print("Passengers :")
        for passenger in self.passengers:
            print(passenger.name)

    def delay(self,amount):
        self.duration +=amount

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:
    def __init__(self,name):
        self.name = name


def main():
    f1 = Flight(origin="New York",destination="Paris", duration=540)
    f1.delay(20)

    f2 = Flight(origin="New York", destination="Jersey", duration=540)


    alice =  Passenger(name="Alice")
    bob = Passenger(name='Bob')

    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()

if __name__== "__main__":
    main()