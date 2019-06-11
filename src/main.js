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
import moment from 'moment'
// 注册vuex
import Vuex from 'vuex'

axios.defaults.baseURL = 'http://127.0.0.1:5000/';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(MintUI)
Vue.use(Vuex)
Vue.prototype.$http = axios

var obj = [{"id":90,"count":3,"price":1999,"selected":true}]
obj = JSON.stringify(obj)
localStorage.setItem('cart', obj)
var cart = JSON.parse(localStorage.getItem('cart')) || '[]'

// 创建vuex对象
var store = new Vuex.Store({
  state:{
    cart: cart
  },
  mutations:{ // 使用this.$store.commit('方法名')调用
    addToCart(state, goodsinfo){
      var flag = false

      state.cart.some(item => {
        if(item.id === goodsinfo.id){
          item.count += parseInt(goodsinfo.count)
          flag = true
          return true
        }
      })

      if(!flag){
        state.cart.push(goodsinfo)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    updateGoodsInfo(state, goodsinfo) {
      // 修改购物车中商品的数量值
      // 分析：cart
      state.cart.some(item => {
        if (item.id === goodsinfo.id) {
          item.count = parseInt(goodsinfo.count)
          return true
        }
      })
      // 当修改完商品的数量，把最新的购物车数据，保存到 本地存储中
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    removeFormCar(state, id) {
      // 根据Id，从store 中的购物车中删除对应的那条商品数据
      state.cart.some((item, i) => {
        if (item.id === id) {
          state.cart.splice(i, 1)
          return true;
        }
      })
      // 将删除完毕后的，最新的购物车数据，同步到 本地存储中
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    updateGoodsSelected(state, info) {
      state.cart.some(item => {
        if (item.id === info.id) {
          item.selected = info.selected
        }
      })
      // 把最新的 所有购物车商品的状态保存到 store 中去
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  getters:{
        // 相当于 计算属性，也相当于 filters
    getAllCount(state) {
      var c = 0;
      state.cart.forEach(item => {
        c += item.count
      })
      return c
    },
    getGoodsCount(state) {
      var o = {}
      state.cart.forEach(item => {
        o[item.id] = item.count
      })
      return o
    },
    getGoodsSelected(state) {
      var o = {}
      state.cart.forEach(item => {
        o[item.id] = item.selected
      })
      return o
    },
    getGoodsCountAndAmount(state) {
      var o = {
        count: 0, // 勾选的数量
        amount: 0 // 勾选的总价
      }
      state.cart.forEach(item => {
        if (item.selected) {
          o.count += item.count
          o.amount += item.price * item.count
        }
      })
      return o
    }
  }
})

// 定义全局的过滤器
Vue.filter('dateFormat', function (dataStr, pattern = 'YYYY-MM-DD') {
  return moment(dataStr).format(pattern)
})

new Vue({
  el: '#app',
  router,
  render: c => c(App),
  store
})
