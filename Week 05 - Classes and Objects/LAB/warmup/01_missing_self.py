# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, percent): 
        self.percent = percent
        return self.percent

r = Record()
print(r.status(95))