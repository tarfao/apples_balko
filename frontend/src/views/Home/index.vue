<template>
  <div class="home-page">
    <img src="./../../assets/macas-600.jpg" alt="Maçãs" />
    <div class="container-inputs">
      <div class="container-input">
        <label>Vetor de árvores:</label>
        <input class="input-field" v-model="trees" type="text" />
        <p v-if="treesError" class="error-p">Exemplo de entrada: 3,2,5,4,3</p>
      </div>
      <div class="container-input">
        <label>Árvores de Marcelo:</label>
        <input class="input-field" v-model="nMarcelo" type="number" />
        <p v-if="nMarceloError" class="error-p">O número deve ser maior que 0.</p>
      </div>
      <div class="container-input">
        <label>Árvores de Carla:</label>
        <input class="input-field" v-model="nCarla" type="number" />
        <p v-if="nCarlaError" class="error-p">O número deve ser maior que 0.</p>
      </div>
      <div v-on:click="calcula" class="button-default">Calcular</div>
    </div>
  </div>
</template>

<script>
import "./styles.css";
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      trees: "",
      nMarcelo: 1,
      nCarla: 1,
    };
  },
  computed:{
    treesError() {
      return !/(\d(,\d)*)$/.test(this.trees) && this.trees !== ""
    },
    nMarceloError(){
      return !(this.nMarcelo > 0)
    },
    nCarlaError(){
      return !(this.nCarla > 0)
    },
  },
  methods: {
    async calcula() {
      //console.log(this.$apollo.queries.maxApples.start());
      try {
        if (
          /(\d(,\d)*)$/.test(this.trees) &&
          this.nMarcelo > 0 &&
          this.nCarla > 0
        ) {
          const { data } = await axios.post("http://localhost:5000/graphql", {
            query: `
            {
              maxApples(trees: "${this.trees}", nMarcelo: ${this.nMarcelo}, nCarla: ${this.nCarla})
            }
          `,
          });
          const array_trees = this.trees.split(",").map((n) => parseInt(n));
          const res = data.maxApples.split(",").map((n) => parseInt(n));
          this.$router.push("resultado");
          this.$store.commit("changeValues", {
            trees: array_trees,
            nMarcelo: this.nMarcelo,
            nCarla: this.nCarla,
            res,
          });
        } else {
          alert("Erro nos dados de entrada");
        }
      } catch (error) {
        throw new Error(error);
      }
    },
  },
};
</script>