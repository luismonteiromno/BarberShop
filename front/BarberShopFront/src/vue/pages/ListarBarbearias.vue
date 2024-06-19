<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      items: [],
    };
  },
  async created() {
    try {
      const response = await api.get('/barbearias/');
      this.items = response.data;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
};
</script>
