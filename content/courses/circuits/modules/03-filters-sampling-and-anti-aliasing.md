# Filters, sampling, and anti-aliasing

A first-order low-pass RC filter has fc=1/(2πRC), attenuating frequencies above cutoff. Sampling at fs maps continuous-time frequencies into discrete-time spectra; components above fs/2 alias unless filtered or otherwise constrained. A practical anti-alias filter needs a transition band and attenuation matched to dynamic range and downstream analysis. Digitization also requires adequate resolution, stable timing, and calibrated gain.
