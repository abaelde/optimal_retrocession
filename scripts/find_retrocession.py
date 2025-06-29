import numpy as np
from scipy.optimize import minimize
from plot_helpers import plot_retrocession_matrix_graph
import pandas as pd
from io import StringIO
import time
import networkx as nx
import matplotlib.pyplot as plt


def print_status(xk):
    print(f"Current parameter vector: {xk}")


# Set random seeds for reproducibility
np.random.seed(42)

# Generate random data for 20 entities with seeds set
num_entities = 20

# Generate entity names
entity_names = [f"Entity_{i+1}" for i in range(num_entities)]

# Generate random capital values between 10 and 100
capital_values = np.random.randint(10, 101, num_entities)

# Generate random loss values between 10 and 30
loss_values = np.random.randint(10, 31, num_entities)

# Generate RC values as capital / random choice of 2 or 3
rc_values = capital_values / np.random.choice([2, 3], num_entities)

# Create a DataFrame
df_generated_seed = pd.DataFrame(
    {
        "entity_name": entity_names,
        "C": capital_values,
        "L": loss_values,
        "RC": rc_values,
    }
)

# Convert the DataFrame to CSV format (for demonstration; in reality, you'd save it to a file)
csv_generated_seed = df_generated_seed.to_csv(index=False)

print(csv_generated_seed)


# Create a sample CSV content
csv_content = """
entity_name,C,L,RC
Entity_1,100,10,50
Entity_2,100,20,50
Entity_3,100,10,50
"""

csv_content = csv_generated_seed

# Simulate reading from a CSV file
df = pd.read_csv(StringIO(csv_content))

# Extract vectors C, L, RC, and entity_name from the DataFrame
C = df["C"].values
L = df["L"].values
RC = df["RC"].values
entity_name = df["entity_name"].values

N = len(df)

"""
C = np.array([100, 100, 100])  # Capital values
L = np.array([10, 20, 10])  # Loss values
RC = np.array([50, 50, 50])  # Risk capital values
"""

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
print("Start Optimization")
t0 = time.time()
res = minimize(objective, R0, constraints=cons)
print(time.time() - t0)

# Reshape the solution to NxN matrix
print("plot results")
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

# plot ------------------------------
print("plot ")
plot_retrocession_matrix_graph(R_optimal)
# plot_sankey(R_optimal, L)
