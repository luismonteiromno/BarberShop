<template>
  <div>
    <h2>Lista de Barbearias</h2>
    <ul v-if="barbearias.length > 0">
      <li v-for="barbearia in barbearias" :key="barbearia.id">
        {{ barbearia.nome_da_barbearia }}
      </li>
    </ul>
    <p v-else>Nenhuma barbearia encontrada.</p>
  </div>
</template>

<script>
import api from '@/services/api/api';

export default {
  data() {
    return {
      barbearias: []
    };
  },
  async created() {
    try {
      const response = await api.get('barbearias/');
      console.log('Dados recebidos:', response.data); // Verifique os dados recebidos
      this.barbearias = response.data.results;
    } catch (error) {
      console.error('Erro ao buscar barbearias:', error);
    }
  }
};
</script>
