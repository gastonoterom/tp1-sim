from abc import ABC, abstractmethod
from math import trunc


class RandomGenerator(ABC):
    def __init__(self, seed, g, cifras_decimales=4):
        self.cifras_decimales = cifras_decimales
        self.seed = seed
        self.m = 2**g

    def generateNumbers(self):
        xi = self.seed
        random_array = []
        for i in range(self.n):
            xi_mas_uno = (self.a * xi + self.c) % self.m
            xi = xi_mas_uno
            random_number = trunc(
                (xi / (self.m)) * 10 ** self.cifras_decimales) / 10**self.cifras_decimales
            random_array.append({"num": random_number})
        return random_array

class LinearGenerator(RandomGenerator):
    def __init__(self, k, c, seed, g, cifras_decimales=4):
        super().__init__(seed, g, cifras_decimales)
        self.a = 1 + 4 * k
        self.c = c
        self.n = self.m


class MultiplicativeGenerator(RandomGenerator):
    def __init__(self, k, seed, g, cifras_decimales=4):
        super().__init__(seed, g, cifras_decimales)
        self.a = 3 + 8 * k
        self.c = 0
        self.n = int(self.m / 4)
