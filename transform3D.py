import numpy as np


class Transform3D:

    def __init__(self, number_of_points):
        self.number_of_points = number_of_points
        self.dimension = 3

    def compute_rigid_transform(self, source_points, target_points):
        # Input: both source_points and target_points are Nx3 matrix of points
        # Returns R,translation
        # R = 3x3 rotation matrix
        # translation = 3x1 column vector
        assert self.number_of_points == source_points.shape[0]  # total points
        assert self.dimension == source_points.shape[1]
        assert len(source_points) == len(target_points)

        mean_source_points = np.mean(source_points, axis=0)
        mean_target_points = np.mean(target_points, axis=0)
        # centre the points
        centered_source_points = source_points - np.tile(mean_source_points, (self.number_of_points, 1))
        centered_target_points = target_points - np.tile(mean_target_points, (self.number_of_points, 1))

        H = np.dot(np.transpose(centered_target_points), centered_source_points)/self.number_of_points
        U, D, V = np.linalg.svd(H, full_matrices=True, compute_uv=True)
        V = V.T.copy()
        r = np.ndim(H)
        d = np.linalg.det(H)
        S = np.eye(self.dimension)
        if r > self.dimension - 1:
            if np.linalg.det(H) < 0:
                S[self.dimension, self.dimension] = -1
            elif r == self.dimension - 1:
                if np.linalg.det(U) * np.linalg.det(V) < 0:
                    S[self.dimension, self.dimension] = -1
            else:
                rotation = np.eye(2)
                translation = np.zeros(2)
                return rotation, translation

        rotation = np.dot(np.dot(U, S), V.T)
        translation = (mean_target_points.T - np.dot(rotation, mean_source_points.T)).reshape((3,1))
        return rotation, translation
