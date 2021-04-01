<template>
<div>
<h2 class="van-doc-demo-block__title">基础信息</h2>
  <van-cell-group>
  <van-cell title="用户昵称" v-model="username" />
</van-cell-group>

  <div class="box">
    <van-button type="info" @click="logout">退出登录</van-button>
  </div>

  </div>
</template>

<script>
  export default {
    name: "Mine",
    data () {
            return {
              username:this.$store.getters.getUsername,
        };},
    methods: {
      logout(){
        this.$store.commit('logout')
      }
    }
  }
  
</script>

<style scoped>
.box {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 500%;
}

.user {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 300%;
}

.van-doc-demo-block__title {
    margin: 0;
    padding: 32px 16px 16px;
    color: rgba(69, 90, 100, 0.6);
    font-weight: normal;
    font-size: 14px;
    line-height: 16px;
}
</style>
