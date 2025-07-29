
# Simulación del Precio del Oro con Google Trends

Este proyecto realiza una simulación de Monte Carlo del precio del oro, donde el **drift dinámico** está ajustado en función del interés público medido por **Google Trends**.

## Archivos incluidos

- `simulacion_oro_googletrends.py`: script Python que simula trayectorias del precio del oro con un modelo de Caminata Aleatoria Geométrica (GBM) ajustado por minería de datos.
- `README.md`: instrucciones de uso.

## Requisitos

```bash
pip install numpy pandas matplotlib statsmodels
```

## Cómo usar

1. Ejecutá el script en Google Colab, Replit, o un entorno Python local.
2. El gráfico mostrará 10 trayectorias simuladas del precio del oro.
3. El drift cambia dinámicamente según el nivel de interés en Google Trends (simulado entre 20–100).

## Notas

- Este modelo **no predice** el futuro, pero permite visualizar cómo el "sentimiento" (Google Trends) puede influir en la tendencia esperada del precio.
- Ideal para usar como base en plataformas tipo Lovable o conectar con datasets reales.

---
Desarrollado para ejecución ligera en dispositivos móviles con acceso a GitHub.
