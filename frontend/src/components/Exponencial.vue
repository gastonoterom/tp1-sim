<template>
  <div class="exponencial">
    <b-card
      class="bcard-index"
      title="Generador de Números Aleatorios"
      header="Simulación - UTN FRC"
      sub-title="Método Exponencial"
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
              label="Cantidad a generar: "
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                placeholder=""
                required
                v-model="cantidadGenerar"
                @keypress="isNumber($event)"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-form-row>
        <b-form-row
          ><b-col>
            <b-form-group
              id="input-group-2"
              label="Media: "
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                placeholder=""
                required
                v-model="media"
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
          id="exponencial-table"
          :per-page="pageSize"
          :current-page="pageNum"
          striped
          hover
          :items="randomDataProvider"
        ></b-table>
        <p>
          Tabla N°1: Serie de numeros aleatorios generados por el metodo
          exponencial
        </p>
      </div>
      <div v-if="randomHash" class="pagination-container">
        <b-pagination
          v-model="pageNum"
          :total-rows="cantidadFilas"
          :per-page="pageSize"
          aria-controls="exponencial-table"
          align="center"
        ></b-pagination>
      </div>
    </b-card>
    <Histogram
      style="margin-top: 10px"
      v-if="randomHash"
      :key="randomHash"
      :histogramProps="histogramProps"
    >
    </Histogram>
  </div>
</template>

<script>
import clienteAxios from "../config/axios";
import Histogram from "./Histogram.vue";
export default {
  components: { Histogram },
  name: "Exponencial",
  data() {
    return {
      pageNum: 1,
      pageSize: 5,
      cantidadGenerar: 20,
      semilla: 0,
      seed: 0,
      media: 1,
      randomHash: false,
      cantidadFilas: 0,
      histogramProps: {
        type: "exponencial",
        cantidad: 0,
        random_props: {
          semilla: 0,
          media: 1,
          cantidad: 0,
        },
      },
    };
  },
  props: ["isNumber"],

  methods: {
    async randomDataProvider(ctx) {
      if (this.cantidad == "") return;

      const promise = clienteAxios.get(
        `/api/randomExponencial?pagina=${ctx.currentPage}&pageSize=${this.pageSize}&cantidad_muestra=${this.cantidadGenerar}&seed=${this.semilla}&media=${this.media}`
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

      if (this.cantidadGenerar > 1000000 || this.cantidadGenerar <= 0) {
        alert("La cantidad a generar debe estar entre 0 y 1000000!");
        return;
      }

      this.histogramProps = {
        type: "exponencial",
        cantidad: this.cantidadGenerar,
        random_props: {
          semilla: this.semilla,
          media: this.media,
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
.exponencial {
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
