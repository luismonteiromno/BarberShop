import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // A URL base da sua API Django
});

export default api;
