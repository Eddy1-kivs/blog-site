<template>
    <div class=" flex flex-col gap-y-2">

        <div class=" py-3">
            <div>
                <div>Comments</div>
                <UTextarea variant="outline" placeholder="Search..." v-model="form.text" />
                <div v-if="formErrors.text" class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start">
                    <div v-for="(error, index) in formErrors.text" :key="index">
                        {{ error }}
                    </div>
                </div>
            </div>
            <div class=" pt-3 flex justify-end">
                <button class="register-button " type="button" @click="submitForm()">
                    Submit
                </button>
            </div>hh
        </div>

        <div v-for="item, index in comments" :key="index" class=" text-xs">

            <div class=" flex  items-center text-xs gap-x-2">
                <UAvatar size="sm" :src="item.user_profile_image" alt="Avatar" />
                <div>

                    <div>
                        {{ item['user_username'] }}
                    </div>

                    <div>
                        {{ item['pub_date'] }}
                    </div>
                </div>
            </div>
            <div class=" pt-2">
                {{ item['text'] }}
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';

defineProps(['comments'])
const route = useRoute();
const formErrors = ref({})
const form = ref({
    text: ''
})

const submitForm = () => {
    axios.post(`/blog/${route.params.slug}/add_comment/`, form.value).then(response => {

    }).catch(err => {
        if (err.response && err.response.status == 400) {
            formErrors.value = err.response.data
        }
    })
}
</script>

<style scoped>
.register-button {
    background-color: #3490dc;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.25rem;
    cursor: pointer;
}
</style>