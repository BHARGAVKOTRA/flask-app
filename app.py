from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Bhargav's Platform</title>
        <style>
            body {
                font-family: sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                text-align: center;
                padding: 60px;
                background: #1e293b;
                border-radius: 16px;
                border: 1px solid #334155;
            }
            h1 { font-size: 2.5rem; color: #38bdf8; margin-bottom: 10px; }
            p { color: #94a3b8; font-size: 1.1rem; }
            .badge {
                display: inline-block;
                background: #0ea5e9;
                color: white;
                padding: 6px 16px;
                border-radius: 999px;
                font-size: 0.85rem;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello from Kubernetes!</h1>
            <p>Deployed by Bhargav Kotra</p>
            <p>Flask + Docker + Prometheus + Grafana</p>
            <span class="badge">v3.0 — With Monitoring</span>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok', 'version': '3.0'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
