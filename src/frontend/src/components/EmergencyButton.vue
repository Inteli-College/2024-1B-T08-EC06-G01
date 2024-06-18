<template>
  <div>
    <button class="bg-red-500 text-white py-2 px-8 rounded hover:bg-red-700" @click="emergencyStop">
      Modo de Emergência
    </button>
  </div>
</template>

<script>
export default {
  name: 'EmergencyButton',
  data() {
    const websocket = new WebSocket(import.meta.env.VITE_CONTROL_WEBSOCKET);

    console.log(import.meta.env.VITE_CONTROL_WEBSOCKET);

    websocket.onopen = () => {
      console.log('Connected to the control websocket');
    };

    websocket.onclose = () => {
      console.log('Disconnected from the control websocket');
    };

    websocket.onerror = (error) => {
      console.error('Error:', error);
    };

    return {
      websocket: websocket,
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

      if (this.$notify) {
        console.log('notificação enviada');
        return this.$notify({
          title: 'Emergência',
          text: 'A parada de emergência foi acionada, para continuar movimentando o robô, reinicie o serviço responsável pelo controle do robô',
          type: 'error'
        });
        
      } else {
        console.error('Notification plugin is not available');
      }
    },
  },
};
</script>
