from SortedTableMap import SortedTableMap

class FlightQuery(SortedTableMap):
    class Key:

        def __init__(self, origin, destination, date, time):
            self.origin = origin
            self.destination = destination
            self.date = date
            self.time = time
        
        def __lt__(self, other):
            if self.origin != other.origin:
                return self.origin < other.origin
            if self.destination != other.destination:
                return self.destination < other.destination
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
            return False

        def __str__(self):
            return "{0}-{1}-{2}-{3}".format(self.origin, self.destination, self.date, self.time)

    def __init__(self):
        super().__init__()

    def query(self, k1, k2):
        result = []
        for key in self._table:
            if k1 < key._key < k2:
                result.append((key._key, key._value))
        return result

# Create a FlightQuery object
flights = FlightQuery()

# Create flight key-value pairs using 'for' loop
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3"), ("A", "B", 620, 1330, "No4"), ("A", "B", 630, 1400, "No5"), ("A", "B", 624, 1430, "No6")]
for each in s:
    key = flights.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    flights[key] = value

# Interface for inputting user queries
origin = input("Enter the origin airport: ")
destination = input("Enter the destination airport: ")
earliest_date = int(input("Enter the earliest date (in YYYYMMDD format): "))
earliest_time = int(input("Enter the earliest time (in HHMM format): "))
latest_date = int(input("Enter the latest date (in YYYYMMDD format): "))
latest_time = int(input("Enter the latest time (in HHMM format): "))

# Run the query and print results
k1 = FlightQuery.Key(origin, destination, earliest_date, earliest_time)
k2 = FlightQuery.Key(destination, origin, latest_date, latest_time)
results = flights.query(k1, k2)

if results:
    for result in results:
        print(result)
else:
    print("No flights found.")
