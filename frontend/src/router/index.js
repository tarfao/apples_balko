import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home'
import Resultado from '../views/Resultado'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/resultado',
    name: 'Resultado',
    component: Resultado
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
