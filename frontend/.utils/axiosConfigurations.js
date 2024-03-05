import axios from "axios";

export const setAxiosConfigurations = () => {
  const accessToken = localStorage.getItem("token");
  let env = useRuntimeConfig();
  axios.defaults.baseURL = env.public.baseURL;
  axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`;
  // axios.defaults.headers.get["Content-Type"] = "application/json";
  // axios.defaults.headers.get["Access-Control-Allow-Origin"] = "*";
  console.log("Axios");
  axiosInterceptor();
};

export const authenticateUser = () => {
  let isAuthenticated = useAuthenticated();
  let user = useUser();

  axios
    .get("/user/")
    .then((response) => {
      user.value = response.data;
    })
    .catch((err) => {
      console.log(err);
      if (err.response.status === 403) {
        isAuthenticated.value = false;
      }
    });
};

export const axiosInterceptor = () => {
  axios.interceptors.request.use(
    function (config) {
      return config;
    },
    function (error) {
      return Promise.reject(error);
    }
  );
  axios.interceptors.response.use(
    function (response) {
      return response;
    },
    function (error) {
      if (error.response && error.response.status === 401) {
        logout();
      }
      return Promise.reject(error);
    }
  );
};

export const logout = () => {
  localStorage.removeItem("token");
  let isAuthenticated = useAuthenticated();
  isAuthenticated.value = false;

  let guestRoutes = ["/", "/articles", "/test"];
  const route = useRoute(); // Make sure you import useRoute from vue-router

  if (!guestRoutes.includes(route.path) && !route.path.startsWith("/auth")) {
    navigateTo("/auth/login");
  }
};

export const login = (accessToken) => {
  if (accessToken) {
    localStorage.setItem("token", accessToken);
  }

  let isAuthenticated = useAuthenticated();
  isAuthenticated.value = true;

  setAxiosConfigurations();
  authenticateUser();
};
