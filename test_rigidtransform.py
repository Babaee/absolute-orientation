import numpy as np
from scipy.stats import special_ortho_group
from transform3D import Transform3D
import unittest


class TestTransform (unittest.TestCase):

    def test_rigid_transformation(self):
        # create a random 3D rotation matrix
        rotation_matrix = special_ortho_group.rvs(3)
        translation_vector = np.mat(np.random.rand(3, 1))

        # number of points
        number_of_points = 10

        source_points = np.mat(np.random.rand(number_of_points, 3))
        target_points = rotation_matrix * source_points.T + np.tile(translation_vector, (1, number_of_points))
        target_points = target_points.T

        # recover the transformation
        dummy_transform = Transform3D(number_of_points)

        rotation_matrix_est, translation_vector_est = dummy_transform.compute_rigid_transform(source_points,
                                                                                              target_points)
        transformed_source_points = (rotation_matrix_est * source_points.T) + np.tile(translation_vector_est,
                                                                                      (1, number_of_points))
        transformed_source_points = transformed_source_points.T
        # Find the error
        err = transformed_source_points - target_points
        err = np.multiply(err, err)
        err = np.matrix.sum(err)
        self.assertAlmostEqual(err, 0)


if __name__ == '__main__':
    unittest.main()



