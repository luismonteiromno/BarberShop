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
            <td class="has-text-success">{{ financeiro.lucro_total }}</td>
            <td class="has-text-success">{{ financeiro.lucro_planos }}</td>
            <td>{{ financeiro.renda_mensal }}</td>
            <td class="has-text-danger">{{ financeiro.despesas }}</td>
            <td class="has-text-info">{{ financeiro.comparar_lucros_mes_anterior_e_atual }}</td>
            <td class="has-text-info">{{ financeiro.comparar_lucros_mes_anterior_e_atual_porcentagem }}</td>
            <td>
              <span v-if="financeiro.prejuizo == true" class="icon has-text-sucess">
                <i class="fas fa-check"></i>
              </span>
              <span v-else class="icon has-text-danger">
                <i class="fas fa-times"></i>
              </span>
            </td>
            <td>
              <span v-if="financeiro.lucro == true" class="icon has-text-success">
                <i class="fas fa-check"></i>
              </span>
              <span v-else class="icon has-text-danger">
                <i class="fas fa-times"></i>
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import api from '../../services/api/api';
  import 'bulma/css/bulma.css';
  import '@fortawesome/fontawesome-free/css/all.css';
  
  export default {
    data() {
      return {
        financeiros: [],
      };
    },
    async created() {
      try {
        const response = await api.get('/financeiro/');
        this.financeiros = response.data.results;
      } catch (error) {
        this.error = error.message;
      }
    },
  };
  </script>
  
  <style scoped>
  .container {
    margin-top: 2rem;
  }
  
  .title {
    margin-bottom: 2rem;
  }
  
  /* Custom colors for different types of data */
  .has-text-success {
    color: #23d160; /* Green for profits */
  }
  
  .has-text-danger {
    color: #ff3860; /* Red for expenses and losses */
  }
  
  .has-text-info {
    color: #209cee; /* Blue for comparisons */
  }
  
  .icon {
    font-size: 1.2rem;
  }
  </style>
  