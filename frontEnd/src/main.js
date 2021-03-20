import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index.js'
import './assets/lib/flexible.js'
import './assets/lib/Chart'

/**使用vux的插件提示功能*/
import  { ToastPlugin } from 'vux'
import { Tabbar, TabbarItem, NavBar, Tab, Tabs, Grid, GridItem, Divider, DropdownMenu, Toast,
    DropdownItem, Switch, Button, List, Cell, CellGroup, PullRefresh, Row, Col, Field, ActionSheet, Icon, Image} from "vant"
import 'vant/lib/index.css'
import http from '@/utils/http'
Vue.use(ToastPlugin)
Vue.use(Tabbar).use(TabbarItem).use(NavBar).use(Tab).use(Tabs).use(Grid).use(GridItem).use(Divider).use(DropdownMenu)
    .use(DropdownItem).use(Switch).use(Button).use(List).use(Cell).use(CellGroup).use(PullRefresh).use(Row).use(Col)
    .use(Field).use(ActionSheet).use(Icon).use(Image).use(Toast);
Vue.use(axios);
Vue.config.productionTip = false

Vue.prototype.$http = http;
new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
})
