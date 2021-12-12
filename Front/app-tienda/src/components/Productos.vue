<template>
  <!-- <div class="cointainer-menu">
    <h3>producto categoria</h3>
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
            <v-bton>Editar</v-bton>
            <v-bton>Eliminar</v-bton>
          </td>
        </tr>
      </tbody>
    </table>
  </div> -->

  <v-data-table
    :headers="headers"
    :items="productos"
    sort-by="Categoria"
    class="elevation-3"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Lista de Productos</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on" @click="crearProducto()">
              Crear Producto
            </v-btn>
          </template>

          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.id"
                      
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.categoria"
                      label="Categoria"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.marca"
                      label="Marca"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.nombre"
                      label="Nombre"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.precio"
                      label="Precio"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.ref"
                      label="Referencia"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.unidad_medida"
                      label="unidad de medida"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="producto.unidades_disponibles"
                      label="unidades disponibles"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this item?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>

      </v-toolbar>
    </template>

    <template v-slot:item="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>

    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize"> Reset </v-btn>
    </template>

  </v-data-table>

</template>




<script>
import axios from "axios";
import NProgress from "nprogress";

export default {
  name: "Productos",
  data: function () {
    return {
      productos: [],
      producto: {
        id: null,
        categoria: "",
        marca: "",
        nombre: "",
        precio: 0,
        ref: "",
        unidad_medida: "",
        unidades_disponibles: 0,
      },

      headers: [
        {
          text: "Nombre Producto",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "Categoria", value: "Categoria" },
        { text: "Marca", value: "Marca" },
        { text: "Precio", value: "Precio" },
        { text: "Unidades Disponibles", value: "Unidades Disponibles" },
        { text: "Acciones", value: "actions", sortable: false },
      ],
      dialog: false,
      dialogDelete: false,
    };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nuevo Producto" : "Editar Producto";
    },
  },

  watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

  created: function () {
    this.listarProductos();
  },


  methods: {
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
      NProgress.start();
      axios
        .post("http://127.0.0.1:8000/producto/crear/", {categoria:this.producto.categoria, 
        marca:this.producto.marca, nombre:this.producto.nombre, precio:this.producto.precio,
        ref:this.producto.ref, unidad_medida:this.producto.unidad_medida, unidades_disponibles:this.producto.unidades_disponibles})
        .then((response) => {
          console.log(response);
          this.listarProductos();
        })
        this.producto.categoria='', 
        this.producto.marca='', 
        this.producto.nombre='', 
        this.producto.precio=0,
        this.producto.ref='', 
        this.producto.unidad_medida='', 
        this.producto.unidades_disponibles=0
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    listarProducto() {
      NProgress.start();
      axios
        .get("http://127.0.0.1:8000/producto/" + id)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    actualizarProducto() {
      NProgress.start();
      axios
        .put("http://127.0.0.1:8000/producto/" + id)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    borrarProducto() {
      NProgress.start();
      axios
        .delete("http://127.0.0.1:8000/producto/" + id)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    numberFormat(value) {
      const formatter = new Intl.NumberFormat("es-CO", {
        style: "currency",
        currency: "COP",
        minimumFractionDigits: 0,
      });

      return formatter.format(value);
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