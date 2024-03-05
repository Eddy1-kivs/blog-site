<!-- components/Register.vue -->
<template>
  <div
    class="press-start-text bg-[#fde7be] min-h-screen h-full flex text-black items-center justify-center"
  >
    <div class="register-container">
      <h2 class="pb-10">Register</h2>
      <form>
        <div class="text-sm text-center">{{ offlineText }}</div>
        <div class="form-group">
          <div for="username" class="w-full text-start">Username:</div>
          <input
            type="text"
            class="input-field"
            id="username"
            v-model="form.username"
          />
          <div
            v-if="errors.username"
            class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
          >
            <div v-for="(error, index) in errors.username" :key="index">
              {{ error }}
            </div>
          </div>
        </div>
        <div class="form-group">
          <div for="username" class="w-full text-start">Email:</div>

          <input
            type="email"
            class="input-field"
            id="email"
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

        <div class="form-group">
          <div for="username" class="w-full text-start">Password:</div>

          <input
            type="password"
            class="input-field"
            id="password"
            v-model="form.password"
          />
          <div
            v-if="errors.password"
            class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
          >
            <div v-for="(error, index) in errors.password" :key="index">
              {{ error }}
            </div>
          </div>
        </div>

        <div class="form-group">
          <div for="username" class="w-full text-start">Confirm Password:</div>
          <input
            type="password"
            class="input-field"
            id="confirm-password"
            v-model="form.confirm_password"
          />
          <div
            v-if="errors.confirm_password"
            class="inline-flex flex-col gap-y-2 text-xs mt-2 text-red-600 text-start"
          >
            <div v-for="(error, index) in errors.confirm_password" :key="index">
              {{ error }}
            </div>
          </div>
        </div>
        <button class="register-button" type="button" @click="submitForm()">
          Register
        </button>
      </form>

      <div class="login-link">
        <router-link to="/auth/login" class="login-link-text">
          Already have an account? <span class="blue-text">Login here.</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { login, setAxiosConfigurations } from "~/.utils/axiosConfigurations";
const errors = ref({});
const offlineText = ref("");
const form = {
  username: "",
  email: "",
  password: "",
  confirm_password: "",
};
const toast = useToast();

const auth = useAuthenticated();
const configs = useRuntimeConfig();
const submitForm = () => {
  console.log("register");
  errors.value = {};

  axios
    .post("/register/", form)
    .then((response) => {
      localStorage.setItem("token", response.data.access);
      login(response.data.access);
      setAxiosConfigurations();
      navigateTo("/account/profile");
      toast.add({ title: "Register successful" });
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
  max-width: 400px;
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
