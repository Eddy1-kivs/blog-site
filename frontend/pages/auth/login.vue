<!-- components/Login.vue -->
<template>
  <div
    class="press-start-text bg-[#fde7be] min-h-screen h-full flex items-center justify-center"
  >
    <div class="login-container">
      <h2 class="pb-10">Login</h2>

      <form @submit.prevent="submitForm">
        <div class="text-red-600 text-xs text-center mt-2">
          {{ internetError }}
        </div>

        <div class="form-group">
          <div for="username" class="w-full text-start">Username:</div>

          <input
            type="text"
            id="username"
            v-model="form.username"
            class="input-field"
          />
          <div
            v-if="errors.username"
            class="inline-flex w-full flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
          >
            <div v-for="(error, index) in errors.username" :key="index">
              {{ error }}
            </div>
          </div>
          <div class="text-red-600 text-xs text-start mt-2">{{ error }}</div>
        </div>

        <div class="form-group">
          <div for="username" class="w-full text-start">Password:</div>

          <input
            type="password"
            id="password"
            v-model="form.password"
            class="input-field"
          />

          <div
            v-if="errors.password"
            class="inline-flex w-full flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
          >
            <div v-for="(error, index) in errors.password" :key="index">
              {{ error }}
            </div>
          </div>
        </div>
        <!-- <UButton name="jhddbb">www</UButton> -->
        <button type="submit" class="login-button">Login</button>
        <div class="forgot-password">
          <router-link to="/forgot-password">Forgot Password?</router-link>
        </div>
      </form>

      <div class="register-link">
        <router-link to="/auth/register" class="register-link-text">
          Don't have an account? <span class="blue-text">Register here.</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { login } from "~/.utils/axiosConfigurations";
let configs = useRuntimeConfig();
const form = ref({
  username: "",
  password: "",
});
const internetError = ref("");
const errors = ref({});
const toast = useToast();
const submitForm = () => {
  errors.value = {};
  internetError.value = "";
  axios
    .post("/login/", form.value)
    .then((response) => {
      console.log("success");
      localStorage.setItem("token", response.data.access);
      login(response.data.access);

      toast.add({ title: "Login successful" });
      navigateTo("/account/profile");
    })
    .catch((err) => {
      console.error(err);
      if (!err.response) {
        internetError.value = "Please check your internet connection.";
      } else if (err.response.status == 400) {
        errors.value = err.response.data;
      } else if (err.response.status == 401) {
        console.log([err.response.data.error]);
        errors.value["username"] = [err.response.data.error];
      }
    });
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

.press-start-text {
  font-family: "Press Start 2P";
  background-color: #fde7be;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.input-field {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.login-button {
  background-color: #007bff;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.forgot-password {
  margin-top: 0.5rem;
}

.register-link {
  margin-top: 1rem;
}

.register-link-text {
  color: #000;
}

.blue-text {
  color: #007bff;
}

/* Add any additional styling as needed */
</style>
