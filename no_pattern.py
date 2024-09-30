# Список для хранения информации о рейсах
flights = []

# Добавление рейсов
flights.append(("SU-123", "Москва", "14:00", "Отправлен"))
flights.append(("AA-456", "Нью-Йорк", "15:30", "Запланирован"))

# Вывод табло
for flight in flights:
    flight_number, destination, departure_time, status = flight
    print(f"Рейс {flight_number}: Направление - {destination}, Время вылета - {departure_time}, Статус - {status}")