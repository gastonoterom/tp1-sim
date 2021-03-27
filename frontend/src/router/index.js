import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../components/Index";
import Random from "../components/Random";
import Linear from "../components/Linear";
import Multiplicative from "../components/Multiplicative";

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
];

const router = new VueRouter({
    routes,
});

export default router;
