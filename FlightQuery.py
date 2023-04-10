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

    def query(self, k1, k2, sort_by_price=False):
        result = []
        for key in self._table:
            if k1 < key._key < k2:
                result.append((key._key, key._value))
        if sort_by_price:
            result = sorted(result, key=lambda x: x[1])
        else:
            result = sorted(result, key=lambda x: (x[0].date, x[0].time))
        return result
    
    def get_available_range(self):
        dates = sorted(set([key.date for key in self._table.keys()]))
        if dates:
            date_range = "{0} to {1}".format(min(dates), max(dates))
            times = sorted(set([key.time for key in self._table.keys()]))
            time_range = "{0} to {1}".format(min(times), max(times))
        else:
            date_range = "No flights available"
            time_range = "No flights available"
        return date_range, time_range


# Create a FlightQuery object
flights = FlightQuery()

# Create flight key-value pairs using 'for' loop
s = [("A", "B", 622, 1200, 100), ("A", "B", 622, 1230, 120), ("A", "B", 622, 1300, 150), ("A", "B", 620, 1330, 80), ("A", "B", 630, 1400, 200), ("A", "B", 624, 1430, 180)]
for each in s:
    key = flights.Key(each[0], each[1], each[2], each[3])
    value = each[4]  # add the fare value to the value object
    flights[key] = value

print(flights)

# Interface for inputting user queries
print("Welcome to the Flight finder program!\n")

# Set the available range for flight entries
date_range = None
time_range = None

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

# Set the available range for flight entries based on current flights
if flights:
    date_range = "{0} to {1}".format(min(flights, key=lambda x: x.date).date, max(flights, key=lambda x: x.date).date)
    time_range = "{0} to {1}".format(min(flights, key=lambda x: x.time).time, max(flights, key=lambda x: x.time).time)

# Ask user for flight details
print("\nEnter the origin airport (A, B, or C):")
origin = input().upper()

print("Enter destination airport (A, B, or C):")
destination = input().upper()

print("Enter the earliest date ({0}):".format(date_range))
earliest_date = input()

print("Enter the earliest time ({0}):".format(time_range))
earliest_time = input()

print("Enter the latest date ({0}):".format(date_range))
latest_date = input()

print("Enter the latest time ({0}):".format(time_range))
latest_time = input()

# Run the query and print results
k1 = FlightQuery.Key(origin, destination, earliest_date, earliest_time)
k2 = FlightQuery.Key(destination, origin, latest_date, latest_time)
results = flights.query(k1, k2, sort_by_price)

if results:
    print("\nHere are the available flights:\n")
    for result in results:
        print("Flight from {0} to {1} on {2} at {3} with fare {4}".format(result[0].origin, result[0].destination, result[0].date, result[0].time, result[1]))
else:
    print("\nNo flights found.")
