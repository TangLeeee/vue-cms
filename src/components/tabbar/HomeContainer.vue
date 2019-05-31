<template>
  <div>
    <!-- 轮播图区域 -->
    <mt-swipe :auto="4000" :continuous="true">
      <mt-swipe-item v-for="item in lunbotuList" :key="item.id">
        <img alt="" :src="item.img">
      </mt-swipe-item>
    </mt-swipe>

    <!-- 六宫格区域 -->
    <ul class="mui-table-view mui-grid-view mui-grid-9">
      <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="/index/newslist">
        <img src="../../images/menu1.png" alt="">
        <div class="mui-media-body">新闻资讯</div></router-link>
      </li>
      <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="/index/photolist">
        <img src="../../images/menu2.png" alt="">
        <div class="mui-media-body">图片分享</div></router-link>
      </li>
      <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="/index/goodslist">
        <img src="../../images/menu3.png" alt="">
        <div class="mui-media-body">商品购买</div></router-link>
      </li>
      <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="#">
        <img src="../../images/menu4.png" alt="">
        <div class="mui-media-body">留言反馈</div></router-link>
      </li>
      <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="#">
        <img src="../../images/menu5.png" alt="">
        <div class="mui-media-body">视频专区</div></router-link>
      </li>
      <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="#">
        <img src="../../images/menu6.png" alt="">
        <div class="mui-media-body">联系我们</div></router-link>
      </li>
    </ul>

  </div>
</template>

<script>
import { Toast } from 'mint-ui'

export default {
  name: "HomeContainer",
  data(){
    return {
      lunbotuList: []
    }
  },
  created(){
    this.getLunbotu()
  },
  methods: {
    getLunbotu(){
      this.$http.get('/').then(result => {
        // console.log(result)
        if(result.status === 200){
          this.lunbotuList = result.data.messages;
          // console.log(this.lunbotuList)
        } else {
          Toast('加载轮播图失败')
        }
      })
    }
  }


}
</script>

<style scoped lang="scss">
  .mint-swipe{
    height: 200px
  }

  .mint-swipe-item{
    &:nth-child(1){
      background-color: #1c7430;
    }
    &:nth-child(2){
      background-color: cyan;
    }
    &:nth-child(3){
      background-color: #4e555b;
    }
    img{
      height: 100%;
      width: 100%;
    }
  }

  .mui-grid-view.mui-grid-9{
    background-color: white;
    img{
      width: 60px;
      height: 60px;
    }
    .mui-media-body{
      font-size: 13px;
    }
  }
  .mui-grid-view.mui-grid-9 .mui-table-view-cell{
    border: 0;
  }
</style>
