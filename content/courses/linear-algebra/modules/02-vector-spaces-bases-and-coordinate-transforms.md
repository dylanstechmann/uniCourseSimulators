# Vector spaces, bases, and coordinate transforms

A basis is a linearly independent set that spans a vector space. Coordinates depend on that basis, while the underlying vector does not. Change-of-basis matrices convert coordinates between descriptions. In robotics, rotation matrices represent the same physical vector in different frames and must be orthogonal with determinant +1 for a proper rotation. A basis with poor scaling can make numerical estimates unstable even when mathematically valid.
