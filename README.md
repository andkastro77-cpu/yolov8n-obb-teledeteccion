# YOLOv8n-obb — Detección con cajas orientadas para teledetección

## Descripción general

**YOLOv8n-obb** es la variante *nano* de la familia YOLOv8 de [Ultralytics](https://github.com/ultralytics/ultralytics), especializada en la tarea **OBB** (*Oriented Bounding Box*, detección con cajas orientadas). A diferencia de un detector tradicional, cada predicción incluye un ángulo de rotación, lo que permite encerrar objetos alineados con su orientación (aviones, barcos, vehículos, puentes) en imágenes aéreas y satelitales sin incluir fondo innecesario. El modelo viene preentrenado sobre el conjunto **DOTAv1** (15 clases de objetos en imágenes aéreas) y, en este repositorio, se aplica al análisis territorial de teledetección sobre tres zonas de prueba: el Aeropuerto El Dorado, la Bahía de Santa Marta y una imagen de España.

## Ficha del modelo

Los datos técnicos, fuentes, estructura, sesgos, limitaciones y citación están documentados en:

📄 **[Ficha del modelo YOLOv8n-obb](fichas/ficha-yolov8n-obb.md)**

## Autor

- Leonel Andrés Cárdenas Castro

## Estructura del repositorio

```
yolov8n-obb-teledeteccion/
├── README.md                       # Este archivo
├── fichas/
│   └── ficha-yolov8n-obb.md        # Ficha descriptiva del modelo
├── scripts/
│   ├── inferencia_obb.py           # Script unificado de inferencia
│   └── verificar_entorno.py        # Chequeo de GPU (Google Colab / local)
├── imagenes/
│   ├── ElDorado.png                # Aeropuerto El Dorado (aviones)
│   ├── BahiaSM.png                 # Bahía de Santa Marta (barcos)
│   └── Espana.png                  # Imagen aérea de España
├── requirements.txt
└── .gitignore
```

## Requisitos

- Python 3.9+
- Google Colab (con GPU) o un equipo local con GPU NVIDIA (opcional)

```bash
python -m pip install -r requirements.txt
```

Los pesos `yolov8n-obb.pt` se descargan automáticamente de Ultralytics en la primera ejecución.

## Uso

1. **Verificar el entorno** (GPU):

   ```bash
   python scripts/verificar_entorno.py
   ```

2. **Ejecutar la inferencia** sobre una imagen:

   ```bash
   python scripts/inferencia_obb.py --imagen imagenes/ElDorado.png
   python scripts/inferencia_obb.py --imagen imagenes/BahiaSM.png
   python scripts/inferencia_obb.py --imagen imagenes/Espana.png
   ```

| Parámetro | Descripción | Por defecto |
|-----------|-------------|-------------|
| `--imagen` | Ruta de la imagen a analizar (obligatorio) | — |
| `--modelo` | Ruta de los pesos `.pt` | `yolov8n-obb.pt` |
| `--conf` | Umbral de confianza mínimo | `0.25` |
| `--imgsz` | Tamaño de imagen de la red | `1024` |

## Resultados

- La consola imprime cada detección con su clase y porcentaje de certeza.
- La imagen anotada se guarda automáticamente en `runs/obb/predict*/` y se muestra al finalizar.
- En Google Colab, la imagen se despliega automáticamente en la celda (usa `display()`); en local se abre con el visor de imágenes del sistema.

## Licencia y créditos

- Modelo: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) — licencia **AGPL-3.0** (también disponible licencia Enterprise).
- Datos de preentrenamiento: conjunto [DOTA](https://captain-whu.github.io/DOTA/) (Ding et al., CVPR 2018).
- Consulta la [ficha del modelo](fichas/ficha-yolov8n-obb.md) para la citación oficial.
