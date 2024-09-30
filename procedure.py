flights = []

def add_flight(flight_number, destination, departure_time, status):
    flights.append({
        "flight_number": flight_number,
        "destination": destination,
        "departure_time": departure_time,
        "status": status
    })

def display_board():
    for flight in flights:
        print(f"Рейс {flight['flight_number']}: Направление - {flight['destination']}, Время вылета - {flight['departure_time']}, Статус - {flight['status']}")

# Пример использования
add_flight("SU-123", "Москва", "14:00", "Отправлен")
add_flight("AA-456", "Нью-Йорк", "15:30", "Запланирован")
display_board()