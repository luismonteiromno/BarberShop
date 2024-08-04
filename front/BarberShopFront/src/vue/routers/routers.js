import { createRouter, createWebHistory } from 'vue-router';
import agendamento from '../components/agendamento.vue';
import financeiro from '../components/financeiro.vue';
import listarBarbearia from '../components/listarBarbearia.vue';
import criarBarbearia from '../components/criarBarbearia.vue';

const routes = [
  { path: '/', component: listarBarbearia },
  { path: '/agendamentos', component: agendamento },
  { path: '/criar-barbearia', component: criarBarbearia},
  { path: '/financeiro', component: financeiro}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
