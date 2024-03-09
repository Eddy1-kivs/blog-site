// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxt/ui"],
  plugins: [{ ssr: false, src: "plugins/axios" }],
  ssr: false,
  app: {
    head: {
      title: "BLOG",
      link: [
        { rel: "icon", type: "image/x-icon", href: "/icon2.ico" },
        { rel: "preconnect", href: "https://fonts.googleapis.com" },
        {
          rel: "preconnect",
          href: "https://fonts.gstatic.com",
          crossorigin: "",
        },
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
        },
      ],
      meta: [],
    },
  },
  colorMode: {
    preference: "light",
  },

  tiptap: {
    prefix: "Tiptap", //prefix for Tiptap imports, composables not included
  },

  runtimeConfig: {
    public: {
      baseURL: "http://localhost:8000",
      appName: "Blog",
    },
  },
});
