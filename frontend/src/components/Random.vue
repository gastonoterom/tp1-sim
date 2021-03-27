<template>
  <div class="random">
    <b-card
      class="bcard-index"
      title="Generador de números aleatorios"
      header="Simulación - UTN FRC"
      sub-title="Método nativo de python"
    >
      <b-form @submit="onSubmit" class="form-random">
        <b-form-row>
          <b-col>
            <b-form-group
              id="input-group-1"
              label="Cantidad a generar:"
              label-for="input-1"
            >
            </b-form-group>
          </b-col>
          <b-col>
            <b-form-group
              id="input-group-2"
              label="Semilla:"
              label-for="input-2"
            >
            </b-form-group>
          </b-col>
        </b-form-row>
        <b-form-row>
          <b-col>
            <b-form-input
              id="input-1"
              placeholder="Ingresar cantidad"
              required
              v-model="cantidad"
              @keypress="isNumber($event)"
            ></b-form-input>
          </b-col>
          <b-col>
            <b-form-input
              id="input-2"
              placeholder="Ingresar semilla"
              required
              v-model="semilla"
              @keypress="isNumber($event)"
            ></b-form-input>
          </b-col>
        </b-form-row>
        <b-form-row>
          <b-col>
            <b-button style="margin-top: 10px" type="submit" variant="primary"
              >Generar</b-button
            >
          </b-col>
        </b-form-row>
      </b-form>

      <div v-if="randomHash" :key="randomHash" class="table-container">
        <b-table
          id="random-table"
          :per-page="pageSize"
          :current-page="pageNum"
          striped
          hover
          :items="randomDataProvider"
        ></b-table>
      </div>
      <div v-if="randomHash" class="pagination-container">
        <b-pagination
          v-model="pageNum"
          :total-rows="cantidadFilas"
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
      cantidad: 0,
      cantidadFilas: 0,
      semilla: new Date().getTime(),
      pageNum: 0,
      pageSize: 5,
      randomHash: null,
    };
  },
  methods: {
    async randomDataProvider(ctx) {
      if (this.cantidad == "") return;

      const promise = clienteAxios.get(
        `/randomPython?cantidad_muestra=${this.cantidad}&pagina=${ctx.currentPage}&pageSize=${this.pageSize}&seed=${this.semilla}`
      );
      // Must return a promise that resolves to an array of items
      return promise.then((data) => {
        console.log(data);
        // Pluck the array of items off our axios response
        let items = data.data;

        // Must return an array of items or an empty array if an error occurred
        return items;
      });
    },

    async onSubmit(event) {
      event.preventDefault();
      if (this.cantidad > 1000000 || this.cantidad <= 0) {
        alert(
          "Error: La cantidad de numeros aleatorios a generar debe estar entre 1 y 1000000!"
        );
        return;
      }

      this.randomHash = new Date().getTime();
      this.cantidadFilas = this.cantidad;
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

.form-random {
  margin: 10px;
}
</style>
