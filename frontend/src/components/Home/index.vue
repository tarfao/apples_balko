<template>
  <div class="home-page">
    <img src="./../../assets/macas-600.jpg" alt="Maçãs" />
    <div class="container-inputs">
      <p>{{ maxApples }}</p>
      <div class="container-input">
        <label>Vetor de árvores:</label>
        <input class="input-field" v-model="tree_string" type="text" />
      </div>
      <div class="container-input">
        <label>Árvores de Marcelo:</label>
        <input class="input-field" v-model="n_marcelo" type="number" />
      </div>
      <div class="container-input">
        <label>Árvores de Carla:</label>
        <input class="input-field" v-model="n_carla" type="number" />
      </div>
      <div v-on:click="calcula" class="button-default">Calcular</div>
    </div>
  </div>
</template>

<script>
import "./styles.css";
import gql from "graphql-tag";

export default {
  name: "Home",
  data() {
    return {
      tree_string: "",
      n_marcelo: 0,
      n_carla: 0,
    };
  },
  apollo: {
    maxApples: {
      query: gql`
        query maxApples($trees: String!, $nMarcelo: Number!, $nCarla: Number!) {
          maxApples(trees: $trees)
        }
      `,
      variables() {
        return {
          trees: this.tree_string,
          nMarcelo: this.n_marcelo,
          nCarla: this.n_carla,
        };
      },
      skip() {
        return true;
      },
      result({ data }) {
        console.log(`Resultado retornado`);
        alert(data);
      },
      error(err) {
        console.error("Ocorreu algum erro!", err);
      },
    },
  },
  methods: {
    calcula: async function () {
      //console.log(this.$apollo.queries.maxApples.start());
      await this.$apollo.query({
        query: gql`
          query{
            maxApples(trees: "${this.tree_string}", nMarcelo: ${this.n_marcelo}, nCarla: ${this.n_carla})
          }
        `,
      }).then(data => {
        console.log(data);
      }).catch(e => {
        console.log("Ocorreu algum erro!",e);
      });
    },
  },
};
</script>