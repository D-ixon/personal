import numpy as np
import matplotlib.pyplot as plt

# 1. Generate an analog signal (e.g., a Sine Wave)
fs = 100            # Sampling frequency
t = np.linspace(0, 1, fs)
analog_signal = np.sin(2 * np.pi * 5 * t)

# 2. Define quantization parameters
bits = 3                        # Number of bits
levels = 2**bits                # Total number of quantization levels
v_min, v_max = -1, 1            # Signal amplitude range

# 3. Quantization process
# Step A: Normalize signal to 0 to 1 range
norm_signal = (analog_signal - v_min) / (v_max - v_min)
# Step B: Scale to the number of levels
scaled_signal = norm_signal * (levels - 1)
# Step C: Round to the nearest discrete integer level
quantized_indices = np.round(scaled_signal)
# Step D: Map back to the original range
quantized_signal = (quantized_indices / (levels - 1)) * (v_max - v_min) + v_min

# 4. Visualization
plt.figure(figsize=(10, 5))
plt.plot(t, analog_signal, label='Analog Signal', color='gray', alpha=0.5)
plt.step(t, quantized_signal, label=f'{bits}-bit Quantized Signal', color='red', where='mid')
plt.title('Analog Signal vs. Quantized Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()