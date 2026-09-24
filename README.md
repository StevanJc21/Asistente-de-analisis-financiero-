# 📈 Automatización de Análisis Bursátil y Envío de Reportes por Email

Script en Python (Jupyter Notebook) que descarga datos históricos de acciones desde Yahoo Finance, realiza un análisis estadístico básico y envía automáticamente un correo con los resultados usando automatización de interfaz gráfica.

---

## 📋 Descripción

Este proyecto automatiza el flujo completo de un análisis financiero básico:

1. **Descarga** los precios de cierre de una acción en los últimos 6 meses usando `yfinance`.
2. **Visualiza** la evolución del precio con `matplotlib`.
3. **Calcula** métricas clave: precio máximo, mínimo y promedio.
4. **Envía** un correo electrónico con el resumen de los resultados mediante automatización con `pyautogui` y `pyperclip` (controlando Gmail en el navegador).

---

## 🛠️ Tecnologías y Librerías

| Librería | Uso |
|----------|-----|
| `yfinance` | Obtención de datos bursátiles desde Yahoo Finance |
| `matplotlib` | Generación de gráficas |
| `pandas` | Manejo de series temporales (dependencia de yfinance) |
| `pyautogui` | Automatización de mouse y teclado |
| `pyperclip` | Copiado/pegado al portapapeles |
| `webbrowser` | Apertura del navegador |
| `time` | Control de tiempos de espera |

---

## 📦 Instalación

Instala las dependencias necesarias con:

```bash
pip install yfinance matplotlib pyautogui pyperclip
