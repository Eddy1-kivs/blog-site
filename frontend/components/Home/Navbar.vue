<!-- components/Navbar.vue -->

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
    <img src="/image1.jpeg" class="w-full rounded-lg h-32" alt="" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedTab: "HOME",
    };
  },


  methods: {
    selectTab(tab) {
      this.selectedTab = tab;
    },
  },
};
</script>
