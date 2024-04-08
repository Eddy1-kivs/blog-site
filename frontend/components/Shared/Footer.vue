<template>
  <footer class="rounded-lg mt-10">
    <div class="p-4 flex flex-col items-center justify-center">
      <span class="text-sm sm:text-center mb-3">© {{ new Date().getFullYear() }}
        <a href="https://flowbite.com/" class="hover:underline">{{ useRuntimeConfig().public.appName }}™</a>. All Rights
        Reserved.
      </span>
      <ul class="flex flex-wrap items-center text-sm font-medium">
        <li>
          <a href="#" class="hover:underline me-4 md:me-6">About</a>
        </li>
        <li>
          <a href="#" class="hover:underline me-4 md:me-6">Privacy Policy</a>
        </li>
        <li>
          <a href="#" class="hover:underline me-4 md:me-6">Licensing</a>
        </li>
        <li>
          <a href="#" class="hover:underline">Contact</a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<style>
footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
