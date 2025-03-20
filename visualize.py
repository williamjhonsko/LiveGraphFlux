
#### **visualize.py**
```python
import matplotlib.pyplot as plt
import random
import time

plt.ion()
fig, ax = plt.subplots()
x_data, y_data = [], []

for i in range(50):
    x_data.append(i)
    y_data.append(random.randint(1, 100))
    ax.clear()
    ax.plot(x_data, y_data, marker='o', linestyle='-')
    plt.pause(0.1)

plt.ioff()
plt.show()
