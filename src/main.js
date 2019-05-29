// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import router from './router/index'
// 需要mint导入样式才能生效
import 'mint-ui/lib/style.css'
import MintUI from 'mint-ui'
// 导入MUI样式
import './lib/mui/css/mui.min.css'
import './lib/mui/css/icons-extra.css'
// 导入axios
import axios from 'axios'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(MintUI)
Vue.prototype.$http = axios

new Vue({
  el: '#app',
  router,
  render: c => c(App)
})
