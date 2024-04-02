<template>
  <div class="px-2 bg-[#fde7be] py-2 min-h-screen relative text-gray-900 md:px-20">
    <HomeNavbar></HomeNavbar>
    <div class="w-full grid pt-10 gap-4 md:gap-5 grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
      <div class="rounded-sm overflow-hidden" v-for="(item, index) in articles" :key="index">
        <NuxtLink :to="'/article/' + item.id">
          <img class="w-full rounded-sm" :src="item.cover_photo" alt="" />
          <div class="pt-3">
            {{ item.title }}
          </div>
        </NuxtLink>
        <!-- {{ articles }} -->
      </div>
    </div>
    <SharedFooter></SharedFooter>
  </div>
</template>
<script setup>
import axios from "axios";

definePageMeta({
  layout: "font-layout",
});

const articlesData = ref({});
const articles = ref([]);

const previousUrl = ref(null);

const handleFetch = () => {
  let url = articlesData.value.next ?? "all_blogs/";
  if (url != previousUrl.value) {
    previousUrl.value = url;

    axios
      .get(url)
      .then((response) => {
        articles.value.push(...response.data.results);
        articlesData.value = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};

const handleGetCategories = () => {
  axios.get('categories')
}

const handleScroll = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
    handleFetch();
  }
};

onMounted(() => {
  handleFetch();
  window.addEventListener("scroll", function () {
    handleScroll();
  });
});
</script>
