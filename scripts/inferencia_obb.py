"""Inferencia con YOLOv8n-obb sobre imágenes aéreas (detección con cajas orientadas).

Uso:
    python scripts/inferencia_obb.py --imagen imagenes/ElDorado.png
    python scripts/inferencia_obb.py --imagen imagenes/BahiaSM.png --conf 0.25 --imgsz 1024
"""

import argparse
import glob
import os

from PIL import Image
from ultralytics import YOLO


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analiza una imagen aérea con YOLOv8n-obb y muestra las detecciones."
    )
    parser.add_argument(
        "--imagen",
        required=True,
        help="Ruta de la imagen a analizar (p. ej. imagenes/ElDorado.png)",
    )
    parser.add_argument(
        "--modelo",
        default="yolov8n-obb.pt",
        help="Ruta de los pesos del modelo (se descarga automáticamente si no existe)",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Umbral de confianza mínimo (por defecto: 0.25)",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=1024,
        help="Tamaño de imagen de la red (por defecto: 1024)",
    )
    return parser.parse_args()


def mostrar_imagen(ruta: str) -> None:
    """Muestra la imagen anotada en Colab (display) o en local (visor del sistema)."""
    archivos = glob.glob(f"runs/obb/predict*/{os.path.basename(ruta)}")
    if not archivos:
        print(
            "⚠️ No se pudo proyectar la imagen automáticamente. "
            "Revisa la carpeta 'runs/obb/' en tu barra lateral."
        )
        return

    # Selecciona siempre el resultado de la corrida más reciente
    archivos.sort(key=os.path.getmtime)
    ultima_prediccion = archivos[-1]

    img_final = Image.open(ultima_prediccion)
    try:
        # En Google Colab / Jupyter se despliega la imagen en la celda
        from IPython.display import display

        display(img_final)
    except ImportError:
        # En Python local se abre con el visor de imágenes del sistema
        img_final.show()


def main():
    args = parse_args()

    if not os.path.exists(args.imagen):
        raise FileNotFoundError(f"❌ No se encontró la imagen: {args.imagen}")

    # 1. Inicializar el modelo
    print("🛸 Inicializando modelo de teledetección...")
    model = YOLO(args.modelo)

    # 2. Ejecutar la inferencia (imgsz=1024 es el tamaño óptimo de la red)
    nombre_imagen = os.path.basename(args.imagen)
    print(f"🛰️ Analizando {nombre_imagen}...")
    resultados = model.predict(
        source=args.imagen, save=True, conf=args.conf, imgsz=args.imgsz
    )

    # 3. Listar las detecciones encontradas
    print("\n--- 📊 Resultados del Análisis Territorial ---")
    total_detectados = 0
    for result in resultados:
        n_objetos = len(result.obb)
        total_detectados += n_objetos
        print(f"Total de objetos detectados: {n_objetos}")
        for box in result.obb:
            clase = model.names[int(box.cls)]
            confianza = float(box.conf)
            print(f"• {clase.capitalize()} detectado con {confianza * 100:.1f}% de certeza.")
    if total_detectados == 0:
        print("❌ No se detectaron objetos con el umbral de confianza actual.")

    # 4. Buscar y mostrar la imagen resultante
    print("\n🖼️ Desplegando mapa de detecciones finales...")
    mostrar_imagen(args.imagen)


if __name__ == "__main__":
    main()
