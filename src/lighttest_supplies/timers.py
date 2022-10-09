import time
from time import perf_counter, sleep


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

    @staticmethod
    def bomb(timeout_in_seconds: float, ticking: bool = True):
        def inner(fun):
            start: float = perf_counter()

            def inner_method(*args, **kwargs):
                stopped: bool = False
                end: float = 0
                while not stopped and (end - start < timeout_in_seconds):
                    if ticking:

                        stopped = fun(*args, **kwargs)
                        end = perf_counter()
                        time.sleep(0.1)
                    else:
                        pass

                if not stopped:
                    raise TimeoutError("bad performance")

                return stopped

            return inner_method

        return inner
