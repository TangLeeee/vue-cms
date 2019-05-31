<template>
  <div>
    <ul class="mui-table-view">
				<li class="mui-table-view-cell mui-media" v-for="item in newsList">
					<router-link :to="`/index/newsinfo/` + item.id">
						<img class="mui-media-object mui-pull-left" src="https://avatars1.githubusercontent.com/u/28701321?s=40&v=4">
						<div class="mui-media-body">
							<h4>{{ item.title }}</h4>
							<p class='mui-ellipsis'>
                <span>{{ item.add_time | dateFormat }}</span>
                <span>点击：{{ item.click }}</span>
              </p>
						</div>
					</router-link>
				</li>

			</ul>
  </div>
</template>

<script>
import { Toast } from 'mint-ui'

export default {
  name: "NewsList",
  data(){
    return {
      newsList: []
    }
  },
  created(){
    this.getNewsList()
  },
  methods: {
    getNewsList(){
      this.$http.get('/api/getnewslist').then(result => {
        // console.log(result)
        if(result.status === 200){
          this.newsList = result.data.messages
        }else{
          Toast('加载失败')
        }
      })
    }
  }
}
</script>

<style scoped lang="scss">
.mui-table-view{
  li{
    h4{
      font-size: 14px;
  }

    .mui-ellipsis{
      font-size: 12px;
      color: #226aff;
      display: flex;
      justify-content: space-between;
    }
  }

}
</style>
