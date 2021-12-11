<template>
  <div class="cointainer-menu" >
    <h3>producto categoria </h3>
    <table class="centered container-table" >
      <thead >
        <tr >
          <th>nombre producto</th>
          <th>descripcion</th>
          <th>precio</th>
        </tr>
      </thead>
      <tbody>
        <tr >
          <td>morfeo me llama</td>
          <td>morfeo me llama1</td>
          <td>morfeo me llama2</td>
          
        </tr>
      </tbody>
      <!-- <li>nombre producto {{}} descripcion {{}} precio</li> -->
    </table>
  </div>
</template>

<script>
export default {
  name: "Menu",
  data: function () {
    return {};
  },
  methods: {
    producto() {
      NProgress.start();
      axios
        .get("http://127.0.0.1:8000/producto/")
        .then((response) => {
          console.log(response);
          
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
  },
};
</script>

<style>
.cointainer-menu {
  position: absolute;
  top: 175px;
  right: 85px;
  background-color: rgb(167 165 165 / 53%);
  left: 125px;
  border-radius: 20px;
  box-shadow: 11px 16px 41px #e5e7e9;
}
.cointainer-menu h3 {
  color: white;
  font-size: 2rem;
  padding: 0 90px;
}

.cointainer-menu li {
  margin-left: 80px;
  font-size: 18px;
}

.container-table {
  margin: 0 0 12px 0px;
  background-color: rgb(255 255 255 / 70%);
}
</style>