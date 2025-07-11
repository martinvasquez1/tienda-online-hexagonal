import pytest
from fastapi.testclient import TestClient
from src.main import app

from src.infrastructure.dependencies.dependencias_producto import (
    obtener_servicio_prodcuto,
)
from src.application.servicio_producto import ServicioProducto
from src.infrastructure.repositories.repositorio_producto_in_memory import (
    RepositorioProductoInMemory,
)

client = TestClient(app)


# Fixture para reiniciar el repositorio antes de cada prueba
@pytest.fixture(autouse=True)
def reset_repo():
    app.dependency_overrides[obtener_servicio_prodcuto] = lambda: ServicioProducto(
        RepositorioProductoInMemory()
    )
    yield


def test_crear_producto_e2e():
    producto1 = {"nombre": "Pokemon Rojo Fuego", "precio": 10.0}
    response = client.post("/productos/", json=producto1)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nombre": "Pokemon Rojo Fuego",
        "precio": 10.0,
    }


def test_obtener_productos_e2e():
    producto1 = {"nombre": "Pokemon Rojo Fuego", "precio": 10.0}
    producto2 = {"nombre": "Pokemon Azul", "precio": 12.0}
    client.post("/productos/", json=producto1)
    client.post("/productos/", json=producto2)

    response = client.get("/productos/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == [
        {"id": 1, "nombre": "Pokemon Rojo Fuego", "precio": 10.0},
        {"id": 2, "nombre": "Pokemon Azul", "precio": 12.0},
    ]


def test_obtener_productos_vacios():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert response.json() == []


def test_obtener_productos_e2e():
    pass


def test_actualizar_producto_e2e():
    pass


def test_eliminar_producto_e2e():
    pass
