import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../views/HomeView.vue')
  },
  {
    path: '/',
    name: 'json',
    component: () => import(/* webpackChunkName: "about" */ '../views/JsonDataView.vue')
  },
  {
    path: '/',
    name: 'json_analyse',
    component: () => import(/* webpackChunkName: "about" */ '../views/JsonAnalyseView.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
