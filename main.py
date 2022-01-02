class Cinema:
    pass


class Movie:
    pass


class Time:
    pass


class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class Seat:
    def __init__(self, number):
        self.number = number
        self.status = None
        self.customer = None


class Sens:
    def __init__(self, cinema, movie, time, hall):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.prototype_seat()

    def prototype_seat(self):
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))


if __name__ == "__main__":
    cinema = Cinema()
    time = Time()
    hall = Hall("name hall", 60)
    movie = Movie()
    sens = Sens(cinema, movie, time, hall)
    print(len(sens.seats))
    print(type(sens.seats[0]))
