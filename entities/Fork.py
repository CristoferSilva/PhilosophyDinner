from LogGenerator import LogGenerator
from states.ForkState import ForkState


class Fork:
    def __init__(self, name):
        self.state = ForkState.AVAILABLE
        self.name = name

    def change_status_to_busy(self):
        self.state = ForkState.BUSY
        LogGenerator.generate_log("Fork " + self.name + "is BUSY!")

    def change_status_to_available(self):
        self.state = ForkState.AVAILABLE
        LogGenerator.generate_log("Fork " + self.name + "is AVAILABLE!")
