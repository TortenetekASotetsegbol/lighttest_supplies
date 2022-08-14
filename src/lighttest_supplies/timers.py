from time import perf_counter


class Utimer:
    start: float = 0
    end: float = 0

    def set_start(self):
        self.start = perf_counter()

    def set_end(self):
        self.end = perf_counter()

    def elapsed_time(self):
        elapsed_time = self.end - self.start
        return elapsed_time
