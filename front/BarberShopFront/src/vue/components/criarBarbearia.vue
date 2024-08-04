<template>
    <div class="container">
      <h2 class="title has-text-centered">Adicionar Nova Barbearia</h2>
      <form @submit.prevent="createBarbearia">
        <div class="field">
          <label class="label" for="nome">Nome:</label>
          <div class="control">
            <input v-model="barbearia.nome_da_barbearia" class="input" type="text" id="nome" required />
          </div>
        </div>
        <div class="field">
          <label class="label" for="cnpj">CNPJ:</label>
          <div class="control">
            <input v-model="barbearia.cnpj" class="input" type="text" id="cnpj" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="abertura">Hora de Abertura:</label>
          <div class="control">
            <input v-model="barbearia.horario_de_abertura" class="input" type="time" id="abertura" required />
          </div>
        </div>
        <div class="field">
          <label class="label" for="fechamento">Hora de Fechamento:</label>
          <div class="control">
            <input v-model="barbearia.horario_de_fechamento" class="input" type="time" id="fechamento" required />
          </div>
        </div>
        <div class="field">
          <label class="label" for="tipo">Tipo:</label>
          <div class="control">
            <input v-model="barbearia.tipo_de_barbearia" class="input" type="text" id="tipo" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="rua">Rua:</label>
          <div class="control">
            <input v-model="barbearia.rua" class="input" type="text" id="rua" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="bairro">Bairro:</label>
          <div class="control">
            <input v-model="barbearia.bairro" class="input" type="text" id="bairro" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="complemento">Complemento:</label>
          <div class="control">
            <input v-model="barbearia.complemento" class="input" type="text" id="complemento" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="cidade">Cidade:</label>
          <div class="control">
            <input v-model="barbearia.cidade" class="input" type="text" id="cidade" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="estado">Estado:</label>
          <div class="control">
            <input v-model="barbearia.estado" class="input" type="text" id="estado" />
          </div>
        </div>
        <div class="field">
          <label class="label" for="cep">CEP:</label>
          <div class="control">
            <input v-model="barbearia.cep" class="input" type="text" id="cep" />
          </div>
        </div>
        <button type="submit" class="button is-primary">Criar Barbearia</button>
        <p v-if="errorMessage" class="has-text-danger">{{ errorMessage }}</p>
        <p v-if="successMessage" class="has-text-success">{{ successMessage }}</p>
      </form>
    </div>
  </template>
  
  
  <script>
import axios from 'axios';
import api from '@/services/api/api';

export default {
  data() {
    return {
      barbearia: {
        nome_da_barbearia: '',
        cnpj: '',
        horario_de_abertura: '',
        horario_de_fechamento: '',
        tipo_de_barbearia: '',
        rua: '',
        bairro: '',
        complemento: '',
        cidade: '',
        estado: '',
        cep: ''
      },
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async createBarbearia() {
      const token = localStorage.getItem('authToken'); // Supondo que você armazena o token no localStorage
      try {
        const response = await api.post('/barbearia/', this.barbearia, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        console.log('Barbearia criada com sucesso:', response.data);
        this.successMessage = 'Barbearia criada com sucesso!';
        this.errorMessage = '';
        this.$router.push('/'); // Redireciona para a lista de barbearias
      } catch (error) {
        console.error('Erro ao criar barbearia:', error);
        this.errorMessage = 'Erro ao criar barbearia. Verifique os dados e tente novamente.';
        this.successMessage = '';
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
  
  .field {
    margin-bottom: 1rem;
  }
  
  .button {
    margin-top: 1rem;
  }
  
  .has-text-success {
    color: #23d160; /* Cor verde para sucesso */
  }
  
  .has-text-danger {
    color: #ff3860; /* Cor vermelha para erro */
  }
  </style>
  