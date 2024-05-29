<template>
<div class="main">
  <div class="flex xl:mx-[5rem] mx-0 xl:my-[5rem] my-0">
    <div class="hidden xl:flex xl:w-1/2 bg-[#ffedd7] xl:py-[15rem] py-0 xl:px-[8em] px-0 justify-center items-center rounded-tl-2xl rounded-bl-2xl">
      <Bananeira />
    </div>
    <div class="w-full xl:w-1/2 rounded-tr-2xl rounded-br-2xl shadow-2xl bg-white xl:px-14 px-0 xl:py-20 py-0">
      <div class=" mr-5 xl:ml-20 ml-5">
        <h1 class="text-[2.4rem] text-[#F28705] pb-10 text-center xl:text-start">Criar Conta</h1>
        <div class="pb-5">
          <h2 class="text-[1.25rem] text-[#F28705] pb-3">Nome:</h2>
          <input type="text" id="nome_completo" class="bg-[#FFF4E7] border w-[25%] text-gray-900 text-sm rounded-xl block w-full py-3.5 px-2.5 focus:border-[#F28705] focus:outline-none" placeholder="Digite seu nome completo" required />
        </div>
        <div class="pb-5">
          <h2 class="text-[1.25rem] text-[#F28705] pb-3">Username:</h2>
          <input type="text" id="username" class="bg-[#FFF4E7] border text-gray-900 text-sm rounded-xl block w-full py-3.5 px-2.5 focus:border-[#F28705] focus:outline-none" placeholder="Crie seu username" required />
        </div>
        <div class="pb-5">
          <h2 class="text-[1.25rem] text-[#F28705] pb-3">Senha:</h2>
          <input type="password" id="senha" class="bg-[#FFF4E7] border text-gray-900 text-sm rounded-xl block w-full py-3.5 px-2.5 focus:border-[#F28705] focus:outline-none" placeholder="Digite uma senha de acesso" required />
        </div>
        <div class="flex flex-col justify-center items-center">
          <a href="url_do_seu_cadastro" class="pt-2 pb-7">
            <h1 class="text-[1.25rem] text-[#F28705]">Já tenho cadastro</h1>
          </a>
          <button class="hover:bg-[#F28705] text-[1.18rem] hover:text-white text-[#F28705] font-bold py-2 px-6 rounded-lg border border-[#F28705] mb-10">
            Cadastrar
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
    import Bananeira from '../assets/bananeira.svg'
</script>

<script>
export default {
  name: 'Signup'
}
</script>

<style scoped>

.main {
  font-family: 'Poppins';
}

</style>

