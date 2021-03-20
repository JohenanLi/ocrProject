<template>
  <div class="container-view">
    <nav-bar></nav-bar>
    <section
      style="padding: 30px 30px; display: flex; flex-flow: column nowrap"
    >
      <div style="font-size: 20px; font-weight: bold">手机号密码登录</div>
      <div>
        <van-cell-group>
          <van-field
            v-model="tel"
            clearable
            placeholder="请输入手机号"
            style="background-color: WhiteSmoke"
            ref="phone"
          >
          </van-field>
          <van-field
            v-model="pwd"
            center
            clearable
            placeholder="请输入密码"
            style="background-color: WhiteSmoke"
            ref="pwd"
            type="password"
          >
          </van-field>
        </van-cell-group>
        <span style="color: red" v-show="errMsg">{{ errMsg }}</span>
      </div>
      <div style="background-color: DarkGray">
        <van-button :type="type" block :disabled="loginDisabled" @click="login"
          >登录</van-button
        >
      </div>
    </section>
  </div>
</template>

<script>
// 引入组件Cell CellGroup
import { Cell, CellGroup, Icon } from "vant";
import NavBar from "@/components/NavBar";
import {loginByPwd} from "@/api/index";
export default {
  name: "LoginByPwd",
  components: {NavBar},
  mounted() {
    // 输入框聚焦
  
    if (!this.tel) {
      this.$refs.phone.focus();
    } else {
      this.$refs.pwd.focus();
    }
  },
  watch: {
    // 监听手机号和密码输入框，修改登录按钮状态和类型
    pwd(newVal) {
      if (newVal.length > 0) {
        this.loginDisabled = false;
        this.type = "danger";
      } else {
        this.loginDisabled = "disabled";
        this.type = "default";
      }
    },
    tel(newVal, oldVal) {
 
      if (this.pwd.length > 0) {
        this.loginDisabled = false;
        this.type = "danger";
      } else {
        this.loginDisabled = "disabled";
        this.type = "default";
      }
    },
  },
  data() {
    return {
      // 登录按钮类型
      type: "default",
      // 手机号
      tel: this.$store.state.phone,
      // 密码
      pwd: "",
      // 错误提示信息
      errMsg: "",
      // 登录按钮是否禁用
      loginDisabled: "disabled",
    };
  },
  methods: {
    // 登录
    login() {
      let params = {
        username: this.tel,
        password: this.pwd,
      };
      loginByPwd(params).then((res) => {
        
        if (res.data.code !== 200) {
          console.log(res);
          this.errMsg = res.data.msg;
          // 密码输入错误时重新聚焦输入框
          this.$refs.pwd.focus();
        } else {
          console.log(res.data.data)
          this.$store.commit("login", res.data.data);
        }
      });
    },
  },
};
</script>

<style scoped>
section div {
  margin-bottom: 16px;
}
</style>
</template>
