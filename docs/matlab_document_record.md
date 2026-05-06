# MATLAB AUTOSAR Documentation Record

## 📘 Overview

This document records the official **MATLAB/Simulink AUTOSAR Blockset configurations** used as reference models in the paper *“Acausal Modeling and Code Generation for AUTOSAR Applications Based on Modelica”*.  

It serves as a visual reference for:
- The **AUTOSAR Dictionary** and configuration settings of each example model.
- The **AUTOSAR Mappings** between Simulink elements and AUTOSAR software components.
- Comparison against the corresponding **Modelica-based AUTOSAR models** presented in the M2 library.

Seven example models are derived from official AUTOSAR Blockset examples, 
and one additional large-scale model is constructed for scalability evaluation， and they are used for **functional equivalence testing**, **semantic mapping validation**, and **NRMSE evaluation**.

In total, eight experimental cases are included.

---

## 📂 Included Examples

This record includes seven representative automotive AUTOSAR examples:

1. `autosar_swc` — Basic AUTOSAR Software Component
2. `autosar_swc_expfcns` — AUTOSAR SWC with external functions
3. `autosar_swc_throttle_sensor` — Throttle position sensing component
4. `autosar_swc_monitor` — Monitoring and diagnostic component
5. `autosar_swc_pedal_sensor` — Pedal position sensing component
6. `autosar_swc_controller` — Controller component for actuator coordination
7. `autosar_swc_actuator` — Actuator control component
8. `large_scale_autosar_swc_expfcns` - a large-scale AUTOSAR application-layer case, is constructed with 108 runnables, 211 PPorts, and 109 IRVs. It forms a high-density, deeply interconnected signal-processing chain in which runnables perform transformations and exchange data via IRVs.

Each example corresponds to one case used in performance evaluation and NRMSE comparison.  
For each example, this document records two sections:

- **AUTOSAR Dictionary** — showing the software component structure, ports, interfaces, and data elements defined in MATLAB/Simulink.
- **AUTOSAR Mappings** — showing how Simulink model blocks are mapped to AUTOSAR components, runnable entities, and communication interfaces.

---

## 🧩 Example Records

### 1. autosar_swc

https://ww2.mathworks.cn/help/autosar/ug/example-modeling-patterns-for-autosar-runnables.html

#### AUTOSAR Dictionary
*(Insert screenshot of AUTOSAR Dictionary interface here, e.g. `images/autosar_swc_dictionary.png`)*
![](example_pics/1-1.png)
![](example_pics/1-2.png)
![](example_pics/1-3.png)
![](example_pics/1-4.png)
![](example_pics/1-5.png)
![](example_pics/1-6.png)
![](example_pics/1-7.png)
![](example_pics/1-8.png)
![](example_pics/1-9.png)
![](example_pics/1-10.png)
![](example_pics/1-11.png)

#### AUTOSAR Mappings
![](example_pics/1-12.png)
![](example_pics/1-13.png)
![](example_pics/1-14.png)
![](example_pics/1-15.png)
![](example_pics/1-16.png)


---

### 2. autosar_swc_expfcns

https://ww2.mathworks.cn/help/autosar/ug/example-model-autosar-runnables-exported.html

#### AUTOSAR Dictionary
![](example_pics/2-1.png)
![](example_pics/2-2.png)
![](example_pics/2-3.png)
![](example_pics/2-4.png)
![](example_pics/2-5.png)
![](example_pics/2-6.png)
![](example_pics/2-7.png)
![](example_pics/2-8.png)
![](example_pics/2-9.png)
![](example_pics/2-10.png)


#### AUTOSAR Mappings
![](example_pics/2-11.png)
![](example_pics/2-12.png)
![](example_pics/2-13.png)
![](example_pics/2-14.png)
![](example_pics/2-15.png)

---

### 3. autosar_swc_throttle_sensor

https://ww2.mathworks.cn/help/autosar/ug/example-import-autosar-composition-to-simulink.html
#### AUTOSAR Dictionary
![](example_pics/3_1.png)
![](example_pics/3_2.png)
![](example_pics/3_3.png)
![](example_pics/3_4.png)
![](example_pics/3_5.png)
![](example_pics/3_6.png)
![](example_pics/3_7.png)
![](example_pics/3_8.png)
![](example_pics/3_9.png)
![](example_pics/3_10.png)
![](example_pics/3_11.png)
![](example_pics/3_12.png)
![](example_pics/3_13.png)
![](example_pics/3_14.png)

#### AUTOSAR Mappings
![](example_pics/3_15.png)
![](example_pics/3_16.png)
![](example_pics/3_17.png)
![](example_pics/3_18.png)
![](example_pics/3_19.png)

---

### 4. autosar_swc_monitor

https://ww2.mathworks.cn/help/autosar/ug/example-import-autosar-composition-to-simulink.html

#### AUTOSAR Dictionary
![](example_pics/4_1.png)
![](example_pics/4_2.png)
![](example_pics/4_3.png)
![](example_pics/4_4.png)
![](example_pics/4_5.png)
![](example_pics/4_6.png)
![](example_pics/4_7.png)
![](example_pics/4_8.png)
![](example_pics/4_9.png)
![](example_pics/4_10.png)
![](example_pics/4_11.png)
![](example_pics/4_12.png)

#### AUTOSAR Mappings
![](example_pics/4_13.png)
![](example_pics/4_14.png)
![](example_pics/4_15.png)

---

### 5. autosar_swc_pedal_sensor

https://ww2.mathworks.cn/help/autosar/ug/example-import-autosar-composition-to-simulink.html

#### AUTOSAR Dictionary
![](example_pics/5_1.png)
![](example_pics/5_2.png)
![](example_pics/5_3.png)
![](example_pics/5_4.png)
![](example_pics/5_5.png)
![](example_pics/5_6.png)
![](example_pics/5_7.png)
![](example_pics/5_8.png)
![](example_pics/5_9.png)
![](example_pics/5_10.png)
![](example_pics/5_11.png)
![](example_pics/5_12.png)

#### AUTOSAR Mappings
![](example_pics/5_13.png)
![](example_pics/5_14.png)
![](example_pics/5_15.png)


---

### 6. autosar_swc_controller

https://ww2.mathworks.cn/help/autosar/ug/example-import-autosar-composition-to-simulink.html

#### AUTOSAR Dictionary
![](example_pics/6_1.png)
![](example_pics/6_2.png)
![](example_pics/6_3.png)
![](example_pics/6_4.png)
![](example_pics/6_5.png)
![](example_pics/6_6.png)
![](example_pics/6_7.png)
![](example_pics/6_8.png)
![](example_pics/6_9.png)
![](example_pics/6_10.png)
![](example_pics/6_11.png)
![](example_pics/6_12.png)

#### AUTOSAR Mappings
![](example_pics/6_13.png)
![](example_pics/6_16.png)
![](example_pics/6_16.png)

---

### 7. autosar_swc_actuator

https://ww2.mathworks.cn/help/autosar/ug/example-import-autosar-composition-to-simulink.html

#### AUTOSAR Dictionary
![](example_pics/7_1.png)
![](example_pics/7_2.png)
![](example_pics/7_3.png)
![](example_pics/7_4.png)
![](example_pics/7_5.png)
![](example_pics/7_6.png)
![](example_pics/7_7.png)
![](example_pics/7_8.png)
![](example_pics/7_9.png)
![](example_pics/7_10.png)
![](example_pics/7_11.png)
![](example_pics/7_12.png)
![](example_pics/7_13.png)

#### AUTOSAR Mappings

![](example_pics/7_14.png)
![](example_pics/7_15.png)
![](example_pics/7_16.png)
![](example_pics/7_17.png)
---


### 8. large_scale_autosar_swc_expfcns
This model is manually extended and is used for scalability experiments. It contains 108 runnable entities, along with a large number of ports and inter-runnable variables (IRVs), and is used to evaluate scalability.

#### Simulink model
![](example_pics/8_1.png)
![](example_pics/8_2.png)


#### AUTOSAR Dictionary
![](example_pics/8_3.png)
![](example_pics/8_4.png)
![](example_pics/8_5.png)
![](example_pics/8_6.png)
![](example_pics/8_7.png)

#### AUTOSAR Mappings
![](example_pics/8_8.png)
![](example_pics/8_9.png)
![](example_pics/8_10.png)


## 📎 Notes

- The first seven models are from official examples of the AUTOSAR Blockset, while the eighth model is created for scalability experiments.
- These records are used for comparison and validation with the Modelica-based AUTOSAR modeling framework (`M2/Examples`).
- For details on ARXML and C code generation results, refer to the modelica_generate/ directory.
- The naming convention follows the same case identifiers as used in the experimental evaluation section of the paper.

---

Last updated: March 2026
