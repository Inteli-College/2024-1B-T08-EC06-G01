<template>
  <div>
    <button class="bg-red-500 text-white py-2 px-8 rounded hover:bg-red-700" @click="emergencyStop">
      Modo de Emergência
    </button>
  </div>
</template>

<script>
import { useNotification } from '@kyvg/vue3-notification';

export default {
  name: 'EmergencyButton',
  data() {
    return {
      websocket: null,
    };
  },
  created() {
    this.websocket = new WebSocket(import.meta.env.VITE_CONTROL_WEBSOCKET);

    this.websocket.onopen = () => {
      console.log('Connected to the control websocket');
    };

    this.websocket.onclose = () => {
      console.log('Disconnected from the control websocket');
    };

    this.websocket.onerror = (error) => {
      console.error('Error:', error);
    };
  },
  methods: {
    emergencyStop() {
      console.log('Emergency Stop');
      this.websocket.send(JSON.stringify({
        type: "CPacketControl",
        data: {
          state: "emergency"
        }
      }));

      try {
        const { notify } = useNotification();
        console.log('Trying to send notification');
        if (notify) {
          console.log('notificação enviada');
          notify({
            title: 'Emergência',
            text: 'A parada de emergência foi acionada, para continuar movimentando o robô, reinicie o serviço responsável pelo controle do robô',
            type: 'error'
          });
        } else {
          console.error('Notification plugin is not available');
        }
      } catch (error) {
        console.error('Error while sending notification:', error);
      }
    },
  },
};
</script>
