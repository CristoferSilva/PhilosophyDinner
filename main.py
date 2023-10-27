import random

from entities.Philosophy import Philosophy
from entities.Table import Table


philosophers = [Philosophy("Steve"), Philosophy("Bill"), Philosophy("Tim"), Philosophy("Elon")]
random.shuffle(philosophers)

table = Table(fork_quantity=5, initial_earters_quantity= 2, philosophers= philosophers)
table.run_table()