<template>
  <div>
    <p>Tabla de frecuencias:</p>
    <b-table
      id="frec-table"
      striped
      hover
      :items="randomDataProvider"
    ></b-table>

    <p>Tabla N°2: Frecuencias obtenidas de numeros aleatorios</p>
  </div>
</template>
<script>
import clienteAxios from "../config/axios";

export default {
  data() {
    return {};
  },
  props: ["frequencyProps"],
  methods: {
    async randomDataProvider() {
      let apiUrl;
      let li, ls, media, sigma;

      let seed = this.frequencyProps.seed;
      let intervalos = this.frequencyProps.intervalos;
      let cantidad = this.frequencyProps.cantidad;

      let tipo = this.frequencyProps.randomType;
      switch (tipo) {
        case "uniforme":
          li = this.frequencyProps.li;
          ls = this.frequencyProps.ls;
          apiUrl = `/api/frequency/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&li=${li}&ls=${ls}`;
          break;
        case "exponencial":
          media = this.frequencyProps.media;
          apiUrl = `/api/frequency/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&media=${media}`;

          break;
        case "normal":
          media = this.frequencyProps.media;
          sigma = this.frequencyProps.sigma;

          apiUrl = `/api/frequency/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&media=${media}&sigma=${sigma}`;
          break;
      }
      const promise = clienteAxios.get(apiUrl);
      // Must return a promise that resolves to an array of items
      return promise.then((data) => {
        console.log(data);
        // Pluck the array of items off our axios response
        let items = data.data;

        // Must return an array of items or an empty array if an error occurred
        return items;
      });
    },
    mounted() {},
  },
};
</script>

<style></style>
