# 📊 Aplicativo Web de Prorrateo - Clockify

Este es un aplicativo web desplegado en Azure, diseñado para generar el **prorrateo de horas registradas** por los colaboradores en [Clockify](https://clockify.me/).

Con una interfaz sencilla, permite al usuario ingresar una **fecha de inicio** y una **fecha de fin**, generando un **reporte automático** que se descarga directamente en el navegador.

> ⚠️ **Nota importante:** El aplicativo solo funciona dentro de la red local de la oficina.

---

## 🚀 Cómo usar

1. Conéctate a la red interna de la oficina.
2. Accede al aplicativo web desde tu navegador.
3. Ingresa la **fecha de inicio** y **fecha de fin**.
4. Haz clic en **Generar Reporte**.
5. El archivo será descargado automáticamente.

---

## 🛠️ Tecnologías utilizadas

- 🌐 Azure Web App
- 🧠 Backend: Flask
- 🎨 Frontend: HTML/CSS/JS
- 🔄 Integración con Clockify API 

---

## 🧭 Accesibilidad y restricciones

- ✅ Disponible **únicamente** desde la red interna de la oficina.
- ❌ No accesible desde internet o redes externas.

---

## 🔄 CI/CD Integrado

Este proyecto cuenta con un flujo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** utilizando **GitHub Actions**. Cada cambio en la rama `main` activa automáticamente el proceso de:

1. Validación y pruebas del código fuente.
2. Construcción del paquete/webapp.
3. Despliegue automático al entorno productivo en **Azure Web App**.

> ✅ Esto garantiza que el aplicativo esté siempre actualizado con la última versión funcional.

---
