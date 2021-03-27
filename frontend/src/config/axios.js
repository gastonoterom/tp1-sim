const axios = require("axios").default;

const clienteAxios = axios.create({
  baseURL: "http://127.0.0.1:5000",
});

export default clienteAxios;
