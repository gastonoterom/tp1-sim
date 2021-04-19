<template>
  <div class="index">
    <b-card
      class="bcard-index"
      title="Trabajo Practico N° 3"
      header="Simulación - UTN FRC"
      sub-title="Integrantes"
    >
      <b-card-text :key="integrante" v-for="integrante in integrantes">{{
        integrante
      }}</b-card-text>
      <div class="logo-container">
        <img class="logo" src="@/assets/utn.jpg" />
      </div>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "Index",
  data() {
    return {
      integrantes: [
        "Belelli, Federico - 64932",
        "Cesar Nieto, Manuel - 81095",
        "Mendez Nole, Ignacio - 78599",
        "Otero, Gastón - 78710",
        "Peña Beltrami, Gustavo - 81074",
      ],
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.index {
  width: 100%;
  height: 100%;
  max-width: 500px;
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
}
.logo {
  width: 120px;
  height: auto;
}
</style>
