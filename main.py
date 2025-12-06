import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T = 100
time = np.arange(0, T, dt)

V_rest = -70.0
V_reset = -70.0
V_thresh = -50.0
tau_m = 10.0


g_max = 0.05
tau_syn = 2.0
E_syn = 0.0


g_syn = np.zeros(len(time))
V_A = np.zeros(len(time))
V_A[0] = V_rest

V_B = np.zeros(len(time))
V_B[0] = V_rest

T_spike = -1
threshold = -40.0

for i in range (len(time)-1):
    if 15.0 > time[i] > 10.0:
        I_ext =100.0
    else:
        I_ext = 0.0

    if V_A[i] >= 0.0:
        V_A[i] = V_reset
        V_A[i+1] = V_reset

    else:
        dV_A = (dt / tau_m) * (-(V_A[i] - V_rest) + I_ext)
        V_A[i+1] = V_A[i] + dV_A

    if V_A[i+1] >= V_thresh:
        V_A[i+1] = 0.0
        if T_spike == -1:
            T_spike = time[i+1]

    if T_spike != -1 and time[i] >= T_spike:
        delta_t = time[i] - T_spike
        term1 = delta_t / tau_syn
        term2 = np.exp(1.0 - (delta_t / tau_syn))
        g_syn[i] = g_max * term1 * term2
    else:
        g_syn[i] = 0.0

    I_syn = g_syn[i] * (V_B[i] - E_syn)

    dvB = (dt / tau_m) * (-(V_B[i] - V_rest) - I_syn * 100.0)
    V_B[i + 1] = V_B[i] + dvB

plt.figure(figsize=(10,10))

plt.subplot(3,1,1)
plt.plot(time, V_A, label='Presynaptic (A)', color='blue')
plt.title('Step 1: Neuron A Fires (Spike)')
plt.ylabel('Voltage (V)')
plt.axhline(V_thresh, color='red', linestyle='--', label='Threshold')
plt.legend(loc='upper right')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(time, g_syn, label='Conductivity (g_syn)', color= "orange")
plt.title('Step 2: Synapses Opens (Neurotransmitter Release')
plt.ylabel('Conductivity (mS)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, V_B, label='Postsynaptic (B)', color='green')
plt.title('Step 3: Neuron B Reactions (EPSP)')
plt.ylabel('Voltage (mV)')
plt.xlabel('Time (ms)')
plt.grid(True)

plt.tight_layout()
plt.show()