import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../components/Index";
import Random from "../components/Random";
import Linear from "../components/Linear";
import Multiplicative from "../components/Multiplicative";
import JiCuadrado from "../components/JiCuadrado";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Inicio",
    component: Index,
  },
  {
    path: "/random",
    name: "Random Generator",
    component: Random,
  },
  {
    path: "/linear",
    name: "Linear",
    component: Linear,
  },
  {
    path: "/multiplicative",
    name: "Multiplicative",
    component: Multiplicative,
  },
  {
    path: "/jicuadrado",
    name: "JiCuadrado",
    component: JiCuadrado,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
