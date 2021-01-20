<template>
  <div class="home-page">
    <img src="./../../assets/macas-600.jpg" alt="Maçãs" />
    <div class="container-inputs">
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

export default {
  name: "Home",
  data () {
    return {
      tree_string: "",
      n_marcelo: 0,
      n_carla: 0,
    };
  },
  methods: {
    calcula: function() {
      console.log(this.tree_string, this.n_marcelo, this.n_carla);
    },
  },
};
</script>