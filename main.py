from utils import *

grid_size = 1000
side_length = 25

grid_obj = Grid(grid_size, side_length)
grid_obj.generate_grid()
grid_obj.generate_points()


for val in np.arange(1, 10, 0.5):
    matrix = np.array([[val, 0],
                       [0, 1]])

    _, new_pts = transform(grid_obj, matrix)
    grid = grid_obj.plot(new_pts)
    cv2.imshow("Grid", grid)
    if cv2.waitKey(250) == 27:
        break

cv2.destroyAllWindows()