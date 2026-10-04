from statedesign import TransportMode, TrainMode, BikeMode, WalkMode, TransportService

bike = BikeMode()
transport = TransportService(bike)

transport.eta()

transport.directions()
