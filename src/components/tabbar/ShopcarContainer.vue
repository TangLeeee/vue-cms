<template>
  <div class="shopcar-container">
    <div class="goods-list">
      <div class="mui-card">
        <div class="mui-card-content">
          <div class="mui-card-content-inner">
            <mt-switch></mt-switch>
            <img src="//i1.mifile.cn/a1/pms_1524621350.77238418!220x220.jpg">
            <div class="info">
              <h1>一代神机小米6，全网通版64G</h1>
              <p>
                <span class="price">￥1999</span>
                <numbox :initcount="$store.getters.getGoodsCount['90']"></numbox>
                <a>删除</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mui-card">
      <div class="mui-card-content">
        <div class="mui-card-content-inner jiesuan">
          <div class="left">
            <p>总计（不含运费）</p>
            <p>已勾选商品 <span class="red">0</span> 件，总价 <span class="red">￥0</span></p>
          </div>
          <mt-button type="danger">结算</mt-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import numbox from '../subcomponents/shopcar_numbox'

  var obj = localStorage.getItem('cart')

  export default {
    name: "ShopcarContainer",
    components:{
      numbox
    }
  }
</script>

<style scoped lang="scss">
.shopcar-container{
  background-color: #eeeeee;
  overflow: hidden;
  .goods-list{
    .mui-card-content-inner{
      display: flex;
    }
    img{
      width: 60px;
      height: 60px;
    }
    h1{
      font-size: 14px;
    }
    .info{
      display: flex;
      flex-direction: column;
      .price{color:red;font-weight: bold}
    }
  }
  .jiesuan{
    display: flex;
    align-items: center;
    justify-content: space-between;
    .red{
      color: red;
      font-weight: bold;
      font-size: 16px;
    }
  }
}
</style>
