import { createRouter, createWebHistory } from "vue-router";
import SignIn from "../components/SignIn"
import SignUp from "../components/SignUp"
import HomePage from "../components/HomePage"
import NamesList from "../components/NamesList"



const routes = [
    {
        path: "/SignIn",
        name: "SignIn",
        component: SignIn,
    },
    {
        path: "/Signup",
        name: "SignUp",
        component: SignUp,
    },
    {
        path: "/HomePage",
        name: "HomePage",
        component: HomePage,
    },
    {
        path: "/NamesList",
        name: "NamesList",
        component: NamesList,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;