<template>
  <div class="home-page">
    <img src="./../../assets/macas-600.jpg" alt="Maçãs" />
    <div class="container-inputs">
      <div class="container-input">
        <label>Vetor de árvores:</label>
        <input class="input-field" v-model="trees" type="text" />
      </div>
      <div class="container-input">
        <label>Árvores de Marcelo:</label>
        <input class="input-field" v-model="nMarcelo" type="number" />
      </div>
      <div class="container-input">
        <label>Árvores de Carla:</label>
        <input class="input-field" v-model="nCarla" type="number" />
      </div>
      <div v-on:click="calcula" class="button-default">Calcular</div>
    </div>
  </div>
</template>

<script>
import "./styles.css";
import axios from 'axios';

export default {
  name: "Home",
  data() {
    return {
      trees: "",
      nMarcelo: 0,
      nCarla: 0,
    };
  },
  methods: {
    async calcula() {
      //console.log(this.$apollo.queries.maxApples.start());
      try {
        const {data} = await axios.post('http://localhost:5000/graphql',{
          query: `
            {
              maxApples(trees: "${this.trees}", nMarcelo: ${this.nMarcelo}, nCarla: ${this.nCarla})
            }
          `
        })
        console.log(data.maxApples);
      } catch (error) {
        throw new Error(error);
      }
    },
  },
};
</script>