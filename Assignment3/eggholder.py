import numpy as np
import matplotlib.pyplot as plt

### The Eggholder Function ###
def eggholder_function(x, y):
    return -(y + 47) * np.sin(np.sqrt(abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(abs(x - (y + 47))))

### Implementation of Deterministic Hill Climbing Search ###
def hill_climbing_search():
    # initialize x and y randomly between 0 and 1
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    # calculate the initial value of the Eggholder function
    current_min = eggholder_function(x, y)

    for _ in range(100):
        # generate new x and y by adding a random value between -0.5 and 0.5 to the previous x and y, 
        # limit the maximum step size to 1
        x_new = np.clip((np.random.rand() - 0.5) * 1.0 + x, 0, 1)
        y_new = np.clip((np.random.rand() - 0.5) * 1.0 + y, 0, 1)
        # calculate the new minima of the Eggholder function
        new_min = eggholder_function(x_new, y_new)

        # if the new local minima is lower than the current minimum value, update the values
        if new_min < current_min:
            x, y, current_min = x_new, y_new, new_min
        else:
            break
    # return the final x, y, and the minimum value
    return x, y, current_min


def main():
    minima = []
    positions = []

    for i in range(100):  # 100 runs
        x, y, minimum = hill_climbing_search()
        minima.append(minimum)
        positions.append((x, y))
        # output all 100 minima and positions
        #print(f"Run {i + 1}: minimum at x = {x}, y = {y}, value = {minimum}")

    # find the best minima and its corresponding position
    best_minima_index = np.argmin(minima)
    best_minima = minima[best_minima_index]
    best_position = positions[best_minima_index]
    print(f"\nBest minima found: x = {best_position[0]}, y = {best_position[1]}, value = {best_minima}")

    # 3D colored scatterplot of the 100 Minima
    fig = plt.figure(figsize=(8, 5))
    positions = np.array(positions)
    ax2 = fig.add_subplot(projection='3d')
    scatter = ax2.scatter(positions[:, 0], positions[:, 1], minima, c=minima, cmap='viridis')
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.set_zlabel("Minima")
    ax2.set_title("3D Scatter Plot of 100 Minima")

    plt.show()

if __name__ == "__main__":
    main()
