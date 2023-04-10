from SortedTableMap import *

class FlightQuery(SortedTableMap):
    class Key:
        def __init__(self, origin, destination, date, time):
            self.origin = origin
            self.destination = destination
            self.date = date
            self.time = time

        def __lt__(self, other):
            if self.date != other.date:
                if self.date is None:
                    return False
                if other.date is None:
                    return True
                return self.date < other.date
            if self.time != other.time:
                if self.time is None:
                    return False
                if other.time is None:
                    return True
                return self.time < other.time
            if self.origin != other.origin:
                return self.origin < other.origin
            if self.destination != other.destination:
                return self.destination < other.destination
            return False

        def __str__(self):
            return "{0}-{1}-{2}-{3}".format(self.origin, self.destination, self.date, self.time)

    def __init__(self):
        super().__init__()

    def query(self, origin, destination, date, time, sort_by_price=False):
        # Find the closest flight in either direction
        closest_before = None
        closest_after = None
        for key in self._table:
            if key.origin == origin and key.destination == destination:
                flight_time = int(str(key.date) + str(key.time).zfill(4))
                if flight_time < date * 100 + time:
                    if closest_before is None or flight_time > closest_before:
                        closest_before = flight_time
                        before_key = key
                elif flight_time > date * 100 + time:
                    if closest_after is None or flight_time < closest_after:
                        closest_after = flight_time
                        after_key = key

        # Return the closest flight(s) as a list of tuples
        result = []
        if closest_before:
            result.append((before_key, self[before_key]))
        if closest_after:
            result.append((after_key, self[after_key]))

        if sort_by_price:
            result = sorted(result, key=lambda x: x[1])
        else:
            result = sorted(result, key=lambda x: (x[0].date, x[0].time))
        return result


# Create a FlightQuery object
flights = FlightQuery()

# Create flight key-value pairs using 'for' loop
s = [("A", "B", 622, 1200, 100), ("A", "B", 622, 1230, 120), ("A", "B", 622, 1300, 150), ("A", "B", 620, 1330, 80), ("A", "B", 630, 1400, 200), ("A", "B", 624, 1430, 180)]
for each in s:
    key = flights.Key(each[0], each[1], each[2], each[3])
    value = each[4]  # add the fare value to the value object
    flights[key] = value

# Interface for inputting user queries
print("Welcome to the Flight finder program!\n")

# Ask user to select a sorting option
print("Please select a sorting option:")
print("1. Sort by date and time (earliest flights first)")
print("2. Sort by price (cheapest flights first)")

sort_option = input("Enter your choice (1 or 2): ")

if sort_option == "1":
    sort_by_price = False
elif sort_option == "2":
    sort_by_price = True
else:
    print("Invalid input. Please try again.")
    exit()

# Ask user for flight details
print("\nEnter the origin airport:")
origin = input().upper()

print("Enter destination airport:")
destination = input().upper()

print("Enter the date (in the format MM/DD/YYYY):")
date = input()

print("Enter the time (in the format HHMM, e.g. 1430 for 2:30 PM):")
time = int(input())

# Run the query and print results
result = flights.query(origin, destination, date, time, sort_by_price)

if not result:
    print("\nNo flights found.")
else:
    print("\nHere are the closest flights:")
    for r in result:
        key = r[0]
        value = r[1]
        print("Flight from {0} to {1} on {2} at {3} with fare {4}".format(key.origin, key.destination, key.date, key.time, value))
