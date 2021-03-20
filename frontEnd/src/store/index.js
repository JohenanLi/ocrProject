/**
 * vuex数据控制中心
 * */
import Vue from 'vue'
import Vuex from 'vuex'
import types from './mutation-types.js'
import router from "@/router"
import { Toast } from "vant"
Vue.use(Vuex);
Vue.use(Toast);

/**
 * 数据存储
 * */
const state = {
    user_id:0,
    username:"",
    is_not_first: true,
    animate_name: 'vux-pop-in',
    nav_index: 1,
    phone: localStorage.getItem("phone"),
};

/**
 * 模块
 * */
const modules = {

};

/*getters*/
const getters = {
    //get方法
    getUser_id: state => state.user_id
};

/**
 * 提交同步请求
 * */
const mutations = {
    /**全局判断是否是第一次进入*/
    [types.JUDGE_IS_NOT_FIRST](state, is_not_first) {
        state.is_not_first = is_not_first;
    },
    /**全局判断前进回退的动画*/
    [types.SET_ANIMATE_NAME](state, animate_name) {
        state.animate_name = animate_name;
    },
    /**判断菜单栏选择情况*/
    [types.SET_NAV_INDEX](state, nav_index) {
        state.nav_index = nav_index;
    },
    /**
  * 登录
  * @param state
  * @param token
  */
    login(state, data) {
        // state.token = data.token;
        // 跳转到首页
        state.user_id = data.id;
        state.username = data.username;
        router.replace('/').catch(err => console.warn(err));
        Toast('登录成功');
    },

    /**
   * 更新手机号
   * @param state
   * @param phone
   */
    updatePhone(state, phone) {
        state.phone = phone;
        localStorage.setItem("phone", phone)
    },
}


export default new Vuex.Store({
    state,
    modules,
    mutations,
    getters,
    types
})
