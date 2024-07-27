<template>
    <div class="container">
      <h1 class="title has-text-centered">Dados Financeiros</h1>
      <table class="table is-striped is-fullwidth">
        <thead>
          <tr>
            <th>Barbearia</th>
            <th>Receita Total</th>
            <th>Lucro Total</th>
            <th>Lucro Planos</th>
            <th>Renda Mensal</th>
            <th>Despesas</th>
            <th>Comparação de Lucros (Mês Anterior vs Atual)</th>
            <th>Comparação de Lucros (%)</th>
            <th>Prejuízo</th>
            <th>Lucro</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="financeiro in financeiros" :key="financeiro.id">
            <td>{{ financeiro.barbearia }}</td>
            <td>{{ financeiro.receita_total }}</td>
            <td>{{ financeiro.lucro_total }}</td>
            <td>{{ financeiro.lucro_planos }}</td>
            <td>{{ financeiro.renda_mensal }}</td>
            <td>{{ financeiro.despesas }}</td>
            <td>{{ financeiro.comparar_lucros_mes_anterior_e_atual }}</td>
            <td>{{ financeiro.comparar_lucros_mes_anterior_e_atual_porcentagem }}</td>
            <td>{{ financeiro.prejuizo }}</td>
            <td>{{ financeiro.lucro }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import api from '../../services/api/api';
  import 'bulma/css/bulma.css'

  
  export default {
    data() {
      return {
        financeiros: [],
      }
    },
    async created() {
      try {
        const response = await api.get('/financeiro/');
        this.financeiros = response.data.results;
      } catch (error) {
        this.error = error.message;
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    margin-top: 2rem;
  }
  
  .title {
    margin-bottom: 2rem;
  }
  </style>
  