from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''
    class Key:
        '''Represents a key used to store flights in the FlightQuery object'''
        __slots__ = "_origin", "_dest", "_date", "_time"
        def __init__(self, origin, dest, date, time):
            '''Initializes a Key object with the specified origin, destination, date, and time'''
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        def __lt__(self, other):
            '''Compares two Key objects and returns True if self is less than other'''
            if self._origin < other._origin:
                return True
            elif self._origin > other._origin:
                return False
            else:
                if self._dest < other._dest:
                    return True
                elif self._dest > other._dest:
                    return False
                else:
                    if self._date < other._date:
                        return True
                    elif self._date > other._date:
                        return False
                    else:
                        if self._time < other._time:
                            return True
                        else:
                            return False

    class Flight:
        '''Represents a flight object'''
        __slots__ = "_origin", "_dest", "_date", "_time", "_flight_number", "_seats_F", "_seats_Y", "_duration", "_fare"
        def __init__(self, origin, dest, date, time, flight_number, seats_F, seats_Y, duration, fare):
            '''Initializes a Flight object with the specified parameters'''
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time
            self._flight_number = flight_number
            self._seats_F = seats_F
            self._seats_Y = seats_Y
            self._duration = duration
            self._fare = fare

        def __str__(self):
            '''Returns a string representation of the Flight object'''
            return f"Flight {self._flight_number} from {self._origin} to {self._dest} on {self._date} at {self._time}"

        def query(self, origin, dest, date, time):
            '''Returns a list of flights matching the input query within a flexible departure date'''
            # Create keys that cover a range of possible departure times on the input date
            keys = [self.Key(origin, dest, date, time), 
                    self.Key(origin, dest, date, time + 100), 
                    self.Key(origin, dest, date, time + 200)]
            # Find the range of keys that cover the possible departure times
            start = self._find_index(keys[0])
            end = self._find_index(keys[-1])
            # Filter the flights within the date range
            flights = [flight for key, flight in self._table[start:end+1] if key._origin == origin and key._dest == dest and key._date == date]
            return flights
    
