// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// 需要导入样式才能生效
import 'mint-ui/lib/style.css'
import MintUI from 'mint-ui'
import './lib/mui/css/mui.min.css'

Vue.config.productionTip = false
Vue.use(router)
Vue.use(MintUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: c => c(App)
})
