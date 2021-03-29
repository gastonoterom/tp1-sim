<template>
  <div id="app">
    <NavBar />
    <div class="body">
      <router-view :isNumber="isNumber" :coprimos="coprimos" />
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
  methods: {
    coprimos(num1, num2) {
      const smaller = num1 > num2 ? num1 : num2;
      for (let ind = 2; ind < smaller; ind++) {
        const condition1 = num1 % ind === 0;
        const condition2 = num2 % ind === 0;
        if (condition1 && condition2) {
          return false;
        }
      }
      return true;
    },
    isNumber: function (evt) {
      evt = evt ? evt : window.event;
      var charCode = evt.which ? evt.which : evt.keyCode;
      if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
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
