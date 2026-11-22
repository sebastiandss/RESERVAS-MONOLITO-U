# Pruebas

Suite de pruebas automatizadas con `unittest` (incluido en Python, sin dependencias externas).

## Ejecutar

```bash
cd /home/sebas/monolito-reservas
python -m unittest discover -s pruebas -t . -v
```

Resultado actual: **107 pruebas, todas OK** (0 `expected failures`).

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

## Consultas (paso 9)

- `apoyo_consultas.py`: base con JSON temporales; redirige las rutas de los tres módulos de consulta.
- `test_consultas_asignaciones.py`: solo `Aprobada`, nombres legibles y aviso sin resultados.
- `test_consultas_disponibilidad.py`: `Aprobada` bloquea; `Pendiente`/`Cancelada` no; franjas adyacentes.
- `test_consultas_coincidentes.py`: solo reservas activas, solapes y validaciones.

## Ajustes finales (A01)

- `test_almacen_json.py`: archivo ausente, vacío, dañado, no lista, guardado atómico y limpieza de `.tmp` (5 pruebas).
- `test_aviso_pendientes.py`: aviso al solapar `Pendiente`, franja adyacente, `Cancelada` y no persistencia (5 pruebas).
- `test_acentos_espacios.py`: `SALON`/`Salón`, `SALÓN`/`Salón` y nombres distintos (4 pruebas).

## Heredadas (pasos 1 a 6)

Están en `pruebas/legado/` y se siguen ejecutando con el mismo comando; sus módulos de apoyo están en `pruebas/`.

- `test_modelos.py`: contrato de las funciones de `models/`.
- `test_validaciones.py`: fechas, horas, franjas y campos obligatorios.
- `test_almacen_json.py`: guardar/cargar, archivo ausente, vacío y JSON dañado con respaldo (antes 2 `expected failures`, ya resueltas).
- `test_datos_ejemplo.py`: integridad de `datos_ejemplo/` (IDs, FKs, formatos y estados).
- `test_solapamientos.py`: cruces esperados entre reservas activas del dataset.
- `apoyo_gestion_espacios.py` y `test_gestion_espacios_*.py`: alta, baja y listado de espacios.
- `apoyo_gestion_usuarios.py` y `test_gestion_usuarios_*.py`: alta, baja y listado de usuarios.

## Notas

- No se escribe en `data/`; todas las pruebas usan `tempfile`.
- La suite completa tiene **107 pruebas**: 49 heredadas, 16 de reservas, 12 de estados, 16 de consultas y 14 de los ajustes finales.
- Ya no hay decoradores `@unittest.expectedFailure`: los dos casos de la capa JSON pasan y ninguna prueba se eliminó.
- Las pruebas del dataset leen `datos_ejemplo/` en modo solo lectura.
- El detalle de los hallazgos y su resolución está en la nota de Obsidian `Memoria/Pruebas y hallazgos.md`.
