import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# 1. Define 'Anchor' points (The "Nails" the curve must touch)
# Leading edge is (0,0), Trailing edge is (1,0)
top_anchors = np.array([[0.0, 0.0], [0.2, 0.1], [0.6, 0.08], [1.0, 0.0]])
bottom_anchors = np.array([[0.0, 0.0], [0.3, -0.05], [0.7, -0.03], [1.0, 0.0]])

# 2. Generate 100 smooth points between those anchors
x_fine = np.linspace(0, 1, 100)

# 3. Create the Splines (The math that makes it "fluid")
# bc_type='natural' ensures the ends don't have weird kinks
top_curve = CubicSpline(top_anchors[:, 0], top_anchors[:, 1], bc_type='natural')
bottom_curve = CubicSpline(bottom_anchors[:, 0], bottom_anchors[:, 1], bc_type='natural')

# 4. Plotting it so you can see your design
plt.figure(figsize=(10, 4))
plt.plot(top_anchors[:, 0], top_anchors[:, 1], 'ro', label='Top Anchors') # Red dots
plt.plot(x_fine, top_curve(x_fine), 'b-', label='Fluid Top')           # Blue line
plt.plot(bottom_anchors[:, 0], bottom_anchors[:, 1], 'go', label='Bottom Anchors') 
plt.plot(x_fine, bottom_curve(x_fine), 'g-', label='Fluid Bottom')

plt.ylim(-0.2, 0.2) # Zoom in so it's not squashed
plt.legend()
plt.title("Your First Generative Wing Profile")
plt.show()