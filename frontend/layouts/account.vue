<template>
  <div
    class="px-2 bg-[#fde7be] py-2 min-h-screen pt-4 press-start-text text-gray-900 md:px-20 flex flex-col md:flex-row gap-4 w-full">
    <div class="md:pt-20">
      <div class="px-4 bg-amber-300 py-4 flex flex-col gap-y-2 rounded-md">
        <nuxt-link to="/account">Dashboard</nuxt-link>

        <nuxt-link to="/account/profile">Profile</nuxt-link>

        <nuxt-link to="/article/create">Create </nuxt-link>
      </div>
    </div>
    <div class=" w-full md:pt-20">
      <slot></slot>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

.press-start-text {
  font-family: "Press Start 2P";
}
</style>
