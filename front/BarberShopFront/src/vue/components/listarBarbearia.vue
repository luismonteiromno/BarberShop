<template>
  <div class="container">
    <h2 class="title has-text-centered">Lista de Barbearias</h2>
    <router-link to="/criar-barbearia" class="button is-primary">Adicionar Nova Barbearia</router-link>
    <div v-if="barbearias.length > 0" class="list">
      <div v-for="barbearia in barbearias" :key="barbearia.id" class="box">
        <div class="content">
          <p><strong>Barbearia:</strong> {{ barbearia.nome_da_barbearia }}</p>
          <p><strong>Média das Avaliações:</strong> {{ barbearia.media_das_avaliacoes }}</p>
          <router-link :to="{ path: '/agendamentos', query: { id: barbearia.id } }" class="button is-link is-small">Ver agendamentos</router-link>
          <router-link :to="{ path: '/financeiro', query: { id: barbearia.id } }" class="button is-link is-small">Ver financeiro</router-link>
        </div>
      </div>
    </div>
    <p v-else class="has-text-centered">Nenhuma barbearia encontrada.</p>
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
      const response = await api.get('/barbearia/');
      console.log('Dados recebidos:', response.data);
      this.barbearias = response.data.results;
    } catch (error) {
      console.error('Erro ao buscar barbearias:', error);
    }
  }
};
</script>

<style scoped>
.container {
  margin-top: 2rem;
}

.title {
  margin-bottom: 2rem;
}

.box {
  margin-bottom: 1rem;
}

.button {
  margin-right: 0.5rem;
}
</style>
