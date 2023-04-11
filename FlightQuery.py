from SortedTableMap import *

class FlightQuery(SortedTableMap):
    # class has four attributes: origin, destination, date, and time
    class Key:
        # initializes key class with the four attributes
        def __init__(self, origin, destination, date, time):
            self.origin = origin
            self.destination = destination
            self.date = date
            self.time = time

        # defines less-than comparison operator for Key class
        def __lt__(self, other):
            if self.date != other.date:
                # date of the current Key object is None: return False
                if self.date is None:
                    return False
                # date of the other Key object is None: return True
                if other.date is None:
                    return True
                # True if date of current Key object is less than other Key
                return self.date < other.date
            # same points but for time attribute
            if self.time != other.time:
                if self.time is None:
                    return False
                if other.time is None:
                    return True
                return self.time < other.time
            # origin of current Key not equal to origin of other Key, then:
            if self.origin != other.origin:
                # True if origin of current Key is less than origin of other
                return self.origin < other.origin
            # same for destination
            if self.destination != other.destination:
                return self.destination < other.destination
            # "False" if all of conditions above are False
            return False

        # Returns string representing Key as "origin-destination-date-time"
        def __str__(self):
            return "{0}-{1}-{2}-{3}".format(self.origin, self.destination, self.date, self.time)

    # Calls constructor of SortedTableMap class
    def __init__(self):
        super().__init__()

    # Defines method that searches for flights based on query
    # Method takes in two Key objects (k1 and k2)
    # above and beyond: added optional sort_by_price parameter (default False)
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

print("Enter the earliest date ({0}):")
earliest_date = int(input())

print("Enter the earliest time ({0}):")
earliest_time = int(input())

print("Enter the latest date ({0}):")
latest_date = int(input())

print("Enter the latest time ({0}):")
latest_time = int(input())

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
