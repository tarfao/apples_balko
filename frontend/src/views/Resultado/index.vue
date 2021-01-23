<template>
  <div>
    <h1>Resultado</h1>
    <router-link to="/">Voltar</router-link>
    <div>
      <v-chart :options="appleTrees" />
      <v-chart :options="applesM" />
      <v-chart :options="applesC" />
    </div>
  </div>
</template>

<script>
import ECharts from "vue-echarts";
import "echarts/lib/chart/bar";
import "echarts/lib/component/title";
import { RouterLink } from "vue-router";
import { bars } from "./graficos";

export default {
  name: "resultado",
  components: {
    "v-chart": ECharts,
    RouterLink,
  },
  data() {
    const { trees, res, nMarcelo, nCarla } = this.$store.state;
    console.log(res[0], res[1], res[2], nMarcelo, nCarla);
    var dataAxis = [];
    var dataY = trees;
    for (let i = 0; i < dataY.length; i++) {
      dataAxis.push(`A${i + 1}`);
    }
    const dataAxisM = dataAxis.slice(res[1], res[1] + nMarcelo);
    const dataYM = dataY.slice(res[1], res[1] + nMarcelo);
    const dataAxisC = dataAxis.slice(res[2], res[2] + nCarla);
    const dataYC = dataY.slice(res[2], res[2] + nCarla);
    console.log(dataAxisM, dataAxisC);
    return {
      appleTrees: bars(
        dataAxis,
        dataY,
        "Pés de maçã",
        "Número de maçãs em cada pé"
      ),
      applesM: bars(dataAxisM, dataYM, "Pés de maçã de Marcelo", "", "#FF0000"),
      applesC: bars(dataAxisC, dataYC, "Pés de maçã de Carla", "", "#FFA500"),
    };
  },
};
</script>