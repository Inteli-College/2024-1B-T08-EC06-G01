<template>
    <button class="bg-red-500 text-white py-2 px-8 rounded hover:bg-red-700" @click="emergencyStop">
    Modo de Emergência
    </button>
</template/

<script>
    const websocket = new WebSocket(import.meta.env.VITE_CONTROL_WEBSOCKET);

    console.log(import.meta.env.VITE_CONTROL_WEBSOCKET)

    websocket.onopen = () => {
    console.log('Connected to the control websocket');
    };

    websocket.onclose = () => {
    console.log('Disconnected from the control websocket');
    };

    websocket.onerror = (error) => {
    console.error('Error:', error);
    };

    export default {
        name: 'EmergencyButton',


        // Em métodos vocÊ define as funções que serão chamadas no template
        methods: {
            emergencyStop() {
            console.log('Emergency Stop')
            this.websocket.send(JSON.stringify({
            type: "CPacketControl",
            data: {
                state: "emergency"
            }
            }))

            return this.$notify({
                title: 'Emergência',
                text:'A parada de emergência foi acionada, para continuar movimentando o robô, reinicie o serviço responsável pelo controle do robô',
                type: 'error'
            });
        },
        } 
    }
</script>
