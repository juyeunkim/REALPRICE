import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import infiniteScroll from "vue-infinite-scroll";
import router from "./router";
import store from "./store";
import VueSimpleAlert from "vue-simple-alert";
import VueSession from 'vue-session'

var sessionOptions = {
    persist: true
}

Vue.config.productionTip = false;
Vue.use(infiniteScroll);
Vue.use(VueSimpleAlert);
Vue.use(VueSession, sessionOptions)
new Vue({
    vuetify,
    router,
    store,
    render: h => h(App)
}).$mount("#app");