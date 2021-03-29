<template>
  <div>
    <b-card
      class="bcard-index"
      title="Prueba de Ji Cuadrado"
      :sub-title="subtitle"
    >
      <p>Cantidad de intervalos:</p>
      <b-form-select
        style="max-width: 100px"
        v-on:change="intervalosChanged"
        v-model="intervalos"
        :options="intervalos_select"
      ></b-form-select>
      <b-table
        style="margin-top: 10px"
        id="jicuadrado-table"
        :per-page="pageSize"
        :current-page="pageNum"
        striped
        hover
        :items="rows"
      ></b-table>
      <p>Tabla N°2: Prueba de Ji Cuadrado para serie de numeros aleatorios</p>
      <b-pagination
        v-model="pageNum"
        :total-rows="intervalos"
        :per-page="pageSize"
        aria-controls="jicuadrado-table"
        align="center"
      ></b-pagination>
      <img :src="histogramSrc" />
      <p>
        Figura N°1: Histograma de numeros aleatorios obtenidos dentro de
        intervalos
      </p>
    </b-card>
  </div>
</template>
<script>
import clienteAxios from "../config/axios";

export default {
  data() {
    return {
      pageNum: 0,
      pageSize: 5,
      subtitle: "",
      histogramSrc: "",
      rows: [],
      intervalos: 10,
      intervalos_select: [10, 15, 20],
    };
  },
  props: ["jiCuadradoProps"],
  methods: {
    generateHistogramSrc() {
      let tipo = this.jiCuadradoProps.type;
      let seed = this.jiCuadradoProps.random_props.semilla;
      let intervalos = this.intervalos;
      let cantidad = this.jiCuadradoProps.cantidad;

      let valorK, valorG, valorC;
      switch (tipo) {
        case "random":
          cantidad = this.jiCuadradoProps.cantidad;
          this.histogramSrc = `http://localhost:5000/api/histogram/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}`;
          break;
        case "linear":
          valorK = this.jiCuadradoProps.random_props.valorK;
          valorG = this.jiCuadradoProps.random_props.valorG;
          valorC = this.jiCuadradoProps.random_props.valorC;
          this.histogramSrc = `http://localhost:5000/api/histogram/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&k=${valorK}&g=${valorG}&c=${valorC}`;
          break;
      }
    },
    intervalosChanged() {
      this.generateHistogramSrc();
      this.getRows();
    },
    async getRows() {
      console.log(this.jiCuadradoProps.random_props);
      if (this.cantidad == "") return;

      let tipo = this.jiCuadradoProps.type;
      let cantidad = this.jiCuadradoProps.cantidad;
      let seed = this.jiCuadradoProps.random_props.semilla;
      let intervalos = this.intervalos;
      let promise;
      let valorK, valorG, valorC;

      switch (tipo) {
        case "random":
          cantidad = this.jiCuadradoProps.cantidad;
          promise = clienteAxios.get(
            `/api/jicuadrado/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}`
          );
          break;
        case "linear":
          valorK = this.jiCuadradoProps.random_props.valorK;
          valorG = this.jiCuadradoProps.random_props.valorG;
          valorC = this.jiCuadradoProps.random_props.valorC;
          promise = clienteAxios.get(
            `/api/jicuadrado/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&k=${valorK}&g=${valorG}&c=${valorC}`
          );
          break;
      }

      // Must return a promise that resolves to an array of items
      promise.then((data) => {
        console.log(data);
        // Pluck the array of items off our axios response
        let items = data.data;

        this.rows = items;
      });
    },
  },
  mounted() {
    let tipo = "";
    switch (this.jiCuadradoProps.type) {
      case "random":
        tipo = "nativo de python";

        break;
      case "lineal":
        tipo = "congruencial lineal";
        break;
      case "multiplicativo":
        tipo = "congruencial multiplicativo";
        break;
    }
    this.subtitle = `A partir de valores generados por el método ${tipo}`;
    this.generateHistogramSrc();
    this.getRows();
  },
};
</script>

<style></style>
