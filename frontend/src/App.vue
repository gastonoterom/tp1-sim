<template>
  <div id="app">
    <NavBar />
    <div class="body">
      <router-view />
    </div>
  </div>
</template>
<script>
import NavBar from "./components/NavBar";
export default {
  name: "App",
  components: {
    NavBar,
  },
  data() {
    return {};
  },
};
</script>
<style>
.body {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px;
}
</style>
