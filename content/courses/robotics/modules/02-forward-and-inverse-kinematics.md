# Forward and inverse kinematics

Forward kinematics maps joint coordinates to end-effector pose. For a planar two-link arm, x=L₁cosθ₁+L₂cos(θ₁+θ₂), y=L₁sinθ₁+L₂sin(θ₁+θ₂). Inverse kinematics solves for joint values that reach a desired pose; multiple solutions or no solution may exist under joint and workspace constraints. The Jacobian maps joint velocity to end-effector velocity and loses rank at singular configurations.
