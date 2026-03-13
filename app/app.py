import os
from collections import deque

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

from metrics import get_system_metrics

# Initialisation de l'application Dash
app = Dash(__name__)
server = app.server

# Historique des métriques
MAX_POINTS = 20
cpu_history = deque(maxlen=MAX_POINTS)
memory_history = deque(maxlen=MAX_POINTS)
disk_history = deque(maxlen=MAX_POINTS)
time_history = deque(maxlen=MAX_POINTS)

# Layout de l'application
app.layout = html.Div(className="main-container", children=[
    html.Div(className="header", children=[
        html.H1("System Monitoring Dashboard"),
        html.P("Dashboard DevOps de supervision système avec Python Dash")
    ]),

    dcc.Interval(
        id="interval-component",
        interval=3 * 1000,  # mise à jour toutes les 3 secondes
        n_intervals=0
    ),

    html.Div(className="cards-container", children=[
        html.Div(className="card", children=[
            html.H3("CPU Usage"),
            html.H2(id="cpu-value")
        ]),
        html.Div(className="card", children=[
            html.H3("Memory Usage"),
            html.H2(id="memory-value")
        ]),
        html.Div(className="card", children=[
            html.H3("Disk Usage"),
            html.H2(id="disk-value")
        ]),
        html.Div(className="card", children=[
            html.H3("CPU Cores"),
            html.H2(id="cores-value")
        ])
    ]),

    html.Div(className="system-info", children=[
        html.H2("System Information"),
        html.Div(className="info-grid", children=[
            html.Div([
                html.Strong("Hostname: "),
                html.Span(id="hostname-value")
            ]),
            html.Div([
                html.Strong("Operating System: "),
                html.Span(id="os-value")
            ]),
            html.Div([
                html.Strong("Current Time: "),
                html.Span(id="time-value")
            ]),
            html.Div([
                html.Strong("Uptime: "),
                html.Span(id="uptime-value")
            ]),
            html.Div([
                html.Strong("Global Status: "),
                html.Span(id="status-value")
            ]),
        ])
    ]),

    html.Div(className="graphs-container", children=[
        html.Div(className="graph-box", children=[
            dcc.Graph(id="cpu-graph")
        ]),
        html.Div(className="graph-box", children=[
            dcc.Graph(id="memory-graph")
        ]),
        html.Div(className="graph-box", children=[
            dcc.Graph(id="disk-graph")
        ])
    ])
])


def get_status(cpu, memory, disk):
    if cpu > 85 or memory > 85 or disk > 90:
        return "Critical"
    if cpu > 60 or memory > 60 or disk > 75:
        return "Warning"
    return "Normal"


@app.callback(
    [
        Output("cpu-value", "children"),
        Output("memory-value", "children"),
        Output("disk-value", "children"),
        Output("cores-value", "children"),
        Output("hostname-value", "children"),
        Output("os-value", "children"),
        Output("time-value", "children"),
        Output("uptime-value", "children"),
        Output("status-value", "children"),
        Output("cpu-graph", "figure"),
        Output("memory-graph", "figure"),
        Output("disk-graph", "figure"),
    ],
    [Input("interval-component", "n_intervals")]
)
def update_dashboard(n):
    metrics = get_system_metrics()

    cpu = metrics["cpu_percent"]
    memory = metrics["memory_percent"]
    disk = metrics["disk_percent"]
    current_time = metrics["current_time"]

    cpu_history.append(cpu)
    memory_history.append(memory)
    disk_history.append(disk)
    time_history.append(current_time)

    status = get_status(cpu, memory, disk)

    # Graphique CPU
    cpu_figure = go.Figure()
    cpu_figure.add_trace(go.Scatter(
        x=list(time_history),
        y=list(cpu_history),
        mode="lines+markers",
        name="CPU",
        line=dict(width=3, color="#38bdf8"),
        marker=dict(size=7)
    ))
    cpu_figure.update_layout(
        title="CPU Usage Over Time",
        xaxis_title="Time",
        yaxis_title="CPU %",
        yaxis_range=[0, 100],
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.65)",
        font=dict(color="#f8fafc"),
        margin=dict(l=40, r=20, t=50, b=40)
    )

    # Graphique RAM
    memory_figure = go.Figure()
    memory_figure.add_trace(go.Scatter(
        x=list(time_history),
        y=list(memory_history),
        mode="lines+markers",
        name="Memory",
        line=dict(width=3, color="#818cf8"),
        marker=dict(size=7)
    ))
    memory_figure.update_layout(
        title="Memory Usage Over Time",
        xaxis_title="Time",
        yaxis_title="Memory %",
        yaxis_range=[0, 100],
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.65)",
        font=dict(color="#f8fafc"),
        margin=dict(l=40, r=20, t=50, b=40)
    )

    # Graphique Disque
    disk_figure = go.Figure()
    disk_figure.add_trace(go.Scatter(
        x=list(time_history),
        y=list(disk_history),
        mode="lines+markers",
        name="Disk",
        line=dict(width=3, color="#22d3ee"),
        marker=dict(size=7)
    ))
    disk_figure.update_layout(
        title="Disk Usage Over Time",
        xaxis_title="Time",
        yaxis_title="Disk %",
        yaxis_range=[0, 100],
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.65)",
        font=dict(color="#f8fafc"),
        margin=dict(l=40, r=20, t=50, b=40)
    )

    return (
        f"{cpu}%",
        f"{memory}%",
        f"{disk}%",
        str(metrics["cpu_cores"]),
        metrics["hostname"],
        metrics["os"],
        metrics["current_time"],
        metrics["uptime"],
        status,
        cpu_figure,
        memory_figure,
        disk_figure
    )


if __name__ == "__main__":
    host = os.getenv("DASH_HOST", "127.0.0.1")
    port = int(os.getenv("DASH_PORT", "8050"))
    app.run(debug=True, host=host, port=port)