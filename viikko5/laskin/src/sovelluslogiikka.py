class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvot = [arvo]
    
    @property
    def _arvo(self):
        return self._arvot[-1]

    @_arvo.setter
    def _arvo(self, value):
        self._arvot.append(value)

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        if len(self._arvot) > 1:
            self._arvot.pop()
