import axios from "axios";

const clienteAxios = axios.create({
  baseURL: "//tp1-sim.gastonotero.com",
});

export default clienteAxios;
