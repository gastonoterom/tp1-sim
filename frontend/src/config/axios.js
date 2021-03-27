const axios = require("axios").default;

const clienteAxios = axios.create({
  baseURL: "",
});

export default clienteAxios;
