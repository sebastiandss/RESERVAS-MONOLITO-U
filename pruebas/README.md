# Pruebas

Suite de pruebas automatizadas con `unittest` (incluido en Python, sin dependencias externas).

## Ejecutar

```bash
cd /home/sebas/monolito-reservas
python -m unittest discover -s pruebas -t . -v
```

## Reservas (paso 7)

- `apoyo_gestion_reservas.py`: base con JSON temporales; redirige las rutas del gestor con `patch.object`.
- `test_gestion_reservas_alta.py`: alta válida, campos del modelo e IDs únicos.
- `test_gestion_reservas_validaciones.py`: existencia de usuario/espacio, actividad, fechas y horarios.
- `test_gestion_reservas_conflictos.py`: solapes con `Aprobada`, franjas adyacentes y estados no bloqueantes.

## Estados de reservas (paso 8)

- `apoyo_gestion_estados.py`: base con JSON temporales; redirige la ruta del gestor de estados.
- `test_gestion_estados_validaciones.py`: estados válidos, rechazo de estados inválidos, ID inexistente y guardado.
- `test_gestion_estados_conflictos.py`: solapes al aprobar, franjas adyacentes y estados no bloqueantes.
- `test_gestion_estados_transiciones.py`: aprobación repetida y cambios posteriores de estado.

## Heredadas (pasos 1 a 6)

Están en `pruebas/legado/` y se siguen ejecutando con el mismo comando.

- `test_modelos.py`: contrato de las funciones de `models/`.
- `test_validaciones.py`: fechas, horas, franjas y campos obligatorios.
- `test_almacen_json.py`: carga y guardado JSON en archivos temporales.
- `test_datos_ejemplo.py`: integridad de `datos_ejemplo/` (IDs, FKs, formatos y estados).
- `test_solapamientos.py`: cruces esperados entre reservas activas del dataset.
- `apoyo_gestion_espacios.py` y `test_gestion_espacios_*.py`: alta, baja y listado de espacios.
- `apoyo_gestion_usuarios.py` y `test_gestion_usuarios_*.py`: alta, baja y listado de usuarios.

## Notas

- No se escribe en `data/`; todas las pruebas usan `tempfile`.
- La suite completa tiene **77 pruebas**: 75 OK y 2 `expected failures`.
- `legado/test_almacen_json.py` tiene 2 pruebas con `@unittest.expectedFailure` que documentan deudas pendientes: archivo inexistente y JSON dañado. Cuando se implementen, hay que quitar el decorador.
- Las pruebas del dataset leen `datos_ejemplo/` en modo solo lectura.
