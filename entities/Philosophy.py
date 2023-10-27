import random
from abc import ABC

from LogGenerator import LogGenerator
from observer.Observer import Observer
from observer.Subject import Subject
from states.PhilosophyState import PhilosophyState
from time import sleep


class Philosophy(Observer, Subject, ABC):

    def __init__(self, name):
        super().__init__()
        self.state = PhilosophyState.THIKING
        self.name = name
        self.current_forks = []

    def set_forks(self, fork_right, fork_left):
        fork_right.change_status_to_busy()
        fork_left.change_status_to_busy()
        self.current_forks.append(fork_right)
        self.current_forks.append(fork_left)

    def free_forks(self):
        for current_fork in self.current_forks:
            current_fork.change_status_to_available()

    def update(self):
        self.state = PhilosophyState.EATING
        LogGenerator.generate_log("Philosophy " + self.name + " is eating!\n")
        random_seconds = random.uniform(2, 10)
        sleep(random_seconds)
        self.free_forks()
        self.state = PhilosophyState.THIKING
        LogGenerator.generate_log("Philosophy " + self.name + " is thinking!\n")
        self.notify_observers()