<template>
  <div class="newsinfo-container">
    <!-- 大标题 -->
    <h3 class="title">{{ newsinfo.title }}</h3>

    <!-- 子标题 -->
    <p class="subtitle">
      <span>时间：{{ newsinfo.add_time | dateFormat }}</span>
      <span>点击次数:{{ newsinfo.click }}</span>
    </p>
    <hr>

    <!-- 内容区域 -->
    <div class="content">
      {{ newsinfo.content }}
    </div>

    <!-- 评论区域 -->
    <comment-box :id="this.id">

    </comment-box>
  </div>
</template>

<script>
import { Toast } from 'mint-ui'
import comment from '../subcomponents/comment'
export default {
  name: "NewsInfo",
  data(){
    return {
      id: this.$route.params.id,
      newsinfo: {}
    }
  },
  created(){
    this.getNewsInfo()
  },
  methods: {
    getNewsInfo(){
      this.$http.get('/api/getnew/' + this.id).then(result => {
        // console.log(result)
        if(result.status === 200){
          this.newsinfo = result.data.message
          // console.log(this.newsinfo)
        }else{
          Toast('获取失败')
        }
      })
    }
  },
  components: {  //用来注册子组件节点
    'comment-box' : comment
  }
}
</script>

<style scoped lang="scss">
.newsinfo-container{
  padding: 0 4px;
  .title{
    font-size: 16px;
    text-align: center;
    margin: 15px 0;
  }
  .subtitle{
    font-size: 13px;
    color: #226aff;
    display: flex;
    justify-content: space-between;
  }
  .content{

  }
}
</style>
