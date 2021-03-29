<template>
  <div class="random">
    <b-card
      class="bcard-index"
      title="Generador de Números Aleatorios"
      header="Simulación - UTN FRC"
      sub-title="Método Lineal"
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
            v-model="valorK"
            @keypress="isNumber($event)"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="input-group-2"
          label="Ingrese la c:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            required
            v-model="valorC"
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
            v-model="valorG"
            @keypress="isNumber($event)"
          ></b-form-input>
        </b-form-group>
      </b-form>

      <button
        class="btn btn-info"
        style="margin: 10px 43%;"
        type="submit"
        @click="onSubmit"
      >Generar</button>
    </b-card>
  </div>
</template>

<script>
import clienteAxios from '../config/axios';
export default {
  name: "Multiplicative",
  data() {
    return {
      semilla: 0,
      valorK: 0,
      valorG: 2,
      valorC: 0,
      pageNum: 0,
      pageSize: 5,
    };
  },
  methods: {

    async onSubmit(event) {
      event.preventDefault();

      const promise = await clienteAxios.get(
        `/randomLineal?semilla=${this.semilla}&k=${this.valorK}&g=${this.valorG}&c=${this.valorC}`
      );
      console.log(promise);
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
