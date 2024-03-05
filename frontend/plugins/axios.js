import { login } from "../.utils/axiosConfigurations";

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook("app:beforeMount", () => {
    login();
  });
});
