import router from "@/router";
import {Toast} from "vant";
/**全局判断前进回退的动画*/
const SET_ANIMATE_NAME = 'SET_ANIMATE_NAME';
/**判断菜单栏选择情况*/
const SET_NAV_INDEX = 'SET_NAV_INDEX';
/**判断是否是第一次进入应用*/
const JUDGE_IS_NOT_FIRST = 'JUDGE_IS_NOT_FIRST';
export default {
    SET_ANIMATE_NAME,
    SET_NAV_INDEX,
    JUDGE_IS_NOT_FIRST,
      /**
   * 登录
   * @param state
   * @param token
   */
  login(state, data){
    // state.token = data.token;
    // 跳转到首页
    router.replace('/')
        .catch(err => console.warn(err));
    Toast('登录成功');
  },

    /**
   * 更新手机号
   * @param state
   * @param phone
   */
     updatePhone(state, phone){
        state.phone = phone;
        localStorage.setItem("phone", phone)
      },
}
