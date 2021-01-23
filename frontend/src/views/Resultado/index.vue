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
    /**calcula os valores de X, de Y e a soma total de maçãs para Marcelo(M) 
     * antes eu havia utilizado o slice, porém em determinados momentos ele demorava para executar, 
     * e o reduce utilizado para totalizar a quantidade de maçãs, não conseguia dar seguimento, pois o DataYM
     * não foi preenchido ainda. Dessa forma, utilizando o for, com a inicialização do dataYM como um array,
     * o reduce passou a funcionar sem erros.
    */
    const dataAxisM =[];
    const dataYM=[];
    for(let i = res[1]; i < res[1] + nMarceloInt; i++){
      dataAxisM.push(dataAxis[i]);
      dataYM.push(dataY[i])
    }
    const totalM = dataYM.reduce((acc, curr) => acc + curr);
    /**calcula os valores de X, de Y e a soma total de maçãs para Carla(C) */
    const dataAxisC =[];
    const dataYC=[];
    for(let i = res[2]; i < res[2] + nCarlaInt; i++){
      dataAxisC.push(dataAxis[i]);
      dataYC.push(dataY[i])
    }
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