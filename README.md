# 🚀 Proyecto Sign Language Translator (LSE)

## Visión general

<img src="https://fundacionmusicforall.org/wp-content/uploads/2025/05/lengua-signos-espanola.png" alt="Lengua de Signos Española" width="50%" />

## 📜 Briefing: PROYECTO COMPUTER VISION

### 🔍 Planteamiento  

Una empresa de publicidad quiere comprobar cuánto tiempo aparecen los logos de las
marcas que representan en pantalla para evaluar dónde dirigir sus esfuerzos.
Para ello quieren que sus dos mejores expertos en IA creen un modelo de detección de
marcas en vídeos, para ello deberéis entrenar un modelo, a partir de imágenes obtenidas
por los expertos en IA, el objetivo es analizar un vídeo y decidir si se ha detectado la nueva
categoría (marca), y si se ha hecho dar un informe de cuanto tiempo aparece la nueva
categoría en el vídeo, también dar un porcentaje del tiempo en que aparece. Guardar las
detecciones en una base de datos.
El procesado no es necesario que sea en tiempo real, el objetivo es analizar vídeos y
presentar un informe.
Como de momento solo es una prueba de concepto os permiten elegir los logos de las
marcas que queráis utilizar, con la idea de ir ampliando la lista en el futuro.

---

## 🎯 Objetivos del Proyecto  

* **Familiarizarse con el procesado de Imágenes**  
* **Utilizar un modelo de Vision por computador para deteccion de objetos**  
   

---

## 📦 Condiciones de Entrega  

Para la fecha de entrega, los equipos deberán presentar:  

✅ **Repositorio en GitHub** con el código fuente documentado.

✅ **Demo en vivo** mostrando el funcionamiento del modelo.

✅ **Presentación técnica**, explicando los objetivos, desarrollo y tecnologías utilizadas.

✅ **Tablero Kanban** con la gestión del proyecto (Trello, Jira, etc.).  

---

## ⚙️ Tecnologías Recomendadas  

- **Control de versiones:** Git / GitHub  
- **Entorno de ejecución:** Docker  
- **Lenguaje principal:** Python  
- **Librerías útiles:** OpenCV, Pytorch/Torchvision, scikit-image, pillow, TensorFlow/Keras, PyTorch
- ** Modelos de vison:** YOLO, Faster R-CNN, SSD, Detectron2
- **front end:** Streamlit, Gradio 
- **Gestión del proyecto:** Trello, Jira, Github  

---

## 🏆 Niveles de Entrega  

### 🟢 **Nivel Esencial:**  
✅ Entrenar un modelo que detecte una nueva categoría y la localice dentro de un bounding box visible. En este nivel la detección puede ser en una sola imagen.

✅ El modelo debe reconocer al menos una marca

✅ Repositorio Git con ramas bien organizadas y commits limpios y descriptivos.

✅ Documentación del código y un README en GitHub.  

### 🟡 **Nivel Medio:**  
✅ El modelo deberá funcionar con archivos de video.

✅ Deberá incluirse debajo de cada detección el nombre de la nueva clase detectada.

### 🟠 **Nivel Avanzado:**  
✅ Añadir porcentaje de seguridad en el reconocimiento de forma que sea visible en la pantalla junto al nombre del objeto reconocido.

✅ Guardar los datos de detección en una base de datos, junto con el nombre del video al que pertenecen, las imágenes recortadas de los bounding boxes, así como cualquier otra información que creáis relevante.

✅ Crear un modelo multimarca que sea capaz de reconocer más de una marca y guardar datos relativos a todas las marcas que sea capaz de detectar. 

### 🔴 **Nivel Experto:**  
✅ Crear un front para poder subir los vídeos de forma sencilla y visualizar los resultados en una aplicación web.

✅ Servir el modelo en cloud y apificarlo para poder acceder al modelo desde cualquier cliente.

---

## 📊 Evaluación  

Se considerarán los siguientes criterios:  

✅ Uso de técnicas de preprocesamiento de imágenes: resizing, normalización, escalado  
✅ Uso de Datasets de Imágenes para detección de objetos   
✅ Implementa detección de objetos reentrenando modelo preentrenado    
✅ Uso de técnicas de detección de objetos en tiempo real  
✅ Aumento de datos con técnicas visuales (flip, crop, color jitter)    

Más detalles en: [roadmap-mad-ai-p4.coderf5.es](https://roadmap-mad-ai-p4.coderf5.es/)  


