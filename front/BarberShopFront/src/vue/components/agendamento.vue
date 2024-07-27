<template>
  <div class="container">
    <h2 class="title has-text-centered">Agendamentos</h2>
    <div v-if="agendamentos.length > 0" class="list">
      <div v-for="agendamento in agendamentos" :key="agendamento.id" class="box">
        <div class="content">
          <p><strong>Agendamento:</strong> {{ agendamento.numero_do_agendamento }}</p>
          <p><strong>Preço do Serviço:</strong> {{ agendamento.preco_do_servico }}</p>
          <div v-if="agendamento.agendamento_cancelado" class="notification is-danger">
            Agendamento cancelado
          </div>
          <div v-else>
            <button @click="cancelarAgendamento(agendamento.id)" class="button is-danger is-small">Cancelar Agendamento</button>
          </div>
        </div>
      </div>
    </div>
    <p v-else class="has-text-centered">Nenhum agendamento.</p>
  </div>
</template>

<script>
import api from '@/services/api/api';

export default {
  data() {
    return {
      agendamentos: []
    };
  },
  async created() {
    try {
      const response = await api.get('/agendamento/');
      console.log('Dados recebidos:', response);
      this.agendamentos = response.data.results;
    } catch (error) {
      console.error('Erro ao buscar agendamentos:', error);
    }
  },
  methods: {
    async cancelarAgendamento(id) {
      try {
        await api.post(`agendamentos/${id}/cancelar/`);
        this.agendamentos = this.agendamentos.map(agendamento =>
          agendamento.id === id ? { ...agendamento, agendamento_cancelado: true } : agendamento
        );
      } catch (error) {
        console.error('Erro ao cancelar agendamento:', error);
      }
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
</style>
