<template>
  <div class="multiplicative">
    <b-card
      class="bcard-index"
      title="Generador de números aleatorios"
      header="Simulación - UTN FRC"
      sub-title="Método Multiplicativo"
    >
      <b-form>
        <b-form-group
          id="input-group-2"
          label="Ingrese el valor de la semilla: "
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
        <b-form-group
          id="input-group-2"
          label="Ingrese la constante multiplicativa: "
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            placeholder="Ingresar el valor de la constante no nula"
            required
            v-model="k"
            @keypress="isNumber($event)"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="input-group-2"
          label="Ingrese la g: "
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            placeholder="Ingresar g"
            required
            v-model="g"
            @keypress="isNumber($event)"
          ></b-form-input>
        </b-form-group>
      </b-form>

      <b-button
        variant="primary"
        style="margin: 10px 43%"
        type="submit"
        @click="onSubmit"
      >
        Generar
      </b-button>
    </b-card>
  </div>
</template>

<script>
import clienteAxios from "../config/axios";
export default {
  name: "Multiplicative",
  data() {
    return {
      semilla: 0,
      k: 0,
      g: 0,
      pageNum: 0,
      pageSize: 5,
    };
  },
  props: ["isNumber", "coprimos"],
  methods: {
    async onSubmit(event) {
      event.preventDefault();

      await clienteAxios.get(
        `/randomMultiplicativo?semilla=${this.semilla}&k=${this.k}&g=${this.g}`
      );
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.multiplicative {
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
