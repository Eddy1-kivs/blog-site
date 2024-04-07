export const useAuthenticated = () => useState("useAuthenticated", () => true);
export const useUser = () =>
  useState("useState", () => {
    return {
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      bio: "",
      about: "",
    };
  });


  export const useCategories = ()=>useState('categories', ()=>[])