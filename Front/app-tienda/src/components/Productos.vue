<template>
  <div class="cointainer-menu">
    <h3>Listado de productos</h3>
    <button @click="modalCrear = true">Crear Producto</button>

    <div v-if="modalCrear" class="centrar-modal">
      <transition name="fade">
        <div class="row">
          <div class="col s12">
            <div class="card">
              <div class="card-content">
                <span class="card-title">Crear Producto</span>
                <form class="col s12">
                  <div class="row">
                    <div class="input-field col s6">
                      
                  </div>
                  </div>
                </form>
              </div>
              <div class="card-action bton">
                <button @click="crearProducto()">Guardar</button>
                <button>Cancelar</button>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>

    <table class="centered container-table">
      <thead>
        <tr>
          <th>Nombre Producto</th>
          <th>Categoria</th>
          <th>Marca</th>
          <th>Precio</th>
          <th>Unidades Disponibles</th>
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
            <button
              class="teal accent-4"
              dark
              @click="listarProducto(producto.id)"
            >
              Editar
            </button>
            <button class="error" darck @click="borrarProducto(producto.id)">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
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
      nuevoProducto: {
        categoria: "",
        marca: "",
        nombre: "",
        precio: 0,
        ref: "",
        unidad_medida: "",
        unidades_disponibles: 0,
      },
      modalCrear: false,
    };
  },
  computed: {},
  created: function () {
    this.listarProductos();
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
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    crearProducto() {
      axios
        .post("http://127.0.0.1:8000/producto/crear/")
        .then((response) => {
          // this.nuevoProducto.categoria = response.data.categoria;
          console.log(response.data);
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