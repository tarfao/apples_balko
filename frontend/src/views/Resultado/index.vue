<template>
  <div>
    <v-chart :options="polar" />
  </div>
</template>

<script>
import ECharts from "vue-echarts";
import "echarts/lib/chart/bar";
import "echarts/lib/component/title";

export default {
  name: "resultado",
  components: {
    "v-chart": ECharts,
  },
  data() {
    var dataAxis = [];
    var data = this.$store.state.trees;

    for (let i = 0; i < data.length; i++) {
      dataAxis.push(`A${i+1}`)
    }

    return {
      polar: {
        title: [
          {
            id: "arvores",
            show: true,
            text: "Pés de maçã",
            subtext: "Número de maçãs em cada pé",
          },
        ],
        xAxis: {
          data: dataAxis,
          axisLabel: {
            inside: true,
            textStyle: {
              color: "#fff",
            },
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            show: false,
          },
          z: 10,
        },
        yAxis: {
          axisLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          axisLabel: {
            textStyle: {
              color: "#999",
            },
          },
        },
        dataZoom: [
          {
            type: "inside",
          },
        ],
        series: [
          {
            // For shadow
            type: "bar",
            itemStyle: {
              color: "rgba(0,0,0,0.05)",
            },
            barGap: "-100%",
            barCategoryGap: "40%",
            animation: false,
          },
          {
            type: "bar",
            data: data,
          },
        ],
      },
    };
  },
};
</script>