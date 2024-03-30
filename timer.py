import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.paused = False
        self.pause_start = 0
        self.total_paused_time = 0

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        if not self.paused:
            self.pause_start = time.time()
            self.paused = True

    def resume(self):
        if self.paused:
            self.total_paused_time += time.time() - self.pause_start
            self.paused = False
            self.pause_start = 0


    def elapsed_seconds(self):
        if not self.start_time :
            raise RuntimeError("Timer hasn't been started.")
        if self.paused:
            return self.pause_start - self.start_time - self.total_paused_time
        return time.time() - self.start_time - self.total_paused_time  

