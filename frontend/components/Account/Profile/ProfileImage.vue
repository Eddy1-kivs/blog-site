<template>
  <div class="flex items-start justify-start">
    <div class="relative">
      <img
        v-if="profileImageUrl"
        :src="profileImageUrl"
        alt="Profile"
        class="w-32 h-32 rounded-full"
      />
      <div
        v-else
        class="w-32 h-32 rounded-full bg-gray-200 flex items-center justify-center"
      >
        <svg
          class="w-10 h-10 text-gray-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          ></path>
        </svg>
      </div>
      <input
        type="file"
        accept="image/*"
        class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
        @change="handleImageUpload"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      profileImageUrl: null,
    };
  },
  methods: {
    handleImageUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (e) => {
        this.profileImageUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },
  },
};
</script>
