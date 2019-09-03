class Buffer:
    def __init__(self):
        self.current_part = []
    def add(self, *a):
            self.current_part.extend(a)
            while(len(self.current_part)-5>=0):
                print(sum(self.current_part[0:5]))
                self.current_part = self.current_part[5:]

    def get_current_part(self):
        return self.current_part

