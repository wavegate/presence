web: flask db upgrade; flask translate compile; gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 match:app --timeout 600