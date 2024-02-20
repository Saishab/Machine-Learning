from datetime import datetime, timedelta


flights = [
    ("FL001", "JFK", "LAX", "2024-02-20 08:00", "2024-02-20 11:30"),
    ("FL002", "JFK", "LAX", "2024-02-20 10:00", "2024-02-20 13:30"),
    ("FL003", "JFK", "LAX", "2024-02-20 12:00", "2024-02-20 15:30"),
    ("FL004", "JFK", "LAX", "2024-02-20 14:00", "2024-02-20 17:30"),
    ("FL005", "JFK", "LAX", "2024-02-20 16:00", "2024-02-20 19:30"),
    
]

def get_earliest_arrival(origin, start_time):
    earliest_arrival_time = None
    
    for flight in flights:
        flight_number, flight_origin, destination, departure_time_str, arrival_time_str = flight
        if flight_origin == origin:
            departure_time = datetime.strptime(departure_time_str, '%Y-%m-%d %H:%M')
            arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%d %H:%M')
            if departure_time >= start_time:
                if earliest_arrival_time is None or arrival_time < earliest_arrival_time:
                    earliest_arrival_time = arrival_time
    
    return earliest_arrival_time


origin = "JFK"
start_time = datetime(2024, 2, 20, 7, 0)  
earliest_arrival = get_earliest_arrival(origin, start_time)

if earliest_arrival:
    print("Earliest arrival time for destination from", origin, "starting from", start_time.strftime('%Y-%m-%d %H:%M'), "is", earliest_arrival.strftime('%Y-%m-%d %H:%M'))
else:
    print("No flights available from", origin, "starting from", start_time.strftime('%Y-%m-%d %H:%M'))
