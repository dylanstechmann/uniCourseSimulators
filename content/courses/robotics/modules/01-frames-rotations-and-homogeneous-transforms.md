# Frames, rotations, and homogeneous transforms

A rigid transform combines rotation and translation. Homogeneous coordinates represent both as a 3×3 matrix in 2D or 4×4 in 3D, with frame conventions stated explicitly. Matrix multiplication is not commutative: transforming a point from tool to world is not interchangeable with world to tool. Rotation matrices should satisfy RᵀR=I and det(R)=+1. A frame diagram often catches errors before a numerical result does.
