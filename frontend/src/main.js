import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex'
import 'es6-promise/auto' //vuex require promise
import Echarts from 'vue-echarts'

import './styles.css'

const store = createStore({
    state () {
        return {
            trees: [],
            nMarcelo: 0,
            nCarla: 0,
            res: []
        }
    },
    mutations: {
        changeValues(state, data){
            const { trees, nMarcelo, nCarla, res } = data;
            state.trees = trees;
            state.nMarcelo = nMarcelo;
            state.nCarla = nCarla;
            state.res = res;
        }
    }
})

createApp(App)
    .component('v-chart', Echarts)
    .use(router)
    .use(store)
    .mount('#app')
