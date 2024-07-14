import { createApp } from 'vue'
import App from './App.vue'
import router from './vue/routers/routers';

createApp(App)
  .use(router)
  .mount('#app');
