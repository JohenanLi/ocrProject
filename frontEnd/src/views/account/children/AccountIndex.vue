<template>
    <div class="account-wrap">
        <head-title :title="'记账：'"></head-title>
        <div class="go-btn-box">
            <a href="#/account/consumption" class="go-account go-consumption">消费</a>
            <a href="#/account/earn" class="go-account go-earn">入账</a>
            <a href="#/account/scan" class="go-account go-scan">扫描</a>
        </div>
    </div>
</template>
<script>
    import types from '../../../store/mutation-types'
    import headTitle from '../../../components/head-title.vue'
    export default {
        name: 'account_index',
        created () {
            this.setNavIndex();
        },
        components: {
            headTitle
        },
        methods: {
            setNavIndex () {
                this.$store.commit(types.SET_NAV_INDEX,'2')
            }
        }
    }
</script>
<style lang="scss">
    @import "../../../assets/scss/define";
    .go-btn-box{
        @extend %pa;
        @extend %tac;
        @extend %f14;
        @extend %cfff;
        @extend %l0;
        @extend %r0;
        @extend %t50;
        transform: translate3d(0,-50%,0);
    }
    .go-account{
        @extend %db;
        @extend %cp;
        @extend %cfff;
        margin: 0 auto 20px;
        width: 150px;
        height: 35px;
        line-height: 35px;
        border-radius: 5px;
        &.go-consumption{
            background-color: #e96e6e;
            box-shadow: 0 3px 0 0 rgb(247, 70, 70);
        }
        &.go-earn{
            background-color: #41d5e9;
            box-shadow: 0 3px 0 0 #07caec;
        }
        &.go-scan{
            background-color: #e28ee2;
            box-shadow: 0 3px 0 0 #e480b2;
        }
    }
</style>

