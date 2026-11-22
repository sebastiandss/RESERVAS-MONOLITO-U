# Pruebas

Suite de pruebas automatizadas con `unittest` (incluido en Python, sin dependencias externas).

## Ejecutar

```bash
cd /home/sebas/monolito-reservas
python -m unittest discover -s pruebas -t . -v
```

## Archivos

- `test_modelos.py`: contrato de las funciones de `modelos/`.
- `test_validaciones.py`: fechas, horas, franjas y campos obligatorios.
- `test_almacen_json.py`: carga y guardado JSON en archivos temporales.
- `test_datos_ejemplo.py`: integridad de `datos_ejemplo/` (IDs, FKs, formatos y estados).
- `test_solapamientos.py`: cruces esperados entre reservas activas del dataset.
- `apoyo_gestion_espacios.py`: base con JSON temporales para las pruebas de espacios.
- `test_gestion_espacios_alta.py`: alta, validaciones, IDs y nombres duplicados.
- `test_gestion_espacios_borrado.py`: baja con y sin reservas (actuales y legadas).
- `test_gestion_espacios_listado.py`: lista vacía y orden por nombre.

## Notas

- No se escribe en `data/`; las pruebas de persistencia usan `tempfile`.
- La suite completa tiene **35 pruebas**: 33 OK y 2 `expected failures`.
- `test_almacen_json.py` tiene 2 pruebas con `@unittest.expectedFailure` que documentan deudas pendientes: archivo inexistente y JSON dañado. Cuando se implementen, hay que quitar el decorador.
- Las pruebas del dataset leen `datos_ejemplo/` en modo solo lectura.
