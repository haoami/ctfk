import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import './plugins'
import store from './store'
import VueParticles from 'vue-particles'
import { sync } from 'vuex-router-sync'
import font from './assets/fonts/iconfont.css'
import ElementUI from 'element-ui' // element-ui的全部组件
import 'element-ui/lib/theme-chalk/index.css'// element-ui的css
import axios from 'axios';
import cookie from "./util/cookie";
Vue.prototype.cookie=cookie;
Vue.use(ElementUI) // 使用elementUI
Vue.config.productionTip = false
Vue.use(VueParticles)
Vue.use(axios);

sync(store, router)
// Vue.http.options.emulateJSON = true
// Vue.http.options.headers = {
//   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
// }
new Vue({
  font,
  router,
  vuetify,
  store,
  render: h => h(App),
}).$mount('#app')
