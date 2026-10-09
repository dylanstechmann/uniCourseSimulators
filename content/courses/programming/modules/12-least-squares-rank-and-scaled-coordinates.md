# Least squares, rank and scaled coordinates

**Status:** original formative instruction with substantial AI assistance. All observations and coefficients below are synthetic. A solver returning numbers is not enough evidence that the data identify a meaningful model. Prerequisites are functions, array axes and floating-point cancellation.

## Learning objectives

1. Fit and check a small affine model using centered coordinates and residuals.
2. Diagnose rank loss and distinguish predictions from separately identifiable coefficients.
3. Compare stable numerical calculation with statistical validation and measurement uncertainty.

## Define the residual and the loss

For y_i≈a+b x_i, let residual r_i=y_i−(a+b x_i). Ordinary least squares chooses a and b to minimize the sum of squared residuals. It assumes the declared loss is appropriate; it does not infer why errors occurred. Large residuals receive disproportionately large weight. A single corrupted row can influence both coefficients, which connects fitting back to parsing and input contracts.

For a full-rank affine model, center the coordinates with z_i=x_i−x̄. The intercept in centered coordinates is ȳ, and the slope is the sum of z_i(y_i−ȳ) divided by the sum of z_i². Transforming back gives a=ȳ−b x̄. Centering separates the offset and slope columns and reduces avoidable cancellation when x values share a large common baseline.

The design matrix has one row per observation and columns [1,z_i]. Its shape is (observations,2). Matrix multiplication by [centered_intercept,slope] produces one prediction per observation. Shape checks do not establish rank, and rank does not establish that an affine relationship is appropriate. Those are different checks with different evidence.

## Exact fitting is not always parameter identification

If all x values equal two, the uncentered design columns [1,x] are proportional. The observations constrain a+2b, but cannot separately determine a and b. A rank-revealing solver may return one minimum-norm coefficient pair, which is a convention among multiple possible pairs. That pair is not an experimental identification of both parameters.

For repeated y=5 at x=2, [a,b]=[1,2] and [5,0] make exactly the same predictions. Their different slopes imply different extrapolations. A zero residual therefore coexists with unidentified extrapolation behavior. Collecting many more observations at the same x improves information about the combined level under a suitable noise model, but does not create the missing independent direction.

Near rank loss is a conditioning problem. Very closely spaced x values can give a tiny denominator for slope estimation. Small changes in observations can then cause large coefficient changes. Rescaling a variable can improve numerical representation and make coefficients easier to interpret, but it does not create new experimental variation. Condition and identifiability should be discussed together without treating them as identical.

## Avoid squaring conditioning unnecessarily

The normal equations form XᵀX and solve XᵀX β=Xᵀy. In a full-rank setting, the spectral condition number of XᵀX is the square of that of X. Forming this product can worsen numerical sensitivity. QR or singular-value methods operate on the design matrix more directly and can expose rank information. An explicit matrix inverse is also unnecessary for solving a linear system.

A library call is useful when its outputs are interpreted. The following original example uses synthetic centered observations. It specifies the rank threshold argument explicitly, then recomputes residuals rather than assuming the returned residual array is always populated.

```python
import numpy as np

z = np.array([-1., 0., 1.])
y = np.array([2., 3., 5.])
design = np.column_stack((np.ones(z.size), z))
coef, _, rank, singular_values = np.linalg.lstsq(design, y, rcond=None)
residual = y - design @ coef
sse = residual @ residual
```

An empty residual array from a least-squares routine can describe rank or matrix-shape conditions; it does not necessarily mean zero residual error. Recomputing predictions and the intended loss makes that distinction explicit. Singular values and rank also depend on scale and the chosen numerical cutoff, which belong in the analysis record.

## Worked example

For z=[−1,0,1] and y=[2,3,5], the mean response is 10/3 and slope is 1.5. Predictions are [11/6,10/3,29/6], with residuals [1/6,−1/3,1/6]. Their sum is zero, and their dot product with z is zero. These orthogonality checks follow from the least-squares conditions and provide a separate way to assess the fit. Sum of squared residuals is 1/6.

There are three observations and two fitted coefficients, so residual degrees of freedom are one. A residual standard error computed as sqrt(SSE/(n−p)) is sqrt(1/6)≈0.408248. That quantity requires an appropriate error model to support inference. It is neither a held-out prediction score nor an automatic confidence interval. A line with two observations has no residual degrees of freedom for this estimate even if it fits exactly.

Now label x as [100000001,100000002,100000003] and z=x−100000002. The centered fit still has slope 1.5 and centered intercept 10/3. The uncentered intercept is approximately −149999999.666667. Its huge magnitude reflects the remote origin, not a large local measured response. Reporting the centered equation makes the observed-domain meaning clearer.

The preserved floating-point lesson estimates spacing near 10⁸ using |x| times epsilon. That is a scale estimate, not the exact adjacent-float spacing. In binary64, 10⁸ lies in the binade [2²⁶,2²⁷), so spacing is 2^(26−52)=2⁻²⁶≈1.490116×10⁻⁸. The existing approximate question and key are preserved. Distinguishing the exact binade value prevents treating the approximation as a library result.

## Common mistakes

Interpreting a minimum-norm pair as uniquely measured coefficients, calling an empty residual array a perfect fit, and extrapolating a local centered model without checking its domain all mislead. Computing tiny variation as the difference of two huge second moments invites cancellation. A stable algorithm fixes numerical loss; it cannot establish a biological mechanism or eliminate sampling bias.

## Limits of this lesson

The lesson covers small affine least-squares problems. Robust losses, correlated errors, regularization and nonlinear model uncertainty need further work. Formative items assess coefficients and selected decisions without running learner code. The [NumPy least-squares reference](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) is link-only; its examples are not imported. The original code and numerical construction are CC BY 4.0, with no qualified review.
