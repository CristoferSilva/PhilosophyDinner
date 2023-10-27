class Subject:
    def __init__(self):
        self.observers = []

    def attach_observer(self, new_observer):
        self.observers.append(new_observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for current_observer in self.observers:
            current_observer.update()