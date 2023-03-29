# This file is what was used to create the plot for Q1.
# You should not need to edit or run it.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import hinge_loss, log_loss, mean_squared_error
from plotting import plot_data, plot_decision_surface

# np.random.seed(1)

X = np.array([
  [1, 2], [4, 3], [10, 3],
  [2, 1], [2, 3],
], dtype=np.float64)

y = np.array([
  1, 1, 1,
  -1, -1,
])


fig, axis = plt.subplots()
plot_data(X, y, ax=axis)
for i in range(X.shape[0]):
    point = tuple(X[i, :].astype(int).tolist())
    label = f" ({point[0]:d}, {point[1]:d})"
    axis.annotate(label, xy=point, textcoords="data")

model = LogisticRegression()
model.fit(X, y)
model.coef_ = np.array([[0.9, -1.3]])
model.intercept_ = np.array([1])

preds = model.intercept_ + X @ model.coef_.T

limits = np.array(axis.axis()) + np.array([-1, 1, -1, 1])
plot_decision_surface(
    model.predict,
    axis_limits=limits,
    ax=axis
)

# Starting from x=2.1, draw normal line w
# (1, 0.9, -1.3) * (1, 3, y) = 0
# (1 + 2.7 / 1.3) = y

x_start = 2.1
y_start = (1 + x_start * 0.9) / 1.3

axis.quiver(
    np.array([x_start]),
    np.array([y_start]),
    np.array([1.3]),
    np.array([-0.9]),
    scale=2,
    scale_units="xy",
)
point = (x_start, y_start)
label = "   w = <1, 0.9, -1.3>"
axis.annotate(label, xy=point, textcoords="data")

plt.tight_layout()
plt.show()
