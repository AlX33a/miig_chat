import { createRouter, createWebHistory } from "vue-router";
import Sign_In from "../components/Sign_In"
import Sign_Up from "../components/Sign_Up"

const routes = [
    {
        path: "/Sign_In",
        name: "Sign_In",
        component: Sign_In,
    },
    {
        path: "/Sign_up",
        name: "Sign_Up",
        component: Sign_Up,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;