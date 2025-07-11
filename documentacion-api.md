# API REST - UVShop

La API de UVShop sigue los principios de diseño REST y permite la gestión de **Productos**, **Clientes**, **Pedidos** y **Pagos**.

---

## 1. Gestión de Productos

### Crear Producto

- **Endpoint:** `/clientes/{cliente_id}/pedidos/{pedido_id}/productos`
- **Método HTTP:** `POST`
- **Descripción:** Crea un nuevo producto para un pedido de un cliente

#### Cuerpo de la solicitud:

```json
{
  "nombre": "Laptop",
  "precio": 999.99,
  "stock": 50
}
```

#### Respuestas:

- `201 Created`
- `422 Unprocessable Entity`: Error de validación.

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
    "precio": 11,
    "stock": 3,
    "pedido_id": 1
  },
  {
    "id": 2,
    "nombre": "Fahrenheit 451",
    "precio": 11,
    "stock": 5,
    "pedido_id": 1
  }
]
```

---

### Obtener Producto

- **Endpoint:** `/productos/{producto_id}`
- **Método HTTP:** `GET`
- **Descripción:** Recupera los detalles de un producto específico.

#### Respuestas:

- `200 OK`

```json
{
  "status": "success",
  "data": {
    "id": "123",
    "nombre": "Laptop",
    "precio": 999.99,
    "stock": 50
  }
}
```

- `404 Not Found`

```json
{
  "status": "fail",
  "detail": "Producto con ID {producto_id} no encontrado."
}
```

---

### Actualizar Producto

- **Endpoint:** `/productos/{producto_id}`
- **Método HTTP:** `PUT`
- **Descripción:** Actualiza los detalles de un producto.

#### Cuerpo:

```json
{
  "nombre": "Laptop Pro",
  "precio": 1099.99,
  "stock": 45
}
```

#### Respuestas:

- `200 OK`

```json
{
  "status": "success",
  "data": {
    "id": "123",
    "nombre": "Laptop Pro",
    "precio": 1099.99,
    "stock": 45
  }
}
```

- `404 Not Found`  
  [ ]

---

### Eliminar Producto

- **Endpoint:** `/productos/{producto_id}`
- **Método HTTP:** `DELETE`
- **Descripción:** Elimina un producto existente.

#### Respuestas:

- `204 NO CONTENT`

```json
{
  "status": "success",
  "data": {
    "id": "123",
    "nombre": "Laptop Pro",
    "precio": 1099.99,
    "stock": 45
  }
}
```

- `404 Not Found`

```json
null
```

---

## 2. Gestión de Clientes

### Crear Cliente

- **Endpoint:** `/clientes`
- **Método HTTP:** `POST`
- **Descripción:** Registra un nuevo cliente.

#### Cuerpo:

```json
{
  "nombre": "Juan Pérez",
  "email": "juan.perez@example.com",
  "direccion": "Calle Falsa 123",
  "tipo": "nuevo"
}
```

#### Respuesta:

- `201 Created`

```json
{
  "status": "success",
  "data": {
    "id": "456",
    "nombre": "Juan Pérez",
    "email": "juan.perez@example.com",
    "tipo": "nuevo"
  }
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

## 🔹 3. Gestión de Pedidos

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
- **Descripción:** Obtener pedidos para un cliente

#### Respuestas:

- `200 OK`
- `404 Not Found`

---

### Obtener Pedido

- **Endpoint:** `clientes/{cliente_id}/pedidos/{pedido_id}`
- **Método HTTP:** `GET`
- **Descripción:** Detalles de un pedido por ID.

#### Respuestas:

- `200 OK`
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
