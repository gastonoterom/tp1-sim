<template>
  <div class="random">
    <b-card
      class="bcard-index"
      title="Generador de Números Aleatorios"
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
          <b-col style="text-align: center">
            <b-button style="margin-top: 10px" type="submit" variant="primary"
              >Generar</b-button
            >
            <b-button
              variant="primary"
              style="margin: 10px 46%"
              type="submit"
              @click="unoMas"
            >
              +
            </b-button>
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
        <p>
          Tabla N°1: Serie de numeros aleatorios generados por el metodo nativo
          de python
        </p>
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
    <ji-cuadrado
      style="margin-top: 10px"
      v-if="randomHash"
      :key="randomHash"
      :jiCuadradoProps="jiCuadradoProps"
    ></ji-cuadrado>
  </div>
</template>

<script>
import clienteAxios from "../config/axios";
import JiCuadrado from "./JiCuadrado.vue";
export default {
  components: { JiCuadrado },
  name: "Random",
  props: ["isNumber"],
  data() {
    return {
      jiCuadradoProps: {
        type: "random",
        cantidad: 0,
        random_props: { semilla: 0 },
      },
      cantidad: 0,
      cantidadFilas: 0,
      semilla: new Date().getTime(),
      pageNum: 0,
      pageSize: 5,
      randomHash: null,
    };
  },
  methods: {
    async unoMas() {
      this.cantidad++;
      this.onSubmit({ preventDefault: () => {} });
    },
    async randomDataProvider(ctx) {
      if (this.cantidad == "") return;

      const promise = clienteAxios.get(
        `/api/randomPython?cantidad_muestra=${this.cantidad}&pagina=${ctx.currentPage}&pageSize=${this.pageSize}&seed=${this.semilla}`
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

      this.jiCuadradoProps = {
        type: "random",
        cantidad: this.cantidad,
        random_props: { semilla: this.semilla },
      };
      this.randomHash = new Date().getTime();
      this.cantidadFilas = this.cantidad;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.random {
  width: 100%;
  height: 100%;
  max-width: 800px;
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
