import Vue from "vue";
import VueCookies from "vue-cookies";

import App from "./App.vue";

Vue.use(VueCookies);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
