# API REST - UVShop

La API de UVShop sigue los principios de diseño REST y permite la gestión de **Productos**, **Clientes**, **Pedidos** y **Pagos**.

---

## 1. Gestión de Clientes

### Crear Cliente

- **Endpoint:** `/clientes`
- **Método HTTP:** `POST`
- **Descripción:** Registra un nuevo cliente.

#### Cuerpo:

```json
{
  "nombre": "pepe",
  "email": "pepe@pepe.com",
  "direccion": "Francia",
  "tipo": "nuevo"
}
```

#### Respuesta:

- `201 Created`

```json
{
  "id": 1,
  "nombre": "pepe",
  "email": "pepe@pepe.com",
  "direccion": "Francia",
  "tipo": "nuevo"
}
```

---

### Obtener Cliente

- **Endpoint:** `/clientes/{cliente_id}`
- **Método HTTP:** `GET`
- **Descripción:** Detalles de un cliente específico.

#### Respuestas:

- `200 OK`
- `404 Not Found`

---

### Eliminar Cliente

- **Endpoint:** `/clientes/{cliente_id}`
- **Método HTTP:** `DELETE`
- **Descripción:** Elimina un cliente existente.

#### Respuestas:

- `200 OK`
- `404 Not Found`

---

## 🔹 2. Gestión de Pedidos

### Crear Pedido

- **Endpoint:** `/clientes/{cliente_id}/pedidos`
- **Método HTTP:** `POST`
- **Descripción:** Realiza un pedido.

#### Respuestas:

- `201 Created`
- `400 Bad Request`
- `404 Not Found`

---

### Obtener Pedidos

- **Endpoint:** `clientes/{cliente_id}/pedidos`
- **Método HTTP:** `GET`
- **Descripción:** Obtener pedidos para un cliente con sus productos.

#### Respuestas:

- `200 OK`

```json
[
  {
    "id": 1,
    "estado": "en preparación",
    "productos": [
      {
        "id": 1,
        "nombre": "Brave New World",
        "precio": 40,
        "stock": 23,
        "pedido_id": 1
      }
    ],
    "precio_estandar": 10,
    "cliente_id": 1
  }
]
```

- `404 Not Found`

---

### Obtener Pedido

- **Endpoint:** `clientes/{cliente_id}/pedidos/{pedido_id}`
- **Método HTTP:** `GET`
- **Descripción:** Detalles de un pedido por ID.

#### Respuestas:

- `200 OK`

```json
{
  "id": 1,
  "estado": "en preparación",
  "productos": [
    {
      "id": 1,
      "nombre": "The Trial",
      "precio": 42.0,
      "stock": 20,
      "pedido_id": 1
    }
  ],
  "precio_estandar": 10,
  "cliente_id": 1
}
```

- `404 Not Found`

---

### Actualizar Estado de Pedido

- **Endpoint:** `clientes/{cliente_id}/pedidos/{pedido_id}/estado`
- **Método HTTP:** `PUT`
- **Descripción:** Cambia el estado del pedido.

```json
{
  "estado": "pendiente" | "pagado" | "en preparación" | "enviado" | "entregado" | "cancelado"
}
```

#### Respuestas:

- `200 OK`
- `404 Not Found`
- `400 Bad Request`

---

### Cancelar Pedido

- **Endpoint:** `clientes/{cliente_id}/pedidos/{pedido_id}`
- **Método HTTP:** `DELETE`
- **Descripción:** Cancela un pedido.

#### Respuestas:

- `200 OK`
- `404 Not Found`
- `400 Bad Request`

---

## 3. Gestión de Productos

### Crear Producto

- **Endpoint:** `/clientes/{cliente_id}/pedidos/{pedido_id}/productos`
- **Método HTTP:** `POST`
- **Descripción:** Crea un nuevo producto para un pedido de un cliente

#### Cuerpo de la solicitud:

```json
{
  "nombre": "1984",
  "precio": 19.99,
  "stock": 50
}
```

#### Respuestas:

- `201 Created`
- `422 Unprocessable Entity`

---

### Listar Productos

- **Endpoint:** `/clientes/{cliente_id}/pedidos/{pedido_id}/productos`
- **Método HTTP:** `GET`
- **Descripción:** Lista todos los productos de un pedido.

#### Respuesta:

- `200 OK`

```json
[
  {
    "id": 1,
    "nombre": "1984",
    "precio": 19.99,
    "stock": 3,
    "pedido_id": 1
  },
  {
    "id": 2,
    "nombre": "Fahrenheit 451",
    "precio": 30.0,
    "stock": 5,
    "pedido_id": 1
  }
]
```

---

## 4. Gestión de Pagos

### Procesar Pago

- **Endpoint:** `/pagos`
- **Método HTTP:** `POST`
- **Descripción:** Procesa el pago de un pedido.

#### Cuerpo:

```json
{
  "pedido_id": "ped_789",
  "monto": 1999.98,
  "metodo_pago": "tarjeta",
  "detalles_pago": {
    "numero_tarjeta": "**** **** **** 1234",
    "cvv": "123",
    "fecha_expiracion": "12/25"
  }
}
```

#### Respuesta:

- `200 OK`

```json
{
  "status": "success",
  "data": {
    "pago_id": "pay_xyz",
    "estado": "procesado",
    "pedido_id": "ped_789"
  }
}
```

- `400 Bad Request`
- `404 Not Found`

---

## Notas Finales

- Todos los endpoints retornan respuestas en formato JSON.
- Esta API está diseñada para uso interno de la plataforma UVShop.
