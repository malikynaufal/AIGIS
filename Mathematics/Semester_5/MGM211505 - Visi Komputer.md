---
title: MGM211505 - Visi Komputer (Computer Vision)
type: course
semester: 5
sks: 3
tags: [mathematics, computer-vision, image-processing, semester-5]
created: 2026-07-27
---

# MGM211505 - Visi Komputer (Computer Vision)

> *"The eye is the window to the soul."* — da Vinci
> **SKS:** 3 | **Semester:** 5 | **Prerequisite:** [[Linear Algebra Fundamentals]], [[Multivariable Calculus]]

## 📋 Syllabus

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Image Formation | Camera model, projection |
| 2 | Image Processing | Filtering, convolution |
| 3 | Feature Detection | Edges, corners, Hessian |
| 4 | Feature Matching | SIFT, ORB, descriptor matching |
| 5 | Geometry | Homography, epipolar geometry |
| 6 | Stereo Vision | Depth from disparity |
| 7 | Structure from Motion | Bundle adjustment |
| 8 | Midterm Review | Comprehensive problem solving |
| 9 | Object Detection | Sliding windows, deep learning |
| 10 | Semantic Segmentation | Pixel-wise classification |
| 11 | 3D Reconstruction | Point clouds, meshing |
| 12 | Photogrammetry | Aerial image processing |
| 13 | LiDAR Processing | Point cloud analysis |
| 14 | Applications | Geodetic surveying, monitoring |
| 15 | Final Review | Integration project |

## 📚 Key Concepts

### Camera Projection Matrix

$$\begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = P \begin{bmatrix} X \\ Y \\ Z \\ 1 \end{bmatrix}, \quad P = K[R|t]$$

where $K$ = intrinsic, $[R|t]$ = extrinsic parameters.

### Fundamental Matrix

$$x'^T F x = 0$$

relates corresponding points in stereo images.

### Bundle Adjustment

$$\min_{K, R_i, t_i, X_j} \sum_{i,j} \|x_{ij} - \pi(K, R_i, t_i, X_j)\|^2$$

Joint optimization of camera parameters and 3D points.

## 📐 Geodesy Application

| Method | Application |
|--------|-------------|
| **Photogrammetry** | Aerial/satellite mapping |
| **Structure from Motion** | Terrain reconstruction |
| **LiDAR Processing** | Point cloud to DEM |
| **Feature Matching** | Change detection, monitoring |

## 🎯 Practice Problems

1. Implement Sobel edge detection and compare with Canny.
2. Compute fundamental matrix from point correspondences.
3. Perform triangulation to reconstruct 3D point from stereo.
4. Implement simple bundle adjustment with Levenberg-Marquardt.
5. Process LiDAR point cloud for DSM generation.

## 📖 References

- Szeliski, R. (2022). *Computer Vision: Algorithms and Applications* (2nd ed.). Springer (free online).
- Hartley, R. & Zisserman, A. (2004). *Multiple View Geometry*. Cambridge.
- Gonzalez, R.C. & Woods, R.E. (2017). *Digital Image Processing*. Pearson.

---
*See also: [[Linear Algebra Fundamentals]], [[Least Squares Adjustment]], [[Numerical Methods]]*
