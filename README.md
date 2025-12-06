Synaptic Transmission Simulation: A meets B 

## Overview
This project simulates the biological communication between two neurons (Synaptic Transmission). It moves beyond single-neuron models to demonstrate how an Action Potential in a **Presynaptic Neuron (A)** triggers an Excitatory Post-Synaptic Potential (EPSP) in a **Postsynaptic Neuron (B)**.

## The Model
The simulation uses two **Leaky Integrate-and-Fire (LIF)** neurons connected by a chemical synapse.

### 1. Presynaptic Neuron (A)
* Receives an external current ($I_{ext}$).
* Fires a spike when voltage crosses the threshold (-50 mV).

### 2. The Synapse (Alpha Function)
Unlike electrical wires, biological synapses have a time delay and a dynamic conductance profile. I modeled this using the **Alpha Function**, which describes the time course of neurotransmitter release and receptor binding:

$$g_{syn}(t) = g_{max} \cdot \frac{t - t_{spike}}{\tau_{syn}} \cdot e^{1 - \frac{t - t_{spike}}{\tau_{syn}}}$$

* **Rise Time:** Represents the opening of ligand-gated ion channels.
* **Decay Time:** Represents the clearing of neurotransmitters.

### 3. Postsynaptic Neuron (B)
* Receives the synaptic current defined by Ohm's Law:
  $$I_{syn} = g_{syn}(t) \cdot (V_B - E_{syn})$$
* This current causes a temporary rise in voltage (**EPSP**), mimicking the input signals real neurons receive.

## Results
The graph below shows the chain reaction:
1.  **Blue:** Neuron A spikes due to input current.
2.  **Orange:** The synapse conductance rises smoothly (Alpha Function).
3.  **Green:** Neuron B reacts with a sub-threshold potential (EPSP).

![Synaptic Transmission Result](synapse_result.png)

## Technologies
* **Python**
* **NumPy**
* **Matplotlib**
