<template>
  <div class="random">
    <b-card
      class="bcard-index"
      title="Generador de números aleatorios"
      header="Simulación - UTN FRC"
      sub-title="Método nativo de python"
    >
      <b-form @submit="onSubmit">
        <b-form-group
          id="input-group-2"
          label="Cantidad de números a generar:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            placeholder="Ingresar cantidad"
            required
            v-model="cantidad"
            @keypress="isNumber($event)"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Generar</b-button>
      </b-form>

      <div class="table-container" v-if="randomArray.length > 0">
        <b-table
          id="random-table"
          :per-page="pageSize"
          :current-page="pageNum"
          striped
          hover
          :items="randomArray"
        ></b-table>
      </div>
      <div v-if="randomArray.length > 0" class="pagination-container">
        <b-pagination
          v-model="pageNum"
          :total-rows="randomArray.length"
          :per-page="pageSize"
          aria-controls="random-table"
          align="center"
        ></b-pagination>
      </div>
    </b-card>
  </div>
</template>

<script>
import clienteAxios from "../config/axios";

export default {
  name: "Random",
  data() {
    return {
      cantidad: null,
      randomArray: [],
      pageNum: 0,
      pageSize: 6,
    };
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      if (this.cantidad <= 0) {
        alert("Ingrese una cantidad positiva!");
        return;
      }
      if (this.cantidad > 1000000) {
        alert("Ingrese una cantidad menor o igual a un millon!");
      }

      let randomNumbers = (
        await clienteAxios.get("/randomPython", {
          params: {
            cantidad_muestra: this.cantidad,
          },
        })
      ).data;

      this.randomArray = randomNumbers;
    },
    isNumber: function (evt) {
      evt = evt ? evt : window.event;
      var charCode = evt.which ? evt.which : evt.keyCode;
      if (
        charCode > 31 &&
        (charCode < 48 || charCode > 57) &&
        charCode !== 46
      ) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.random {
  width: 100%;
  height: 100%;
  max-width: 500px;
}

.table-container {
  max-height: 40vh !important;
  overflow: auto;
  margin-top: 10px;
}

.pagination-container {
  width: 100%;
}
</style>
