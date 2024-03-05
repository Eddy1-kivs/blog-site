<template>
  <div
    class="px-2 bg-[#fde7be] py-2 min-h-screen pt-4 press-start-text text-gray-900 md:px-20 flex flex-col md:flex-row gap-4"
  >
    <div class="md:pt-20">
      <div class="px-4 bg-amber-300 py-4 flex flex-col gap-y-2 rounded-md">
        <!-- <NuxtLink ></NuxtLink> -->
        <div>Dashboard</div>
        <div>Profile</div>
      </div>
    </div>
    <div>
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
