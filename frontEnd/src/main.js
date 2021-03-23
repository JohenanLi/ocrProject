import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index.js'
import './assets/lib/flexible.js'
import './assets/lib/Chart'

/**使用vux的插件提示功能*/
import  { ToastPlugin } from 'vux'
import { Tabbar, TabbarItem, NavBar, Tab, Tabs, Grid, GridItem, Divider, DropdownMenu, Toast,
    DropdownItem, Switch, Button, List, Cell, CellGroup, PullRefresh, Row, Col, Field, ActionSheet,  Image} from "vant"
import 'vant/lib/index.css'
import http from './utils/http'
import {
    Layout,
    Input,
    Upload,
    Icon
  } from 'ant-design-vue'
  import 'ant-design-vue/dist/antd.css';
//   import VueHighlightJS from 'vue-highlightjs'
// Vue.use(VueHighlightJS)
Vue.use(Icon)
Vue.use(Button)
Vue.use(Layout)
Vue.use(Input)
Vue.use(Row)
Vue.use(Col)
Vue.use(Icon)
Vue.use(Divider)
Vue.use(Upload)
Vue.use(ToastPlugin)
Vue.use(Tabbar).use(TabbarItem).use(NavBar).use(Tab).use(Tabs).use(Grid).use(GridItem).use(Divider).use(DropdownMenu)
    .use(DropdownItem).use(Switch).use(Button).use(List).use(Cell).use(CellGroup).use(PullRefresh).use(Row).use(Col)
    .use(Field).use(ActionSheet).use(Icon).use(Image).use(Toast);

Vue.config.productionTip = false

Vue.prototype.$http = http;
new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
})
