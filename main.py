import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import figures as fig


N = 60


def conway(count):
    if (count < 2) or (count > 3):
        return 1
    elif count == 3:
        return -1

    return 0


def animationn(i):
  global grid
  newGrid = grid.copy()

  for i in range(N):
    for j in range(N):
      nen = grid[i, (j-1)%N] + grid[i, (j+1)%N] + \
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +\
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +\
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]

      c = conway(nen)
      if grid[i, j] == 1 and c == 1:
          newGrid[i][j] = 0
      elif c == -1:
          newGrid[i][j] = 1

  mat.set_data(newGrid)
  grid = newGrid
  return mat,


if __name__ == '__main__':

    grid = np.random.choice([0], N * N).reshape(N, N)

    fig.pulsar(grid, 10, 10)
    fig.pulsar(grid, 40, 40)

    plt.style.use('grayscale')
    fig, ax = plt.subplots()
    fig.suptitle('Conway\'s Game of Life', fontsize=14)
    ax.plot()
    mat = ax.matshow(grid)
    ani = animation.FuncAnimation(fig, animationn, interval=50)

    # ani.save("animation.gif")
    plt.show()