<template>
  <div class="press-start-text h-full flex flex-col gap-y-4">
    <img src="/image1.jpeg" class="w-full h-32 rounded-b-lg" alt="" />
    <div class="flex flex-col md:flex-row text-black font-extrabold text-2xl justify-between cursor-pointer">
      <nuxt-link to="/" class="nav-link" @click="selectTab('HOME')">HOME</nuxt-link>
      <nuxt-link to="/blog" class="nav-link" @click="selectTab('BLOG')">BLOG</nuxt-link>
      <nuxt-link to="/about" class="nav-link" @click="selectTab('ABOUT ME')">ABOUT ME</nuxt-link>
      <nuxt-link to="/ppos" class="nav-link" @click="selectTab('PPOS')">PPOS</nuxt-link>
      <nuxt-link to="/auth/login" class="nav-link" @click="selectTab('LOGIN')">LOGIN</nuxt-link>
    </div>

    <div class="flex flex-col md:flex-row text-black font-extrabold text-2xl justify-between cursor-pointer">

      <nuxt-link to="/auth/login" class="nav-link text-sm" v-for="item, index in categories" :key="index"
        @click="selectTab(item.name)"> {{ item.name }} </nuxt-link>


    </div>
    <img src="/image1.jpeg" class="w-full rounded-lg h-32" alt="" />
  </div>



</template>

<script setup>
import axios from 'axios';

const selectedTab = ref("HOME");
const categories = ref([]);

const setCategories = () => {
  axios.get('/all_categories/').then(response => {
    categories.value = response.data
  })
}

onMounted(() => {
  setCategories()
})

const selectTab = (tab) => {
  // this.selectedTab = tab;
}
</script>
