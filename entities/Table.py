import threading

from entities.Philosophy import Philosophy
from observer.Observer import Observer
from states.PhilosophyState import PhilosophyState
import math

class Table:
    def __init__(self, fork_quantity, initial_earters_quantity, philosophers):
        self.fork_quantity = fork_quantity
        self.philosophers = list(philosophers)
        self.initial_earters_quantity = initial_earters_quantity

    def add_philosophy(self, philosophy):
        self.philosophers.append(philosophy)

    def remove_philosophy(self, philosophy):
        self.philosophers.remove(philosophy)

    def run_table(self):
        awaiter_quantity = len(self.philosophers) - self.initial_earters_quantity
        awaiters = list()
        eaters = []
        self.fill_list(awaiter_quantity, awaiters)
        self.fill_list(self.initial_earters_quantity, eaters)

        for i in range(len(eaters)):
            eaters[i].attach_observer(awaiters.pop())

        self.wake_up_all_eaters(eaters)

    def wake_up_all_eaters(self, eaters):
        for current_eater in eaters:
            new_thread = threading.Thread(target=current_eater.update)
            new_thread.start()

    def fill_list(self, quantity, state_list):
        for i in range(quantity):
            state_list.append(self.philosophers.pop())

