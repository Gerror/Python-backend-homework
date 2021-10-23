# PythonBackendHomework
Конфиг nginx, отдающего статику из папки public/ и проксирующего запросы
с префиксом /api/ на gunicorn. Сам gunicorn отдает json вида
{"time": "текущее время", "url": "текущий url"} 