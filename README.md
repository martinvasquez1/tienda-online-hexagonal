# Tienda online hexagonal

Este repositorio implementa una tienda con pedidos y productos utilizando arquitectura hexagonal. Esta estructura facilitará la escalabilidad y el mantenimiento del sistema.

## Ejectuar

### Empezar app

```bash
uvicorn src.main:app --reload
```

### Pruebas

Actualmente el programa solo cuenta con pruebas de e2e.

```bash
pytest
```

## Instalar dependencias

### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Linux

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Convenciones de los mensajes de commit

`feat`: para nuevas características. \
`fix`: para correcciones de errores. \
`refactor`: para cambios en el código que no afectan el comportamiento externo. \
`docs`: para cambios en la documentación. \
`style`: para cambios que no afectan el significado del código (espacios en blanco, formato, etc.). \
`test`: para agregar o modificar pruebas automatizadas en el código. \
`chore`: para tareas de mantenimiento y organización del proyecto que no afectan la funcionalidad.
