<template>
    <div class="container-input">
        <label>{{label}}:</label>
        <input class="input-field" v-model="value" v-bind:type="type" />
    </div>
</template>

<script>
import './styles.css'

export default {
    name: "InputData",
    props: ['type', 'label', 'value']
}
</script>