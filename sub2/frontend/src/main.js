import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import infiniteScroll from "vue-infinite-scroll";
import router from "./router";
import store from "./store";
import VueSimpleAlert from "vue-simple-alert";
import VueSession from 'vue-session'
import naver from 'vue-naver-maps';

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
Vue.use(naver, {
  clientID: 'qNluwcsMdPX0MtIrpXM0lReUcADKjinRdevFwuXE',
  useGovAPI: false, //공공 클라우드 API 사용 (선택)
  subModules:'' // 서브모듈 (선택)
});
