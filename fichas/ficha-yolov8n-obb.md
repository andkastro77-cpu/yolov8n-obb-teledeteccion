# Ficha de datos para YOLOv8n-obb (Dataset Card for YOLOv8n-obb)

Modelo de detección de objetos con cajas orientadas (OBB) de la familia YOLOv8 de Ultralytics, preentrenado sobre el conjunto DOTAv1 de imágenes aéreas (15 clases: aviones, barcos, vehículos, puentes, puertos, etc.).

## Detalles del conjunto de datos (Dataset Details)

### Descripción del conjunto de datos (Dataset Description)

**YOLOv8n-obb** es la variante *nano* del modelo YOLOv8 para la tarea de **detección con cajas orientadas** (*Oriented Bounding Box*, OBB). Fue desarrollado por [Ultralytics](https://github.com/ultralytics/ultralytics) y la variante `-obb` se introdujo en la versión v8.1.0 (febrero de 2024). A diferencia de la detección tradicional, cada predicción incluye un ángulo de rotación, lo que permite localizar objetos alineados con su orientación en imágenes aéreas y satelitales. Los pesos `yolov8n-obb.pt` vienen preentrenados sobre el conjunto de datos **DOTAv1** y se usan en este repositorio para análisis territorial de teledetección (Aeropuerto El Dorado, Bahía de Santa Marta e imagen de España).

- **Curated by:** [Ultralytics](https://github.com/ultralytics) (autores originales: Glenn Jocher, Ayush Chaurasia y Jing Qiu)
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [Ultralytics](https://huggingface.co/Ultralytics) (publicado en GitHub y Hugging Face)
- **Language(s) (NLP):** Not applicable — modelo de visión por computador, sin datos textuales
- **License:** [AGPL-3.0](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) (también disponible licencia Enterprise)

### Fuentes del conjunto de datos [opcional] (Dataset Sources [optional])

- **Repository:** https://github.com/ultralytics/ultralytics
- **Paper [optional]:** No existe un paper formal de YOLOv8 (declaración oficial de Ultralytics). Para el conjunto de datos de preentrenamiento: Ding, J. et al. (2018). *DOTA: A Large-scale Dataset for Object Detection in Aerial Images*. CVPR 2018. https://arxiv.org/abs/1711.10145
- **Demo [optional]:** https://docs.ultralytics.com/tasks/obb/ (documentación con ejemplos ejecutables y notebooks de Google Colab)

## Usos (Uses)

### Uso directo (Direct Use)

Detección de objetos con cajas orientadas en imágenes aéreas y satelitales: seguimiento de barcos y vehículos desde satélites o drones, análisis de infraestructura y planificación urbana, monitoreo agrícola e inspección de paneles solares o aerogeneradores. En este repositorio se aplica a imágenes de teledetección territorial con umbral de confianza configurable (`conf=0.25`, `imgsz=1024`).

### Uso fuera de alcance (Out-of-Scope Use)

- Uso como único sistema de decisión en aplicaciones críticas (seguridad vial, militar o médico) sin validación y supervisión humana.
- Uso comercial sin cumplir las obligaciones de la licencia AGPL-3.0 ni contar con la licencia Enterprise de Ultralytics.
- Detección de personas, biometría o identificación individual: el modelo no está entrenado para ello.
- Detección de clases distintas a las 15 clases de DOTAv1 sin un proceso adicional de fine-tuning (ajuste fino).

## Estructura del conjunto (Dataset Structure)

El modelo está entrenado en el formato **DOTAv1**:

- **Imágenes aéreas** de alta resolución (miles de píxeles por lado), divididas en parches de 1024×1024 px para entrenamiento y evaluación.
- **15 clases de objetos:** `plane`, `ship`, `storage tank`, `baseball diamond`, `tennis court`, `basketball court`, `ground track field`, `harbor`, `swimming pool`, `small vehicle`, `large vehicle`, `bridge`, `roundabout`, `soccer ball field`, `helicopter`.
- **Formato de anotación YOLO-OBB:** una línea por objeto con la clase y las 4 esquinas normalizadas: `class_index x1 y1 x2 y2 x3 y3 x4 y4`. Internamente la red procesa las cajas en formato `xywhr` (centro x, y, ancho, alto y ángulo en radianes).

## Creación del conjunto (Dataset Creation)

### Razón de la curación (Curation Rationale)

DOTA es el conjunto de referencia (*benchmark*) para la detección de objetos en imágenes aéreas con cajas orientadas; permite entrenar y comparar modelos de visión aérea de forma estandarizada. Ultralytics preentrenó la familia `-obb` sobre DOTAv1 para ofrecer pesos listos para usar en tareas de teledetección.

### Datos de origen (Source Data)

#### Recolección y procesamiento de datos (Data Collection and Processing)

Imágenes aéreas y satelitales recopiladas de fuentes públicas (principalmente Google Earth y sensores de teledetección aérea), cubriendo escenas urbanas, portuarias, de tránsito y de instalaciones deportivas. Las imágenes se recortaron en parches y se anotaron manualmente con polígonos de 4 puntos.

#### ¿Quiénes son los productores de los datos de origen? (Who are the source data producers?)

El consorcio académico del proyecto DOTA (Gui-Song Xia y colaboradores de Wuhan University y universidades asociadas), con imágenes de origen Google Earth.

### Anotaciones [opcional] (Annotations [optional])

#### Proceso de anotación (Annotation process)

Anotación manual de cajas orientadas de 4 esquinas por imágenes, seguida de revisión por pares dentro del equipo DOTA. Las cajas se canonicalizan al lado largo (ancho ≥ alto) con el ángulo en `[-π/4, 3π/4)`.

#### ¿Quiénes son los anotadores? (Who are the annotators?)

Estudiantes e investigadores del equipo DOTA. [More Information Needed] (Ultralytics no publica el detalle de su proceso de anotación interna).

### Información personal y sensible (Personal and Sensitive Information)

Las imágenes son capturas de teledetección a escala territorial: no contienen datos personales identificables directamente. A las resoluciones utilizadas no se reconocen rostros; aun así, podrían aparecer vehículos o instalaciones sensibles, por lo que los resultados no deben usarse para vigilancia de personas.

## Sesgos, riesgos y limitaciones (Bias, Risks, and Limitations)

- **Sesgo geográfico y de dominio:** DOTAv1 concentra escenas de unas pocas regiones; el rendimiento puede caer en imágenes de otras zonas, sensores o resoluciones (p. ej. ortofotos locales muy distintas a Google Earth).
- **Sesgo de clase:** las clases de vehículo pequeño/son muy frecuentes frente a clases raras (heliductos, puentes), lo que favorece detecciones mayoritarias.
- **Tamaño del modelo:** la variante *nano* es la más rápida pero la menos precisa de la familia; para más precisión existen `yolov8s/m/l/x-obb`.
- **Umbral de confianza:** con `conf=0.25` pueden aparecer falsos positivos (p. ej. embarcaciones pequeñas) o perderse objetos de baja visibilidad.
- **Solo 15 clases:** no detecta edificios genéricos, vegetación ni objetos fuera de DOTAv1.

## Recomendaciones (Recommendations)

Se recomienda advertir a los usuarios los riesgos, sesgos y limitaciones del modelo. Validar los resultados con intérpretes humanos y datos locales antes de usarlos en decisiones territoriales; ajustar `conf` y `imgsz` según la escena; y realizar fine-tuning con un dataset local cuando se necesiten clases o zonas no representadas en DOTAv1.

## Citación [opcional] (Citation [optional])

Esta ficha sigue el formato de ficha de modelo (*model card*) propuesto en *Model Cards for Model Reporting* (Mitchell et al., 2019), a partir de la plantilla oficial de HuggingFace.

### BibTeX:

```bibtex
@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}

@inproceedings{ding2018dota,
  title={DOTA: A Large-scale Dataset for Object Detection in Aerial Images},
  author={Ding, Jian and Xue, Nan and Long, Xiangyu and Wen, Junwen and Xi, Guisong and Xia, Gui-Song},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2018},
  eprint={1711.10145},
  archivePrefix={arXiv}
}

@inproceedings{mitchell2019modelcards,
  title={Model Cards for Model Reporting},
  author={Mitchell, Margaret and Wu, Simone and Zaldivar, Andrew and Barnes, Parker and Vasserman, Lucy and Hutchinson, Ben and Spitzer, Elena and Raji, Inioluwa Deborah and Gebru, Timnit},
  booktitle={Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT*)},
  pages={220--229},
  year={2019},
  url={https://arxiv.org/abs/1810.03993}
}
```

### APA:

Jocher, G., Chaurasia, A., & Qiu, J. (2023). *Ultralytics YOLOv8* (Version 8.0.0) [Software]. https://github.com/ultralytics/ultralytics (licencia AGPL-3.0).

Ding, J., Xue, N., Long, X., Wen, J., Xi, G., & Xia, G.-S. (2018). DOTA: A Large-scale Dataset for Object Detection in Aerial Images. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*. arXiv:1711.10145.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., ... & Gebru, T. (2019, January). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency* (pp. 220-229). Disponible en: https://arxiv.org/abs/1810.03993

## Glosario [opcional] (Glossary [optional])

- **OBB (Oriented Bounding Box):** caja delimitadora rotada que añade un ángulo para ajustarse a la orientación del objeto.
- **DOTA / DOTAv1:** conjunto de datos de referencia para detección en imágenes aéreas.
- **mAP:** media de la precisión promedio (*mean Average Precision*), métrica de calidad de detección.
- **Confianza (conf):** probabilidad mínima que debe tener una detección para mostrarse.
- **Fine-tuning:** reentrenamiento de un modelo preentrenado con datos propios.

## Más información [opcional] (More Information [optional])

- **Plantilla utilizada para esta ficha:** [HuggingFace Hub Templates](https://github.com/huggingface/huggingface_hub/tree/main/src/huggingface_hub/templates) (carpeta `src/huggingface_hub/templates`), de HuggingFace `huggingface_hub`.
- **Formato de ficha de modelo (*model card*):** Mitchell, M. et al. (2019). *Model Cards for Model Reporting*. Disponible en: https://arxiv.org/abs/1810.03993
- Documentación de la tarea OBB: https://docs.ultralytics.com/tasks/obb/
- Documentación de YOLOv8: https://docs.ultralytics.com/models/yolov8/
- Conjunto DOTA: https://captain-whu.github.io/DOTA/
- Repositorio del framework: https://github.com/ultralytics/ultralytics

## Autores de la ficha [opcional] (Dataset Card Authors [optional])

Leonel Andrés Cárdenas Castro

## Contacto de la ficha (Dataset Card Contact)

- Correo: lacardenasc@udistrital.edu.co
- GitHub: @andkastro77-cpu
