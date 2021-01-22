<template>
  <div>
    <h1 v-on:click="cons">Segunda página</h1>
    <h2>{{this.$store.state.nMarcelo}}</h2>
    <h2>{{this.$store.state.nCarla}}</h2>
    <h3 v-for="apples in this.$store.state.trees" :key="apples">
        {{apples}}
    </h3>
  </div>
</template>

<script>
export default {
  name: "resultado",
};
</script>