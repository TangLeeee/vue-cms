import VueRouter from 'vue-router'
import HomeContainer from '../components/tabbar/HomeContainer'
import MemberContainer from '../components/tabbar/MemberContainer'
import ShopcarContainer from '../components/tabbar/ShopcarContainer'
import SearchContainer from '../components/tabbar/SearchContainer'
import NewsList from "../components/news/NewsList";
import NewsInfo from "../components/news/NewsInfo";

export default new VueRouter({
  routes: [
    {path: '/', redirect: '/index'},
    {path: '/index', component: HomeContainer},
    {path: '/member', component: MemberContainer},
    {path: '/shopcar', component: ShopcarContainer},
    {path: '/search', component: SearchContainer},
    {path: '/index/newslist', component: NewsList},
    {path: '/index/newsinfo/:id', component: NewsInfo}
  ],
  linkActiveClass: 'mui-active' //魔改默认路由高亮的类，默认的为router-link-active
})
