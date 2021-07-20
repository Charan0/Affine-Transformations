import cv2
import numpy as np


class Grid:
    def __init__(self, grid_size: int, side_length: int):
        self.grid_size = grid_size
        self.side_length = side_length
        self.points = None
        self.transformed_points = None
        self.grid = None

    def generate_grid(self):
        grid = np.zeros((self.grid_size, self.grid_size, 3))
        cv2.line(grid, (self.grid_size // 2, 0), (self.grid_size // 2, self.grid_size), [255, 255, 255], 2)
        cv2.line(grid, (0, self.grid_size // 2), (self.grid_size, self.grid_size // 2), [255, 255, 255], 2)
        self.grid = grid
        return grid

    def generate_points(self):
        points = np.array([[-self.side_length // 2, self.side_length // 2],
                           [self.side_length // 2, self.side_length // 2],
                           [self.side_length // 2, -self.side_length // 2],
                           [-self.side_length // 2, -self.side_length // 2]])
        self.points = points
        plot_points = points + self.grid_size // 2
        self.transformed_points = plot_points
        return points, plot_points

    def plot(self, transformed_points: np.ndarray = None):
        if transformed_points is None:
            transformed_points = self.transformed_points
        if self.transformed_points is None:
            print("Cannot run this method without initializing the points and the grid")
            return
        dst = self.grid.copy()
        for point in transformed_points:
            cv2.circle(dst, tuple(point), 5, [0, 255, 0], cv2.FILLED)

        for idx in range(4):
            cv2.line(dst, tuple(transformed_points[idx]),
                     tuple(transformed_points[(idx + 1) % 4]), 255, 2)

        return dst


def transform(data: Grid, matrix: np.ndarray, offset_vec: np.ndarray = None):
    grid_size = data.grid_size
    points = data.points

    # Need integer points, cannot plot floats
    if offset_vec is not None:
        transformed_points = np.floor(np.dot(points, matrix) + offset_vec).astype("int")
    else:
        transformed_points = np.floor(np.dot(points, matrix)).astype("int")
    plot_transformed = transformed_points + grid_size // 2

    return transformed_points, plot_transformed
