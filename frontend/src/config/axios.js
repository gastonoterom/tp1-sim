import axios from "axios";

const clienteAxios = axios.create({
  baseURL: "http://18.224.59.31:5000",
});

export default clienteAxios;
