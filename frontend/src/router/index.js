import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../components/Index";

import Uniforme from "../components/Uniforme";
import Exponencial from "../components/Exponencial";
import Normal from "../components/Normal";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Inicio",
    component: Index,
  },
  {
    path: "/random-uniforme",
    name: "Generador Uniforme",
    component: Uniforme,
  },
  {
    path: "/random-exponencial",
    name: "Generador Exponencial",
    component: Exponencial,
  },
  {
    path: "/random-normal",
    name: "Generador Normal",
    component: Normal,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
