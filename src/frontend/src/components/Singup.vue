<template>
  <div class="flex mx-[5rem] my-[5rem] ">
    <div class="bg-[#ffedd7] py-[15rem] px-[8em] flex justify-center items-center w-1/2 rounded-tl-2xl rounded-bl-2xl">
        <Bananeira />
    </div>
    <div class="w-1/2 rounded-tr-2xl rounded-br-2xl shadow-2xl bg-white px-14 py-20">
        <div class="mr-32 ml-20">
            <h1 class="text-[48px] text-[#F28705] pb-10">Criar Conta</h1>
            <div class="pb-5">
                <h2 class="text-[25px] text-[#F28705] pb-3">Nome:</h2>
                <input type="text" id="nome_completo" class="bg-[#FFF4E7] border text-gray-900 text-sm rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full py-3.5 px-2.5" placeholder="Digite seu nome completo" required />
            </div>
            <div class="pb-5">
                <h2 class="text-[25px] text-[#F28705] pb-3">Username:</h2>
                <input type="text" id="nome_completo" class="bg-[#FFF4E7] border text-gray-900 text-sm rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full py-3.5 px-2.5 " placeholder="Crie seu username" required />
            </div>
            <div class="pb-5">
                <h2 class="text-[25px] text-[#F28705] pb-3">Senha:</h2>
                <input type="text" id="nome_completo" class="bg-[#FFF4E7] border t200pxext-gray-900 text-sm rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full py-3.5 px-2.5" placeholder="Digite uma senha de acesso" required />
            </div>
            <div class="my-custom-font flex flex-col justify-center items-center">
                <a href="url_do_seu_cadastro" class="pt-2 pb-7">
                    <h1 class="text-[25px] text-[#F28705]">Já tenho cadastro</h1>
                </a>
                <button class="hover:bg-blue-700 text-[#F28705] font-bold py-2 px-6 rounded-lg border border-[#F28705]">
                    Cadastrar
                </button>
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
