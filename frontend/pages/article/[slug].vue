<template>
  <div
    class="gap-y-4 flex flex-col md:px-[20%] pt-10 relative min-h-screen h-full"
  >
    <div class="text-xl">
      {{ articleData.title }}
    </div>
    <div class="flex gap-x-3 place-items-center">
      <UAvatar
        size="sm"
        src="https://avatars.githubusercontent.com/u/739984?v=4"
        alt="Avatar"
      />
      <div class="inline-flex flex-col text-xs">
        <div>
          <div>Laravel tuts</div>
          <div>7 min read · May 8, 2023</div>
        </div>
      </div>
    </div>
    <div>
      <img class="w-full rounded-sm" :src="articleData.cover_photo" alt="" />
    </div>
    <div
      class="text-sm prose prose:text-sm prose-img:w-full prose-img:rounded-md"
      v-html="articleData.content"
    ></div>
    <div class="pt-10">
      <div class="pb-3">Related</div>

      <div
        class="w-full pb-24 grid text-gray-800 gap-4 md:gap-5 grid-cols-1 sm:grid-cols-2 md:grid-cols-3"
      >
        <div
          class="rounded-sm overflow-hidden"
          v-for="(item, index) in articleData.related_by_author"
          :key="item"
        >
          <img
            class="w-full rounded-sm"
            :src="articleData.cover_photo"
            alt=""
          />
          <div class="pt-3 text-sm" v-text="articleData.title"></div>
        </div>

        <div
          class="rounded-sm overflow-hidden"
          v-for="(item, index) in articleData.related_by_category"
          :key="index"
        >
          <img
            class="w-full rounded-sm"
            :src="articleData.cover_photo"
            alt=""
          />
          <div class="pt-3 text-sm" v-text="articleData.title"></div>
        </div>
      </div>
    </div>
    <SharedFooter></SharedFooter>
  </div>
</template>
<script setup>
import axios from "axios";

definePageMeta({
  layout: "main-layout",
});

const route = useRoute();
const articleData = ref({});

const handleGetArticle = () => {
  axios.get("/blog/" + route.params.slug + "/").then((response) => {
    console.log(response.data);
    articleData.value = response.data;
  });
};

onMounted(() => {
  handleGetArticle();
});
</script>
