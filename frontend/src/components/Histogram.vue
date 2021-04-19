<template>
  <div>
    <b-card class="bcard-index" title="Histograma" :sub-title="subtitle">
      <p>Cantidad de intervalos:</p>
      <b-form-select
        style="max-width: 100px"
        v-on:change="intervalosChanged"
        v-model="intervalos"
        :options="intervalos_select"
      ></b-form-select>
      <p></p>
      <img :src="histogramSrc" />
      <p>
        Figura N°1: Histograma de numeros aleatorios obtenidos dentro de
        intervalos
      </p>
      <Frequencies
        v-if="randomHash"
        :key="randomHash"
        :frequencyProps="frequencyProps"
      >
      </Frequencies>
    </b-card>
  </div>
</template>
<script>
import clienteAxios from "../config/axios";
import Frequencies from "./Frequencies";
export default {
  components: { Frequencies },

  data() {
    return {
      downloadLink: null,
      pageNum: 0,
      pageSize: 5,
      subtitle: "",
      randomHash: false,
      histogramSrc: "",
      rows: [],
      intervalos: 10,
      intervalos_select: [10, 15, 20],
      frequencyProps: {},
    };
  },
  props: ["histogramProps"],
  methods: {
    generateHistogramSrc() {
      let tipo = this.histogramProps.type;
      let seed = this.histogramProps.random_props.semilla;
      let intervalos = this.intervalos;
      let cantidad = this.histogramProps.cantidad;

      let li, ls;
      let media, sigma;
      switch (tipo) {
        case "uniforme":
          li = this.histogramProps.random_props.li;
          ls = this.histogramProps.random_props.ls;
          this.histogramSrc = `${clienteAxios.defaults.baseURL}/api/histogram/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&li=${li}&ls=${ls}`;
          break;
        case "exponencial":
          media = this.histogramProps.random_props.media;
          this.histogramSrc = `${clienteAxios.defaults.baseURL}/api/histogram/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&media=${media}`;

          break;
        case "normal":
          media = this.histogramProps.random_props.media;
          sigma = this.histogramProps.random_props.sigma;

          this.histogramSrc = `${clienteAxios.defaults.baseURL}/api/histogram/${tipo}?cantidad_muestra=${cantidad}&seed=${seed}&intervalos=${intervalos}&media=${media}&sigma=${sigma}`;

          break;
      }
    },
    intervalosChanged() {
      this.generateHistogramSrc();
      this.frequencyProps = {
        randomType: this.histogramProps.type,
        li: this.histogramProps.random_props.li,
        ls: this.histogramProps.random_props.ls,
        sigma: this.histogramProps.random_props.sigma,
        media: this.histogramProps.random_props.media,
        seed: this.histogramProps.random_props.semilla,
        intervalos: this.intervalos,
        cantidad: this.histogramProps.cantidad,
      };
      this.randomHash = new Date().getTime();
    },
  },
  mounted() {
    let tipo = "";
    switch (this.histogramProps.type) {
      case "uniforme":
        tipo = "uniforme";

        break;
      case "exponencial":
        tipo = "exponencial";
        break;
      case "normal":
        tipo = "congruencial multiplicativo";
        break;
    }
    this.subtitle = `A partir de valores generados por el método ${tipo}`;
    this.generateHistogramSrc();
    this.frequencyProps = {
      randomType: this.histogramProps.type,
      li: this.histogramProps.random_props.li,
      ls: this.histogramProps.random_props.ls,
      sigma: this.histogramProps.random_props.sigma,
      media: this.histogramProps.random_props.media,
      seed: this.histogramProps.random_props.semilla,
      intervalos: this.intervalos,
      cantidad: this.histogramProps.cantidad,
    };
    this.randomHash = new Date().getTime();
  },
};
</script>

<style></style>
