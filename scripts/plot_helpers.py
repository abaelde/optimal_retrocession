import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_retrocession_matrix_graph(matrix):

    G = nx.DiGraph()

    # Adding nodes and edges based on the matrix
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val != 0 and i != j:
                G.add_edge(i, j, weight=round(val, 2))

    # Create a layout for the nodes
    pos = nx.spring_layout(G)

    # Draw only the nodes using matplotlib's scatter function for custom zorder
    node_positions = np.array([pos[i] for i in G.nodes()])
    plt.scatter(
        node_positions[:, 0],
        node_positions[:, 1],
        s=1000,
        c="lightblue",
        zorder=2,
        marker="o",
    )

    # Add labels with an offset for better visibility
    offset = 0.1  # Positional offset to move the label outside the node circle
    for node, (x, y) in pos.items():
        plt.text(
            x + offset,
            y + offset,
            str(node),
            fontsize=18,
            ha="center",
            va="center",
            zorder=3,
        )

    # Manually draw edges and add labels
    for (i, j, d) in G.edges(data=True):
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        dx = x1 - x0
        dy = y1 - y0
        dist = np.sqrt(dx * dx + dy * dy)

        # add curvature if the pair has another edge in reversed direction
        if (j, i) in G.edges():
            curvature = 0.6
        else:
            curvature = 0

        # Generate Bezier curve
        x_bezier = np.linspace(x0, x1, 100)
        y_bezier = np.linspace(y0, y1, 100)
        control_x = x0 + dx / 2 + curvature * dy / dist
        control_y = y0 + dy / 2 - curvature * dx / dist
        x_curve = (
            (1 - ((x_bezier - x0) / dx)) * x0
            + ((x_bezier - x0) / dx) * x1
            + ((x_bezier - x0) / dx) * (1 - ((x_bezier - x0) / dx)) * (control_x - x0)
        )
        y_curve = (
            (1 - ((y_bezier - y0) / dy)) * y0
            + ((y_bezier - y0) / dy) * y1
            + ((y_bezier - y0) / dy) * (1 - ((y_bezier - y0) / dy)) * (control_y - y0)
        )

        plt.plot(x_curve, y_curve, "k", zorder=1)

        # Add an arrowhead near the end of the curve
        arrow_index = -10  # index of the point on the curve where the arrowhead starts
        arrow_x = x_curve[arrow_index]
        arrow_y = y_curve[arrow_index]
        arrow_dx = x_curve[-1] - arrow_x
        arrow_dy = y_curve[-1] - arrow_y
        plt.arrow(
            arrow_x,
            arrow_y,
            arrow_dx,
            arrow_dy,
            shape="full",
            lw=0,
            length_includes_head=True,
            head_width=0.08,
            zorder=4,  # Setting zorder to 4 to ensure it's above the node circles
        )

        # Add edge label
        x_label = x0 + dx / 2 + 0.1 * dy / dist
        y_label = y0 + dy / 2 - 0.1 * dx / dist
        plt.text(
            x_label,
            y_label,
            str(d["weight"]),
            fontsize=12,
            ha="center",
            va="center",
            zorder=5,
        )

    plt.show()


def plot_sankey(R, L):
    labels = [f"Entity {i+1}" for i in range(N)] * 2
    source = []
    target = []
    value = []

    for i in range(N):
        for j in range(N):
            source.append(i)
            target.append(j + N)  # Shifted by N to represent the target entities
            value.append(R[i][j] * L[i] + 0.001)

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                ),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )

    fig.update_layout(
        title_text="Distribution of Losses between Entities", font_size=10
    )
    fig.show()
