import './style.css'

import App from './App.vue'
import Notifications from '@kyvg/vue3-notification'
import { createApp } from 'vue'
import router from './router'

createApp(App).use(router).use(Notifications).mount('#app');



