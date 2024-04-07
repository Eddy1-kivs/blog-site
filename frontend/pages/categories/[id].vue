<template>
    <div class="px-2 bg-[#fde7be] py-2 min-h-screen relative text-gray-900 md:px-20">
        <div class="pt-4">
            {{ categories.length > 0 ? categories.filter((item) => item.id == route.params.id)[0].name : '' }}
        </div>
        <div class="w-full grid pt-10 gap-4 md:gap-5 grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
            <div class="rounded-sm overflow-hidden" v-for="(item, index) in articles" :key="index">
                <NuxtLink :to="'/article/' + item.id">
                    <img class="w-full rounded-sm" :src="item.cover_photo" alt="" />
                    <div class="pt-3">
                        {{ item.title }}
                    </div>
                </NuxtLink>
            </div>
        </div>

        <div v-if="articles.length == 0" class="  flex justify-center w-full">
            <div>

                <img src="/images/empty2.png" alt="">
                <div class=" text-gray-500 pt-8 ">
                    Sorry there is nothing here
                </div>


            </div>
        </div>

        <SharedFooter></SharedFooter>


    </div>
</template>
<script setup>
import axios from "axios";
import { useCategories } from '~/composables/states';

definePageMeta({
    layout: "font-layout",
});

const route = useRoute()

const categories = useCategories()

const articlesData = ref({});
const articles = ref([]);

const previousUrl = ref(null);

const handleFetch = () => {
    let url = articlesData.value.next ?? "category/" + route.params.id;
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