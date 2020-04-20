import Vue from "vue";
import Vuex from "vuex";
import data from "./modules/data";
import app from "./modules/app";
import PersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        data,
        app
    },
    plugins: [
        PersistedState({
            path: ['data'],
        })
    ]
});