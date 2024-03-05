<template>
  <div class="pt-10 flex w-full flex-col place-items-center">
    <div class="pb-10">
      <AccountProfileImage></AccountProfileImage>
    </div>

    <div class="w-full">
      <div class="register-container">
        <!-- <h2 class="pb-10"></h2> -->
        <form>
          <div class="text-xs text-red-600 text-center">{{ offlineText }}</div>
          <!-- {{ form }} -->
          <div class="form-group">
            <div for="username" class="w-full text-start">About:</div>

            <textarea
              class="input-field"
              id="about"
              v-model="form.about"
            ></textarea>

            <div
              v-if="errors.about"
              class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
            >
              <div v-for="(error, index) in errors.about" :key="index">
                {{ error }}
              </div>
            </div>
          </div>

          <div class="form-group">
            <div for="username" class="w-full text-start">Bio:</div>

            <textarea
              class="input-field"
              id="bio"
              v-model="form['bio']"
            ></textarea>

            <div
              v-if="errors.bio"
              class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
            >
              <div v-for="(error, index) in errors.bio" :key="index">
                {{ error }}
              </div>
            </div>
          </div>

          <div class="form-group">
            <div for="username" class="w-full text-start">Username:</div>
            <input
              type="text"
              class="input-field"
              id="username"
              v-model="form.first_name"
            />
            <div
              v-if="errors.first_name"
              class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
            >
              <div v-for="(error, index) in errors.first_name" :key="index">
                {{ error }}
              </div>
            </div>
          </div>

          <div class="form-group">
            <div for="username" class="w-full text-start">Last name:</div>
            <input
              type="text"
              class="input-field"
              id="username"
              v-model="form.first_name"
            />
            <div
              v-if="errors.first_name"
              class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
            >
              <div v-for="(error, index) in errors.first_name" :key="index">
                {{ error }}
              </div>
            </div>
          </div>

          <div class="form-group">
            <div for="username" class="w-full text-start">Username:</div>
            <input
              type="text"
              class="input-field"
              id="username"
              v-model="form.email"
            />
            <div
              v-if="errors.email"
              class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
            >
              <div v-for="(error, index) in errors.email" :key="index">
                {{ error }}
              </div>
            </div>
          </div>

          <button class="register-button" type="button" @click="submitForm()">
            Update Profile
          </button>
        </form>

        <!-- <div class="login-link">
          <router-link to="/auth/login" class="login-link-text">
            Already have an account? <span class="blue-text">Login here.</span>
          </router-link>
        </div> -->
      </div>
    </div>
  </div>
</template>
<script setup>
import axios from "axios";

definePageMeta({
  layout: "account",
});
const user = useUser();
const form = ref({
  username: "",
  first_name: "",
  last_name: "",
  email: "",
  bio: "",
  about: "",
});
const offlineText = ref("");
const errors = ref({});

watch(user, (newValue) => {
  form.value = newValue;
});

const submitForm = () => {
  axios
    .post("/user/update/", form.value)
    .then((responsee) => {
      console.log(response.data);
    })
    .catch((err) => {
      if (!err.response) {
        offlineText.value = "Please check your internet connection";
      } else if (err.response.status == 400) {
        errors.value = err.response.data.error;
      }
    });
};
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
