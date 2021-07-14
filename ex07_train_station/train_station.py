"""Train Station."""


class Passenger:
    """Class Passenger."""

    def __init__(self, passenger_id: str, seat: str):
        """Passenger Constructor."""
        self._passenger_id = passenger_id
        self._seat = seat

    @property
    def id(self) -> str:
        """Get ID."""
        return self._passenger_id

    @property
    def seat(self) -> str:
        """Get Seat nr."""
        return self._seat


class Train:
    """Class Train."""

    def __init__(self, train_id: str, carriages: int, seats_in_carriage: int):
        """Train Constructor."""
        self._seats_in_carriage = seats_in_carriage
        self._carriages = carriages
        self._train_id = train_id
        self._passengers = []

    @property
    def carriages(self) -> int:
        """Get number of carriages."""
        return self._carriages

    @property
    def train_id(self) -> str:
        """Get Train ID."""
        return self._train_id

    @property
    def seats_in_carriage(self) -> int:
        """Get number of seats."""
        return self._seats_in_carriage

    @property
    def passengers(self) -> list:
        """Get Passengers."""
        return self._passengers

    def get_seats_in_train(self) -> int:
        """Get Seats."""
        return self._seats_in_carriage * self.carriages

    def get_number_of_passengers(self) -> int:
        """Get Number passengers."""
        return len(self.passengers)

    def get_passengers_in_carriages(self) -> dict:
        """Get Passengers in Carriages."""
        pic = {}
        for i in range(self.carriages):
            pic[str(i + 1)] = []
        for passenger in self.passengers:
            seat = passenger.seat.split('-')
            carriage_nr = passenger.seat_split()[seat[1]]
            pic[carriage_nr].append(passenger)
        return pic

    @train_id.setter
    def train_id(self, value: str):
        """Set Train iD."""
        self._train_id = value

    @carriages.setter
    def carriages(self, value: int):
        """Set Carriages."""
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """Set Seats in Carriage."""
        self._seats_in_carriage = value

    def add_passenger(self, passenger: Passenger) -> Passenger:
        """Add passengers."""
        passengers_dict = {}
        seat = passenger.seat.split('-')
        train_id = str(seat[0])
        carriage_nr = int(seat[1])
        seat_nr = int(seat[2])
        for passenger in self.passengers:
            passengers_dict[passenger.seat] = passenger
            all([train_id == self.train_id,
                 0 < carriage_nr])
        if train_id == self.train_id and 0 < carriage_nr <= self.carriages and 0 < seat_nr <= self.seats_in_carriage and passenger.seat not in passengers_dict:
            self.passengers.append(passenger)
        else:
            return False


class TrainStation:
    """Class Train Station."""

    def __init__(self, trains: list, passengers: list):
        """Train Station."""
        self._trains = trains
        self.passengers = passengers
        self._passengers = []
        for passenger in passengers:
            for train in self.trains:
                if not train.add_passenger(passenger) is False:
                    self._passengers.append(passenger)

    def get_station_overview(self) -> list:
        """Get Station overview."""
        station_overview = list()
        for train in self._trains:
            station_overview.append({'train_id': str(train.train_id), 'carriages': train.carriages, 'seats': "{}/{}".format(train.get_number_of_passengers(), train.get_seats_in_train())})
        return station_overview

    def get_number_of_passengers(self) -> int:
        """Get number of passengers."""
        return len(self._passengers)

    @property
    def passengers(self) -> list:
        """Get number of passengers."""
        return self._passengers

    @passengers.setter
    def passengers(self, value_list: list):
        """Set passengers."""
        self._passengers = value_list

    @property
    def trains(self) -> list:
        """Get Train."""
        return self._trains

    @trains.setter
    def trains(self, value_list: list):
        """Set Train."""
        self._trains = value_list
