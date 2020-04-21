import Vue from "vue";
import Vuex from "vuex";
import data from "./modules/data";
import session from "./modules/session";
import app from "./modules/app";
import PersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        data,
        app,
        session
    },
    plugins: [
        PersistedState({
            path: ['session'],
        })
    ]
});