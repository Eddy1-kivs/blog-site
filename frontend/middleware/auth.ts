export default defineNuxtRouteMiddleware((to, from) => {
  let isAuthenticated = useAuthenticated();

  const guestPages = ["/auth/register", "/auth/register/"];

  console.log(to.path);

  if (isAuthenticated.value == true && to.path.startsWith("/auth")) {
    // console.log("redirecting");
    return navigateTo("/auth/login");
  }
});
