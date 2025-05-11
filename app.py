import streamlit as st

st.set_page_config(page_title="AI Learning Tracker", layout="wide")
st.title("📚 AI Learning Tracker")

modules = {
    "1. Введение": [
        ("Установка Python и Jupyter", "https://youtu.be/r-uOLxNrNk8"),
        ("Библиотеки: NumPy, pandas, sklearn", "https://scikit-learn.org/stable/tutorial/basic/tutorial.html")
    ],
    "2. Математика": [
        ("Линейная алгебра (3Blue1Brown)", "https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_Zan3c3A-"),
        ("Статистика и вероятность", "https://www.khanacademy.org/math/statistics-probability")
    ],
    "3. Машинное обучение": [
        ("Классификация и регрессия", "https://developers.google.com/machine-learning/crash-course"),
        ("Кластеризация, метрики", "https://towardsdatascience.com/")
    ],
    "4. Глубокое обучение": [
        ("Нейросеть с нуля (на NumPy)", "https://youtu.be/w8yWXqWQYmU"),
        ("TensorFlow/Keras", "https://keras.io/examples/")
    ],
    "5. NLP": [
        ("Hugging Face NLP курс", "https://huggingface.co/learn/nlp-course"),
        ("Создание чат-бота с Transformers", "https://huggingface.co/docs/transformers/index")
    ],
    "6. Компьютерное зрение": [
        ("OpenCV + PyImageSearch", "https://pyimagesearch.com/start-here/"),
        ("Классификация изображений (TensorFlow)", "https://www.tensorflow.org/tutorials/images/classification")
    ],
    "7. Деплой и UI": [
        ("Streamlit", "https://docs.streamlit.io/"),
        ("ONNX и TensorFlow Lite", "https://www.tensorflow.org/lite/guide")
    ],
    "Финальный проект": [
        ("GitHub проекты", "https://github.com/krzjoa/awesome-ml-projects")
    ]
}

progress = {}
st.sidebar.title("📈 Прогресс")

for module, topics in modules.items():
    with st.expander(module):
        for title, link in topics:
            key = f"{module}:{title}"
            checked = st.checkbox(title, key=key)
            st.markdown(f"[Материал]({link})")
            note = st.text_area(f"Заметка для: {title}", key=f"note-{key}", height=60)
            progress[key] = checked

# Подсчёт прогресса
completed = sum(progress.values())
total = len(progress)
st.sidebar.markdown(f"**Пройдено:** {completed} из {total} ({(completed/total)*100:.1f}%)")
