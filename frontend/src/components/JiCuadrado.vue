<template>
  <div>
    <b-card
      class="bcard-index"
      title="Prueba de Ji Cuadrado"
      :sub-title="subtitle"
    >
      <b-table
        id="jicuadrado-table"
        :per-page="pageSize"
        :current-page="pageNum"
        striped
        hover
        :items="rows"
      ></b-table>
      <b-pagination
        v-model="pageNum"
        :total-rows="intervalos"
        :per-page="pageSize"
        aria-controls="jicuadrado-table"
        align="center"
      ></b-pagination>
      <img :src="histogramSrc" />
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
      intervalos: 10,
      histogramSrc: "",
      rows: [],
    };
  },
  props: ["jiCuadradoProps"],
  methods: {
    generateHistogramSrc() {
      let tipo = this.jiCuadradoProps.type;
      let cantidad = this.jiCuadradoProps.cantidad;
      let seed = this.jiCuadradoProps.random_props.semilla;
      let intervalos = this.intervalos;

      this.histogramSrc = `http://localhost:5000/api/histogram/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}`;
    },
    async getRows() {
      if (this.cantidad == "") return;
      let tipo = this.jiCuadradoProps.type;
      let cantidad = this.jiCuadradoProps.cantidad;
      let seed = this.jiCuadradoProps.random_props.semilla;
      let intervalos = this.intervalos;
      const promise = clienteAxios.get(
        `/api/jicuadrado/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}`
      );
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
