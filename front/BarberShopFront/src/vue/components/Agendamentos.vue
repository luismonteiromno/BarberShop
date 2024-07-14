<template>
    <div>
        <h2>Agendamentos</h2>
        <ul v-if="agendamentos.length > 0">
            <li v-for="agendamento in agendamentos" :key="agendamento.id">
                    {{ agendamento.numero_do_agendamento }} - {{ agendamento.preco_do_servico }}
                    <div v-if="agendamento.agendamento_cancelado === true">
                        Agendamento cancelado
                    </div>
                    <div v-else="agendamento.agendamento_cancelado === false">
                        <button @click="cancelarAgendamento(agendamento.id)">Cancelar Agendamento</button>
                    </div>
                    <br>
            </li>
        </ul>
        <p v-else>Nenhum agendamento.</p>
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
      const response = await api.get('agendamentos/');
      console.log('Dados recebidos:', response);
      this.agendamentos = response.data.results;
    } catch (error) {
      console.error('Erro ao buscar agendamentos:', error);
    }
  }
};
</script>
