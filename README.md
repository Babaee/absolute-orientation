# Absolute Orientation in Python

## Overview

This project implements the absolute orientation algorithm in Python for rigid transformation of two sets of 3D points using the Umeyama method. The main class provided is `Transform3D`, which facilitates the transformation process.

## Introduction

The `Transform3D` class provides functionality for rigid transformation of two sets of 3D points. It implements the Umeyama method to estimate the rotation matrix and translation vector that define the linear map from source points to target points.

### Inputs

- `source_points`: A matrix of shape `(n, 3)` where `n` is the number of points. Each row represents a point in 3D space from the source set.
- `target_points`: A matrix of shape `(n, 3)` where `n` is the number of points. Each row represents a point in 3D space from the target set that corresponds to the points in the source set.

### Outputs

The outputs of the `Transform3D` class are:
- `R`: Rotation matrix of shape `(3, 3)`
- `t`: Translation vector of shape `(3,)`

These parameters define the transformation from source points to target points.

## Usage

To use the `Transform3D` class for rigid transformation of 3D points, follow these steps:

1. Create an instance of the `Transform3D` class.
2. Call the `compute_rigid_transform` method with the source and target points.
3. Access the rotation matrix `R` and translation vector `t` from the returned values.

Example usage:

```python
from transform3d import Transform3D

# Example source and target points
source_points = [[0, 0, 0], [1, 0, 0], [0, 1, 0]]
target_points = [[1, 1, 1], [2, 1, 1], [1, 2, 1]]

# Create an instance of Transform3D
transformer = Transform3D()

# Compute rigid transformation
R, t = transformer.compute_rigid_transform(source_points, target_points)

print("Rotation Matrix (R):\n", R)
print("Translation Vector (t):", t)
