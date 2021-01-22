import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex'
import 'es6-promise/auto' //vuex require promise
import './styles.css'

const store = createStore({
    state () {
        return {
            trees: [],
            nMarcelo: 0,
            nCarla: 0
        }
    },
    mutations: {
        changeValues(state, data){
            const { trees, nMarcelo, nCarla } = data;
            console.log(trees, nMarcelo, nCarla)
            state.trees = trees;
            state.nMarcelo = nMarcelo;
            state.nCarla = nCarla;
        }
    }
})

createApp(App)
    .use(router)
    .use(store)
    .mount('#app')
