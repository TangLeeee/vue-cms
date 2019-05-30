<template>
  <div class="newsinfo-container">
    <h3 class="title">{{ newsinfo.title }}</h3>
    <p class="subtitle">
      <span>{{ newsinfo.add_time }}</span>
      <span>{{ newsinfo.click }}</span>
    </p>
    <hr>

    <div class="content">
      {{ newsinfo.content }}
    </div>
  </div>
</template>

<script>
import { Toast } from 'mint-ui'
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
  methods:{
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
