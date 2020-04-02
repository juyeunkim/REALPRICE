import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import infiniteScroll from "vue-infinite-scroll";
import router from "./router";
import store from "./store";
import VueSimpleAlert from "vue-simple-alert";

Vue.config.productionTip = false;
Vue.use(infiniteScroll);
Vue.use(VueSimpleAlert);

new Vue({
    vuetify,
    router,
    store,
    render: h => h(App)
}).$mount("#app");