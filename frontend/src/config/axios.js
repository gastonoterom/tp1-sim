const axios = require("axios").default;

const clienteAxios = axios.create({
  baseURL: "https://tp1-sim.herokuapp.com/",
});

export default clienteAxios;
