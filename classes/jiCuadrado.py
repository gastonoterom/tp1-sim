import math


class JiCuadradoClass:
    # Override __init__
    def __init__(self, intervalos, random_array):
        # Variables por parametro, cantidad de intervalos y lista de numeros randoms
        self._intervalos = intervalos
        self._random_array = random_array

        # Constantes
        self._intervalo_size = 0

        # Listas a crear, frecuencia obtenida, frecuencia esperada y estadistico de prueba
        self._frecuencia_obtenida = []
        self._frecuencia_esperada = []
        self._estadistico_prueba = []
        self._estadistico_prueba_ac = []

        # Se llama a la funcion update intervalos
        self._update_valores()

    # Actualiza los valores de la frecuencia obtenida, la frecuencia esperada
    # y el estadistico de prueba, deberia llamarse cada vez que cambia la cantidad
    # de intervalos
    def _update_valores(self):

        # El tamaño de cada intervalo cambia
        self._intervalo_size = 1 / self._intervalos

        # En este ji cuadrado se espera que la frecuencia esperada sea igual para cada intervalo
        fe = len(self._random_array) / self._intervalos
        self._frecuencia_esperada = [fe for x in range(self._intervalos)]

        # Para cada valor de la lista aleatoria, se suma en el intervalo que le corresponde como frecuencias obtenida
        self._frecuencia_obtenida = [0 for x in range(self._intervalos)]

        for random_num in self._random_array:
            # SE MULTIPLICA POR DIEZ LOS VALORES A DIVIDIR PORQUE PYTHON TIENE PROBLEMAS DE DECIMALES
            intervalo_a_sumar = int(
                # Los intervalos tienen este limite: [Li, Ls)
                (random_num["num"] * 10000) // (self._intervalo_size * 10000))
            self._frecuencia_obtenida[intervalo_a_sumar] += 1

        # Se calcula el estadistico de prueba para cada intervalo
        fe = self._frecuencia_esperada
        fo = self._frecuencia_obtenida
        self._estadistico_prueba = [(fe[i] - fo[i])**2 / fe[i]
                                    for i in range(self._intervalos)]

        self._estadistico_prueba_ac = []

        ac = 0
        for i in self._estadistico_prueba:
            ac += i
            self._estadistico_prueba_ac.append(ac)

    # Getters
    @property
    def random_array(self):
        ra = []
        for rn in self._random_array:
            ra.append(rn["num"])
        return ra

    @property
    def frecuencia_obtenida(self):
        return self._frecuencia_obtenida

    @property
    def frecuencia_esperada(self):
        return self._frecuencia_esperada

    @property
    def estadistico_prueba(self):
        return self._estadistico_prueba

    @property
    def estadistico_prueba_ac(self):
        return self._estadistico_prueba_ac

    @property
    def intervalos(self):
        return self._intervalos

    @property
    def rows(self):
        rows = []
        for i in range(self._intervalos):

            li = str(math.trunc(self._intervalo_size * i * 10000) / 10000)
            ls = str(math.trunc(self._intervalo_size * (i + 1) * 10000) / 10000)
            intervalo = li + " - " + ls

            fo = math.trunc(self._frecuencia_obtenida[i] * 10000) / 10000
            fe = math.trunc(self._frecuencia_esperada[i] * 10000) / 10000

            ep = math.trunc(self._estadistico_prueba[i] * 10000) / 10000
            ep_ac = math.trunc(self._estadistico_prueba_ac[i] * 10000) / 10000

            rows.append({
                "intervalo": intervalo,
                "frecuencia_obtenida": fo,
                "frecuencia_esperada": fe,
                "estadistico_prueba": ep,
                "estadistico_prueba_ac": ep_ac,
            })

        return rows
#    # Setters
#    @intervalos.setter
#    def intervalos(self, new_value):
#        self._intervalos = new_value
#        self._update_valores()
