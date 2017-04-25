class Timer:
    def __init__(self, frames_needed):
        self.current_passes = 0
        self.frames_needed = frames_needed
        self.complete = False

    def Update(self):
        self.current_passes += 1
        if self.current_passes >= self.frames_needed:
            self.complete = True

    def Reset(self):
        self.current_passes = 0
        self.complete = False
