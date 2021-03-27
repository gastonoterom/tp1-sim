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
      </b-form>

      <div :key="cantidad" class="table-container">
        <b-table
          id="random-table"
          :per-page="pageSize"
          :current-page="pageNum"
          striped
          hover
          :items="randomDataProvider"
        ></b-table>
      </div>
      <div class="pagination-container">
        <b-pagination
          v-model="pageNum"
          :total-rows="cantidad"
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
      pageNum: 0,
      pageSize: 5,
    };
  },
  methods: {
    async randomDataProvider(ctx) {
      if (this.cantidad == "") return;

      const promise = clienteAxios.get(
        `/randomPython?cantidad_muestra=${this.cantidad}&pagina=${ctx.currentPage}&pageSize=${this.pageSize}`
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
