<template>

    <div class="w-full ">
        <div class="register-container">
            <div class=" flex flex-col  gap-y-3 text-start">


                <div>
                    <div class=" text-start" for="">Title</div>

                    <textarea type="email" class="input-field" id="email" v-model="form.title"> </textarea>
                    <div v-if="formErrors.title"
                        class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start">
                        <div v-for="(error, index) in formErrors.title" :key="index">
                            {{ error }}
                        </div>
                    </div>
                </div>

                <div>
                    <div>Cover Image</div>
                    <div class="flex items-center justify-center w-full ">
                        <label for="dropzone-file"
                            class="flex flex-col items-center justify-center w-full h-64 border-2 overflow-hidden border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                            <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                <img v-if="form.imageUrl" :src="form.imageUrl"
                                    class="w-full h-full object-cover rounded-lg" alt="Uploaded Image">
                                <template v-else>
                                    <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                            stroke-width="2"
                                            d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                                    </svg>
                                    <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span
                                            class="font-semibold">Click to upload</span> or drag and drop</p>
                                    <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX.
                                        800x400px)</p>
                                </template>
                            </div>
                            <input id="dropzone-file" type="file" class="hidden" @change="handleFileChange"
                                accept="image/*" />
                        </label>
                    </div>
                    <div v-if="formErrors.image"
                        class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start">
                        <div v-for="(error, index) in formErrors.image" :key="index">
                            {{ error }}
                        </div>
                    </div>
                </div>

                <div>
                    <div class=" text-start" for="">Content</div>
                    
                    <QuillEditor theme="snow" v-model:content="form.content" />
                    <div v-if="formErrors.content"
                        class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start">
                        <div v-for="(error, index) in formErrors.content" :key="index">
                            {{ error }}
                        </div>
                    </div>
                </div>

                <div class=" pt-3">
                    <button class="register-button w-full" type="button" @click="submitForm()">
                        Create article
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import axios from 'axios';


definePageMeta({
    layout: 'account'
})


const formErrors = ref({
    content: '',
    title: '',
    image: ''
})

const toast = useToast();
const internetError = ref('')

const submitForm = () => {

    // Create a FormData object
    const formData = new FormData();
    formData.append('image', form.value.image);
    formData.append('content', form.value.content);
    formData.append('title', form.value.title);


    axios.post('/create_blog/', formData).then(response => () => {

    }).catch(err => {
        if (!err.response) {
            internetError.value = 'Network error'
            return
        }


        if (err.response.status == 400) {
            formErrors.value = err.response.data
            return
        }
    })
}

const form = ref({
    content: '',
    imageUrl: '',
    title: '',

    image: '',

})

const handleFileChange = (event) => {
    const file = event.target.files[0];

    form.value.image = file
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
        form.value.imageUrl = reader.result;
    };
    reader.readAsDataURL(file);
}

</script>



<style scoped>
.press-start-text {
    font-family: "Press Start 2P";
    background-color: #fde7be;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.register-container {
    /* max-width: 400px; */
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.form-group {
    margin-bottom: 1rem;
}

.input-field {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

.show-password-toggle {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.show-password-toggle label {
    margin-right: 0.5rem;
}

.login-link {
    margin-top: 1rem;
}

.register-button {
    background-color: #3490dc;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.25rem;
    cursor: pointer;
}

.register-link-text {
    color: #000;
}

.blue-text {
    color: #007bff;
}
</style>
