import numpy as np
from scipy.optimize import minimize
import holoviews as hv
from holoviews import opts, dim

hv.extension("bokeh")

# Sample data for N entities
N = 3
C = np.array([100, 100, 70])  # Capital values
L = np.array([10, 10, 15])  # Loss values
RC = np.array([50, 50, 50])  # Risk capital values

SR = C / RC
print("Initial SR:", ", ".join(["{:.2f}".format(val) for val in SR]))


# Objective function
def objective(R):
    R = R.reshape(N, N)
    SR_prime = C / RC - np.dot(R, L) / RC
    return sum([np.abs(SR_prime[i] - SR_prime[i + 1]) for i in range(N - 1)])


# Constraints
cons = []

# Each row in R should sum to 1
for j in range(N):
    cons.append(
        {"type": "eq", "fun": lambda R, j=j: 1 - sum([R[i * N + j] for i in range(N)])}
    )

# R values should be between 0 and 1
for i in range(N):
    for j in range(N):
        cons.append({"type": "ineq", "fun": lambda R, i=i, j=j: R[i * N + j]})
        cons.append({"type": "ineq", "fun": lambda R, i=i, j=j: 1 - R[i * N + j]})

# Initial guess: NxN matrix with equal probabilities
R0 = np.ones(N * N) / N

# Solve
res = minimize(objective, R0, constraints=cons)

# Reshape the solution to NxN matrix
R_optimal = res.x.reshape(N, N)
print("\nRetrocession matrix")
print("\nOptimal R matrix:")
for row in R_optimal:
    print(", ".join(["{:.2f}".format(val) for val in row]))

print("\nLosses after distribution")
print(
    "R_optimal multiplied by L:",
    ", ".join(["{:.2f}".format(val) for val in np.dot(R_optimal, L)]),
)

# Compute new capital after losses
C_prime = C - np.dot(R_optimal, L)

# Compute SR' after optimization
SR_prime = C_prime / RC
print(
    "\nSR' after optimization:", ", ".join(["{:.2f}".format(val) for val in SR_prime])
)


# Convert the retrocession matrix to SR change matrix
SR_changes = np.dot(R_optimal, L) / RC


import plotly.graph_objects as go
import plotly.express as px
import numpy as np


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


plot_sankey(R_optimal, L)
