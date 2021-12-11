<template>
  <div class="greetings" v-if="userData">
    <h1>
      <!-- ¡Bienvenido <span> {{ username }} </span>! -->
      ¡Bienvenido !
    </h1>
  </div>
</template>

<script>
import axios from "axios";
import NProgress from "nprogress";
import { useAuthStore } from "../store/auth";

export default {
  name: "Home",
  data: function () {
    return {
      // username: localStorage.getItem("username") || "none",
      authStore: useAuthStore(),
      userData: null,
    };
  },

  // created() {
  //   NProgress.start();
    
  //     .then(() => NProgress.done());
  // },

  methods: {
    getUserData() {
      return axios
      .get("http://127.0.0.1:8000/" + this.authStore.userId, {
        headers: {
          Authorization: `Bearer ${this.authStore.currentUser.access}`,
        },
      })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      })
    },

    
  }
};
</script>

<style>
.greetings {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.greetings h1 {
  font-size: 50px;
  color: #283747;
}
.greetings span {
  color: crimson;
  font-weight: bold;
}
</style>