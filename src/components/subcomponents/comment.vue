<template>
  <div class="comment-container">
    <h3>发表评论</h3>
    <hr>
    <label><textarea placeholder="请输入评论内容（最多输入120字）" v-model="msg"></textarea></label>

    <mt-button type="primary" size="large" @click="postComment">发表评论</mt-button>

    <div class="comment-list" v-for="(item, i) in comments">
      <div class="comment-item">
        <div class="comment-title">
          第{{ i+1 }}楼&nbsp;&nbsp;用户：匿名用户&nbsp;&nbsp;发表时间：{{ item.addtime }}
        </div>
        <div class="comment-body">
          {{ item.content }}
        </div>
      </div>
    </div>

    <mt-button type="danger" size="large" plain @click="getMore">加载更多</mt-button>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui'

  export default {
    name: "comment",
    data(){
      return{
        pageIndex: 1,  //默认为1
        comments: [],  //所有评论
        msg: ''        //textarea输入的内容
      }
    },
    props: ['id'],
    created(){
      this.getComments()
    },
    methods:{
      getComments(){    //获取评论
        this.$http.get('/api/getcomments/' + this.pageIndex)
          .then(result => {
            if(result.status === 200){
              // this.comments = result.data.messages
              // 再点击加载更多后，应该使用contact拼接上新数组，防止覆盖
              this.comments = this.comments.concat(result.data.messages)
              // console.log(this.comments)
            }else{
              Toast('加载失败')
            }
          })
      },
      getMore(){
        this.pageIndex = this.pageIndex + 1;
        this.getComments()
        this.pageIndex = 0;
      },
      postComment(){
        if(this.msg.trim().length === 0) return Toast("评论内容不能为空")
        var cmt = { user_name: '匿名用户', addtime: Date.now(), content: this.msg.trim()}
        this.comments.unshift(cmt)
        // this.$http.post('' + this.$route.parmas.id, {
        //   content: this.msg
        // }, ).then(reuslt => {
        //   if(reuslt.status === 200){
        //     var cmt = { user_name: '匿名用户', add_time: Date.now(), content: this.msg.trim()}
        //     this.comments.unshift(cmt)
        //   }
        // })
      }
    }
  }
</script>

<style scoped lang="scss">
  .comment-container{
    h3{
      font-size: 18px;
    }
    textarea{
      font-size: 14px;
      height: 85px;
      margin: 0;
    }
    .comment-list{
      margin: 10px 0;
      font-size: 13px;
      .comment-title{
        background-color: #ccc;
        line-height: 30px;
      }
      .comment-body{
        line-height: 30px;
        text-indent: 2em;
      }
    }
  }
</style>
