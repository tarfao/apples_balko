<template>
  <div class="container-resultado">
    <h1>Resultado</h1>
    <router-link class="button-default no-style-link" to="/">Voltar</router-link>
    <div class="container-graficos">
      <v-chart class="grafico-style" :options="appleTrees" />
      <v-chart class="grafico-style" :options="applesM" />
      <v-chart class="grafico-style" :options="applesC" />
      <h1 class="total-colhido">Total de <br>Maçãs colhidas:<br>{{totalColhido}}</h1>
    </div>
  </div>
</template>

<script>
import ECharts from "vue-echarts";
import "echarts/lib/chart/bar";
import "echarts/lib/component/title";
import { RouterLink } from "vue-router";
import { bars } from "./graficos";
import "./styles.css";

export default {
  name: "resultado",

  components: {
    "v-chart": ECharts,
    RouterLink,
  },
  
  data() {
    const { trees, res, nMarcelo, nCarla } = this.$store.state;

    var dataAxis = [];
    var dataY = trees;
    //garantindo que os dados enviados sejam de fato inteiros para fins de cálculos.
    const nMarceloInt = parseInt(nMarcelo)
    const nCarlaInt = parseInt(nCarla)

    /**Atribuindo os valores A1, A2, ... An para os dados de X,
     * indicando arvore 1, avore2...*/
    for (let i = 0; i < dataY.length; i++) {
      dataAxis.push(`A${i + 1}`);
    }
    /**calcula os valores de X, de Y e a soma total de maçãs para Marcelo(M) */
    const dataAxisM = dataAxis.slice(res[1], res[1] + nMarceloInt);
    const dataYM = dataY.slice(res[1], res[1] + nMarceloInt);
    const totalM = dataYM.reduce((acc, curr) => acc + curr);
    /**calcula os valores de X, de Y e a soma total de maçãs para Carla(C) */
    const dataAxisC = dataAxis.slice(res[2], res[2] + nCarlaInt);
    const dataYC = dataY.slice(res[2], res[2] + nCarlaInt);
    const totalC = dataYC.reduce((acc, curr) => acc + curr);

    return {
      appleTrees: bars(
        dataAxis,
        dataY,
        "Pés de maçã",
        "Número de maçãs em cada pé"
      ),
      applesM: bars(dataAxisM, dataYM, "Pés de maçã de Marcelo", `Soma total: ${totalM}`, "#FF0000"),
      applesC: bars(dataAxisC, dataYC, "Pés de maçã de Carla", `Soma total: ${totalC}`, "#FFA500"),
      totalColhido: totalM+totalC
    };
  },
};
</script>