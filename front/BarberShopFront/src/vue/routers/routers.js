import { createRouter, createWebHistory } from 'vue-router';
import ListarBarbearias from '../components/ListarBarbearias.vue';
import Agendamentos from '../components/Agendamentos.vue';

const routes = [
  { path: '/', component: ListarBarbearias },
  { path: '/agendamentos', component: Agendamentos }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
