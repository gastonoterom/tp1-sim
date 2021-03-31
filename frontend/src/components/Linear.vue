<template>
  <div class="linear">
    <b-card
      class="bcard-index"
      title="Generador de Números Aleatorios"
      header="Simulación - UTN FRC"
      sub-title="Método Lineal"
    >
      <b-form>
        <b-form-row
          ><b-col>
            <b-form-group
              id="input-group-2"
              label="Semilla: "
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                placeholder="Ingresar semilla"
                required
                v-model="semilla"
                @keypress="isNumber($event)"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col
            ><b-form-group
              id="input-group-2"
              label="Constante Multiplicativa: "
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                placeholder="Ingresar el valor de la constante no nula"
                required
                v-model="valorK"
                @keypress="isNumber($event)"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-form-row>
        <b-form-row>
          <b-col
            ><b-form-group
              id="input-group-2"
              label="Valor C:"
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                required
                v-model="valorC"
                @keypress="isNumber($event)"
              ></b-form-input> </b-form-group
          ></b-col>
          <b-col>
            <b-form-group
              id="input-group-2"
              label="Valor G: "
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                placeholder="Ingresar g"
                required
                v-model="valorG"
                @keypress="isNumber($event)"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-form-row>
        <b-form-row
          ><b-col>
            <b-form-group
              id="input-group-2"
              label="Cantidad a generar: "
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                placeholder="Ingresar cantidad"
                required
                v-model="cantidadGenerar"
                @keypress="isNumber($event)"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-form-row>
      </b-form>
      <b-button
        variant="primary"
        style="margin: 10px 43%"
        type="submit"
        @click="onSubmit"
      >
        Generar
      </b-button>
      <b-button
        variant="primary"
        style="margin: 10px 46%"
        type="submit"
        @click="unoMas"
      >
        +
      </b-button>
      <div v-if="randomHash" :key="randomHash" class="table-container">
        <p>Cantidad de numeros aleatorios: {{ this.cantidadFilas }}</p>
        <b-table
          id="linear-table"
          :per-page="pageSize"
          :current-page="pageNum"
          striped
          hover
          :items="randomDataProvider"
        ></b-table>
        <p>
          Tabla N°1: Serie de numeros aleatorios generados por el metodo lineal
          multiplicativo
        </p>
      </div>
      <div v-if="randomHash" class="pagination-container">
        <b-pagination
          v-model="pageNum"
          :total-rows="cantidadFilas"
          :per-page="pageSize"
          aria-controls="linear-table"
          align="center"
        ></b-pagination>
      </div>
    </b-card>
    <ji-cuadrado
      style="margin-top: 10px"
      v-if="randomHash"
      :key="randomHash"
      :jiCuadradoProps="jiCuadradoProps"
    >
    </ji-cuadrado>
  </div>
</template>

<script>
import clienteAxios from "../config/axios";
import JiCuadrado from "./JiCuadrado.vue";
export default {
  components: { JiCuadrado },
  name: "Multiplicative",
  data() {
    return {
      semilla: 0,
      valorK: 0,
      valorG: 0,
      valorC: 0,
      pageNum: 0,
      pageSize: 5,
      cantidadGenerar: 20,
      randomHash: null,
      cantidadFilas: 0,
      jiCuadradoProps: {
        type: "linear",
        cantidad: 0,
        random_props: {
          semilla: 0,
          valorK: 0,
          valorG: 0,
          valorC: 0,
          cantidad: 0,
        },
      },
    };
  },
  props: ["isNumber", "coprimos"],

  methods: {
    async randomDataProvider(ctx) {
      if (this.cantidad == "") return;

      const promise = clienteAxios.get(
        `/api/randomLineal?semilla=${this.semilla}&k=${this.valorK}&g=${this.valorG}&c=${this.valorC}&pagina=${ctx.currentPage}&pageSize=${this.pageSize}&cantidad_muestra=${this.cantidadGenerar}`
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
    async unoMas() {
      this.cantidadGenerar++;
      this.onSubmit({ preventDefault: () => {} });
    },
    async onSubmit(event) {
      event.preventDefault();
      // El valor de g debe estar entre 1 y 20 para generar hasta un millon de numeros
      if (this.valorG > 20 || this.valorG <= 0) {
        alert("El valor de la constante G debe estar entre 1 y 20!");
        return;
      }
      if (this.valorK <= 0) {
        alert("El valor de la constante multiplicativa debe ser positivo!");
        return;
      }
      if (this.cantidadGenerar > 1000000 || this.cantidadGenerar <= 0) {
        alert("La cantidad a generar debe estar entre 0 y 1000000!");
        return;
      }
      // C y 2^g (modulo) deben ser coprimos
      if (!this.coprimos(this.valorC, Math.pow(2, this.valorG))) {
        alert("La constante C y el modulo (2^g) deben ser coprimos!");
        return;
      }
      this.jiCuadradoProps = {
        type: "linear",
        cantidad: this.cantidadGenerar,
        random_props: {
          semilla: this.semilla,
          valorG: this.valorG,
          valorK: this.valorK,
          valorC: this.valorC,
        },
      };
      this.randomHash = new Date().getTime();
      this.cantidadFilas = this.cantidadGenerar;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.linear {
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
</style>
