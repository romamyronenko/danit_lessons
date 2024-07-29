class City:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def set_city(self, value):
        self._value = value
