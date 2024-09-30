class Flight:
    def __init__(self, flight_number, destination, departure_time, status):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.status = status

    def display_flight_info(self):
        return f"Рейс {self.flight_number}: Направление - {self.destination}, Время вылета - {self.departure_time}, Статус - {self.status}"


class AirportBoard:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_board(self):
        for flight in self.flights:
            print(flight.display_flight_info())


# Пример использования
airport_board = AirportBoard()
airport_board.add_flight(Flight("SU-123", "Москва", "14:00", "Отправлен"))
airport_board.add_flight(Flight("AA-456", "Нью-Йорк", "15:30", "Запланирован"))
airport_board.display_board()