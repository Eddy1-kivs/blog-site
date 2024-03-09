<template>
  <footer class="rounded-lg absolute bottom-0">
    <div class="mx-auto p-4  ">
      <span class="text-sm sm:text-center">© {{ new Date().getFullYear() }}
        <a href="https://flowbite.com/" class="hover:underline">{{ useRuntimeConfig().public.appName }}™</a>. All Rights
        Reserved.
      </span>
      <ul class="flex flex-wrap items-center mt-3 text-sm font-medium sm:mt-0">
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
