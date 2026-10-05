# Regression, uncertainty, and validation

A regression model estimates parameters by matching predictions to observations under a loss function. Training fit does not measure generalization; independent validation or cross-validation estimates performance on new data. Residual structure signals misspecification, autocorrelation, heteroskedasticity, or unmodeled groups. Parameter uncertainty and predictive uncertainty differ. Avoid leakage: preprocessing, feature selection, and threshold tuning must occur inside each training fold.
