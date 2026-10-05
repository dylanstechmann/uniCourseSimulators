# Controller design and sampled implementation

Proportional action responds to present error, integral action accumulates past error to remove steady-state offset, and derivative action responds to error trend but amplifies high-frequency noise. PID tuning trades rise time, overshoot, steady-state accuracy, and robustness. Digital implementation introduces sample-and-hold behavior, computation delay, quantization, and derivative filtering. The tested controller should include actuator limits and anti-windup logic; a mathematically stable ideal design can fail on hardware.
