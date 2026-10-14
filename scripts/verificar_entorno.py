"""Verifica que el entorno tenga GPU disponible (Google Colab o local).

Uso:
    python scripts/verificar_entorno.py
"""

import torch

print(f"¿GPU disponible?: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"Dispositivo activo: {torch.cuda.get_device_name(0)}")
else:
    print("⚠️ No se detectó GPU. La inferencia se ejecutará en CPU (más lenta).")
    print("   En Google Colab: Runtime > Change runtime type > GPU")
