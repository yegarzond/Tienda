<template>
  <div class="cabecera">
    <h1>
      ¡Bienvenido ! <span> {{ userData.name }} </span>
    </h1>
    <div class="greetings">
      <div class="producto">
        <h2>producto</h2>
      </div>
      <div class="inventario">
        <h2>Facturación</h2>
      </div>
      <div class="Venta">
        <h2>Venta</h2>
      </div>
    </div>
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
      authStore: useAuthStore(),
      userData: null,
    };
  },

  created() {
    NProgress.start();
    this.getUserData()
      .then((data) => (console.log(data), (this.userData = data)))
      .catch((error) => {
        if (error.response.status === 401) {
          this.refreshToken().then(() => {
            this.getUserData().then((data) => (this.userData = data));
          });
        } else {
          this.redirectToSignIn();
        }
      })
      .then(() => NProgress.done());
  },

  methods: {
    getUserData() {
      return axios
        .get("http://127.0.0.1:8000/user/detailview/", {
          headers: {
            Authorization: `Bearer ${this.authStore.currentUser.access}`,
          },
        })
        .then((response) => response.data);
    },
    refreshToken() {
      const refresh = this.authStore.currentUser.refresh;

      axios
        .post("http://127.0.0.1:8000/user/detailview/refresh/", { refresh })
        .then((response) => {
          // OBTIENE NUEVO TOKEN
          localStorage.setItem("access", response.data.access);
          this.authStore.$patch({
            currentUser: {
              access: response.data.access,
              refresh,
            },
          });
          console.log("New token:", response.data);
        })
        .catch(() => {
          this.redirectToSignIn();
        });
    },
    redirectToSignIn() {
      this.$router.push({ name: "logIn" });
    },
  },
};
</script>

<style>
/* .greetings {
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
} */
  .cabecera {
    text-align: center;
    padding: 7px;
    
  }
  .cabecera h1 {
    color: white;
    text-shadow: 7px 10px 11px #4caf50, -4px -6px 31px #28bbad;
  }

.greetings {
  display: flex;
    justify-content: space-evenly;
    align-items: center;
}

.producto{
  margin: 0;
  padding: 0;
  border-radius: 15px;
  background-color: blue;
}

.inventario {
  background-color: red;

}
</style>