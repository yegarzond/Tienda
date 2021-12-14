<template>
  <div class="cointainer-menu">
    <h3>Listado de productos</h3>
    <button @click="modalCrear = true">Crear Producto</button>

    <div v-if="modalCrear" class="container">
      <form action="" @submit.prevent="crearProducto()">
        <div class="row">
          <div class="col m12 card-panel">
            <span>Crear Producto</span>
            <div class="row">
              <div class="col m12">
                <label>Nombre Producto</label>
                <input type="text" v-model="nombre" />
              </div>
            </div>
            <div class="row">
              <div class="col m4">
                <label>Categoria</label>
                <input type="text" v-model="categoria" />
              </div>
              <div class="col m4">
                <label>Marca</label>
                <input type="text" v-model="marca" />
              </div>
            </div>
            <div class="row">
              <div class="col m4">
                <label>Precio</label>
                <input type="number" v-model="precio" />
              </div>
              <div class="col m4">
                <label>Referencia</label>
                <input type="text" v-model="ref" />
              </div>
            </div>
            <div class="row">
              <div class="col m4">
                <label>Unidad de medida</label>
                <input type="text" v-model="unidad_medida" />
              </div>
              <div class="col m4">
                <label>Unidades disponibles </label>
                <input type="number" v-model="unidades_disponibles" />
              </div>
            </div>
          </div>
          <div class="card-action bton">
            <button class=""><i class="material-icons">save</i> Guardar</button>

            <button class="">
              <i class="material-icons">cancel</i>Cancelar
            </button>
          </div>
        </div>
      </form>
    </div>

    <table class="centered container-table striped #eceff1 blue-grey lighten-5">
      <thead>
        <tr>
          <th>Nombre Producto</th>
          <th>Categoria</th>
          <th>Marca</th>
          <th>Precio</th>
          <th>Unidades Disponibles</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in productos" :key="item.nombre">
          <td>{{ item.nombre }}</td>
          <td>{{ item.categoria }}</td>
          <td>{{ item.marca }}</td>
          <td>{{ numberFormat(item.precio) }}</td>
          <td>{{ item.unidades_disponibles }}</td>
          <td>
            <button class="" @click="listarProducto(producto.id)">
              <i class="material-icons">create</i>
            </button>
            <button class="" @click="borrarProducto(producto.id)">
              <i class="material-icons">delete</i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <ul>
      <li v-for=""></li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import NProgress from "nprogress";

export default {
  name: "Productos",
  data: function () {
    return {
      productos: [],
      producto: {},
      categoria: "",
      marca: "",
      nombre: "",
      precio: 0,
      ref: "",
      unidad_medida: "",
      unidades_disponibles: 0,

      modalCrear: false,
    };
  },
  computed: {},
  created: function () {
    this.listarProductos();
  },

  mounted() {
    document.addEventListener("DOMContentLoaded", function () {
      var elems = document.querySelectorAll(".modal");
      this.productos = M.Modal.init(elems, null);
    });
  },

  methods: {
    numberFormat(value) {
      const formatter = new Intl.NumberFormat("es-CO", {
        style: "currency",
        currency: "COP",
        minimumFractionDigits: 0,
      });

      return formatter.format(value);
    },
    // showModalCrear() {
    //   this.modalCrear == true;
    //   console.log("Modal")
    // },

    listarProductos() {
      NProgress.start();
      axios
        .get("http://127.0.0.1:8000/producto/")
        .then((response) => {
          this.productos = [...response.data];
          console.log(this.productos);
          if (this.productos.length > 10 ){
            
          }
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    crearProducto() {
      {
        var data = {
          categoria: this.categoria,
          marca: this.marca,
          nombre: this.nombre,
          precio: this.precio,
          ref: this.ref,
          unidad_medida: this.unidad_medida,
          unidades_disponibles: this.unidades_disponibles,
        };
      }

      axios
        .post("http://127.0.0.1:8000/producto/crear/")
        .then(() => {
          console.log();
          this.listarProductos();
        })

        .catch((error) => {
          console.log(error);
        });
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

.centrar-modal {
  z-index: 999999999;
}
</style>