<template>
  <div class="container-view">
    <head-title :title="'分析：'"></head-title>
    <div class="chart-wrap">
      <Scroller 
        lock-x
        height="-118"
        :scrollbarY="true"
        @on-scroll="onScroll"
        ref="chartScrollEvent"
      >
        <div class="chart-con">
          <div class="chart-item">
            <h2 class="chart-title">消费状况：</h2>
            <canvas id="consumption-chart" width="400" height="400"></canvas>
          </div>
          <div class="chart-item">
            <h2 class="chart-title">入账状况：</h2>
            <canvas id="earn-chart" width="400" height="400"></canvas>
          </div>
          <div>
            <h2 class="chart-title">test</h2>
            <canvas id="myChart" width="400" height="400"></canvas>
          </div>
        </div>
      </Scroller >
    </div>
  </div>
</template>
<script>
import types from "../../store/mutation-types";
import headTitle from "../../components/head-title.vue";
import Util from "../../assets/lib/Util";
import { Scroller } from "vux";
import { queryAccount } from "@/api/index";
export default {
  name: "chart",
  data() {
    return {
      consumption_chart_arr: [0, 0, 0, 0, 0, 0, 0, 0],
      earn_chart_arr: [0, 0, 0],
    };
  },
  components: {
    Scroller,
    headTitle,
  },
  created() {
    this.$store.commit(types.SET_NAV_INDEX, "4");
    this.fetchBillData();
    this.$nextTick(() => {
    //   var dataText =  [12, 19, 3, 5, 2, 3]
    //   console.log(dataText)
      var consumption_data = {
        labels: [
          "水果零食",
          "餐饮伙食",
          "出行旅游",
          "网上购物",
          "生活日常",
          "租房水电",
          "医疗药物",
          "其它消费",
        ],
        datasets: [
          {
            data: this.consumption_chart_arr,
            backgroundColor: [
              "#999933",
              "#FF9933",
              "#FF6666",
              "#36A2EB",
              "#666699",
              "#CCFF00",
              "#66CCCC",
              "#663366",
            ],
          },
        ],
      };
      var earn_data = {
        labels: ["基本工资", "公司福利", "其它入账"],
        datasets: [
          {
            data: this.earn_chart_arr,
            backgroundColor: ["#13CE66", "#F7BA2A", "#FF4949"],
          },
        ],
      };
      var consumption_ctx = document
        .getElementById("consumption-chart")
        .getContext("2d");
      var earn_ctx = document.getElementById("earn-chart").getContext("2d");
      console.log(consumption_data, earn_data);
      var conChart = new Chart(consumption_ctx, {
        type: "pie",
        data: consumption_data,
      });

      new Chart(earn_ctx, {
        type: "pie",
        data: earn_data,
      });
      var ctx = document.getElementById("myChart").getContext("2d");
      var myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
          datasets: [
            {
              label: "# of Votes",
              data: [6879987, 0, 0, 0, 0, 0, 12344, 0],
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)",
              ],
              borderColor: [
                "rgba(255,99,132,1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)",
              ],
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
        },
      });
    });
  },
  methods: {
    onScroll(pos) {
      this.scrollTop = pos.top;
    },
    fetchBillData() {
      queryAccount().then((res) => {
        var bill_arr = res.data;
        bill_arr.forEach((item, index) => {
          if (item.account_type == "水果零食") {
            this.consumption_chart_arr[0] =
              this.consumption_chart_arr[0] + item.sum_value;
          } else if (item.account_type == "餐饮伙食")
            this.consumption_chart_arr[1] =
              this.consumption_chart_arr[1] + item.sum_value;
          else if (item.account_type == "出行旅游")
            this.consumption_chart_arr[2] =
              this.consumption_chart_arr[2] + item.sum_value;
          else if (item.account_type == "网上购物")
            this.consumption_chart_arr[3] =
              this.consumption_chart_arr[3] + item.sum_value;
          else if (item.account_type == "生活日常")
            this.consumption_chart_arr[4] =
              this.consumption_chart_arr[4] + item.sum_value;
          else if (item.account_type == "租房水电")
            this.consumption_chart_arr[5] =
              this.consumption_chart_arr[5] + item.sum_value;
          else if (item.account_type == "医疗药物")
            this.consumption_chart_arr[6] =
              this.consumption_chart_arr[6] + item.sum_value;
          else if (item.account_type == "其它消费")
            this.consumption_chart_arr[7] =
              this.consumption_chart_arr[7] + item.sum_value;
          else if (item.account_type == "基本工资")
            this.earn_chart_arr[0] = this.earn_chart_arr[0] + item.sum_value;
          else if (item.account_type == "公司福利")
            this.earn_chart_arr[1] = this.earn_chart_arr[1] + item.sum_value;
          else if (item.account_type == "其它入账")
            this.earn_chart_arr[2] = this.earn_chart_arr[2] + item.sum_value;
        });
      });
    },
  },
};
</script>
<style lang="scss">
@import "../../assets/scss/define";
.chart-wrap {
  @extend %oya;
  @extend %pa;
  @extend %w100;
  @extend %ios;
  @extend %b0;
  top: 64px;
}
.chart-title {
  @extend %f14;
  @extend %fwn;
  color: #58b7ff;
}
.chart-item {
  padding: 10px;
}
</style>
