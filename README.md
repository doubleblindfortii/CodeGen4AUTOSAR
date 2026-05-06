# CodeGen4AUTOSAR

**Acausal Modeling and Code Generation for AUTOSAR Applications Based on Modelica**

---

## 📘 Overview

This repository provides the **open-source artifacts, experimental records, and supporting scripts** for the paper:

> **Acausal Modeling and Code Generation for AUTOSAR Applications Based on Modelica**

The repository includes:
- The complete **source code** for the Modelica-based AUTOSAR modeling and code generation framework.
- **Experimental scripts and records** used for model transformation, evaluation, and performance testing.
- **Documentation** related to the eight experimental cases reported in the paper.

Due to confidentiality requirements, the **final compiled visualization and full-featured UI version** of the tool cannot be made public here.  
The final integrated product (including visualization, data management, and simulation orchestration interfaces) has been released on the platform below:

🔗 **[Product page on MoHub Science Platform](https://mohub.net/science/toolDetail?id=165)**

---

## 📂 Repository Structure

```bash
CodeGen4AUTOSAR/
│
├── README.md                           # Project description (this file)
├── LICENSE                             # License GPL
├── .gitignore                          # Ignore Simulink cache, Modelica build files, temp logs
│
├── docs/                               # 📘 Documentation
│   ├── matlab_document_record.md        # Record of 8 MATLAB-side experimental cases
│   ├── performance_screenshots/         # Performance and runtime screenshots
│   │   ├── simulink/*.png               # Simulink benchmark screenshots
│   │   └── modelica/*.txt               # Modelica benchmark logs
│   └── paper_related/                   # Paper-related supporting materials
│       └── elements_arxml_count.xlsx    # Statistics of ARXML elements and our custom XML file(for MIC and Line counts in case study)
│
├── src/                                # 💻 Source code
│   ├── python/                          # Python utilities and automation scripts
│   │   ├── eva.py                       # NRMSE metric computation script
│   │   ├── CCodeGenerate/               # AUTOSAR-compliant C code generation module
│   │   └── convertARXML/                # ARXML transformation and configuration parser
│   │
│   ├── modelica/                        # Modelica engineering and libraries
│   │   ├── M2/                          # Modelica AUTOSAR wrapper libraries
│   │   │   ├── VisibleElements/
│   │   │   ├── Utilities/
│   │   │   ├── AUTOSAR_Templates/
│   │   │   └── MSR/
│   │   ├── examples/                    # Example cases (used in the paper)
│   │   │   ├── autosar_swc_Example.mo
│   │   │   ├── Swc_Expfcns_Example.mo
│   │   │   └── autosar_composition/
│   │   │       ├── autosar_swc_throttle_sensor.mo
│   │   │       ├── test_autosar_swc_throttle_sensor.mo
│   │   │       └── ... more examples
│   │   └── modelica_generate/           # Modelica-generated ARXML and C source files
│   │       ├── autosar_swc/
│   │       │   ├── first/
│   │       │   └── after_sim/
│   │       └── ... others
│   └── configuration/                   # Custom AUTOSAR XML configuration files
│       ├── autosar_swc_mo_configuration.xml
│       └── ... others
│
├── simulink/                           # ⚙️ Simulink-related content
│   ├── source_models/
│   │   ├── native/                      # Original AUTOSAR Blockset models
│   │   └── add_source/                  # Models with additional source signals
│   ├── workspace/                       # Simulink auto-generated code directories, containing ARXML files and C files generated.
│   │   ├── autosar_swc_autosar_rtw/
│   │   ├── autosar_swc_monitor_autosar_rtw/
│   │   └── ... others
│
├── results/                            # 📊 Simulation and evaluation results
│   ├── simulation/                      # Output data for evaluation
│   │   ├── simulink/                    # Simulink CSV outputs after simulation.
│   │   └── modelica/                    # Modelica CSV outputs after simulation.
│
├── external/                           # 🌐 External linked repositories
│   └── Modelica4AUTOSAR/                # Submodule: Modelica-based visual modeling and multi-domain examples
│       ↳ https://github.com/xxx/Modelica4AUTOSAR
│       # Contains detailed Modelica visual modeling cases, domain examples, used in the paper.

```




# 🧩 Functional Description

This repository serves as the research and reproducibility version of the **AUTOSAR–Modelica integration framework**.

---




## 🔹 Python Components

Located under `src/python/`, these scripts implement several core utilities:

- **eva.py**  
  Computes **NRMSE (Normalized Root Mean Square Error)** between Simulink and Modelica simulation results.

- **CCodeGenerate/**  
  Contains functions for transforming **AUTOSAR XML** into **C source code templates**.

- **convertARXML/**  
  Implements **XML structure parsing and translation** for Modelica–AUTOSAR interoperability.




> **Note:** Only partial functionality is available via direct Python execution.  
> The full AUTOSAR modeling, visualization, configuration, transformation, and code generation workflows are integrated in the official toolchain, which centers around a **unified UI framework**.  
> For complete functionality, please download the integrated toolbox from the link above.

--- 
## 🔬 Minimal Working Example

To help users quickly understand and reproduce the workflow, we provide a minimal working example based on the `autosar_swc` case.

This example demonstrates the complete pipeline from Simulink modeling to Modelica-based reconstruction, configuration, code generation, and final evaluation.

---

### Step 1: Simulink Model (Reference Baseline)

This part serves only as the baseline for comparison with the Modelica-based implementation.

- Open the model: `simulink/source_models/native/autosar_swc.slx`
- Open the AUTOSAR toolchain in Simulink:
- Navigate to **Apps → AUTOSAR Component**
- Build the control logic model as shown in:
  ```
  docs/example_pics/1-0.png
  ```

- Configure **AUTOSAR Dictionary**:
- Click the corresponding button in the AUTOSAR toolstrip
- Configure elements as illustrated in:
  ```
  docs/example_pics/1-2.png ~ 1-11.png
  ```

- Configure **AUTOSAR Mappings**:
- Click the mapping configuration button
- Set mappings as shown in:
  ```
  docs/example_pics/1-12.png ~ 1-16.png
  ```

- Run simulation:
- Click the **Simulation** button to execute the model

- Generate AUTOSAR artifacts:
- Click **Generate Code** in the AUTOSAR toolstrip
- The generated files include:
  - ARXML files
  - C source files (.c, .h)

- Output directory: `simulink/workspace/autosar_swc_autosar_rtw/`
---

### Step 2: Modelica-Based Modeling and Generation

#### Preparation

Download the integrated toolchain from:

🔗 https://mohub.net/science/toolDetail?id=165

This tool provides a Modelica-based AUTOSAR modeling environment built on MWorks Sysplorer.  
The framework is platform-independent and can also be adapted to other Modelica environments (e.g., OpenModelica) due to its Qt-based architecture.

---

#### Modeling and Configuration

- Open **Sysplorer**
- Load the Modelica AUTOSAR library:`src/modelica/M2/`
- Navigate to the example model: `M2/Examples/autosar_swc_Example.mo`
- Construct the Modelica model using drag-and-drop composition:
- Combine AUTOSAR library components with Modelica standard libraries
- The resulting model is shown in:
  ```
  docs/example_pics/1-17.png
  ```

- Open AUTOSAR configuration panel:
- Navigate to:
  ```
  Tool → AUTOSAR Tool
  ```

- Configure:
- AUTOSAR Dictionary
- AUTOSAR Mapping

These configurations correspond to those in Simulink, and are internally stored in: `src/configuration/autosar_swc_mo_configuration.xml`

---

#### Simulation and Code Generation

- Run simulation:
- Click the **Simulation** button in Sysplorer

- Generate AUTOSAR artifacts:
- Click **Generate Code**
- Specify output directory

- Generated files include:
- ARXML files
- AUTOSAR-compliant C code

- Output directory:`src/modelica/modelica_generate/autosar_swc/`

---

### Step 3: Result Comparison and Evaluation

#### Simulation Output

- Simulink results:`results/simulation/simulink/autosar_swc_si.csv`
- Modelica results:`results/simulation/modelica/autosar_swc_mo.csv`

---

#### Performance Measurement

- Simulation runtime (5-run average):
- Simulink:
  ```
  docs/performance_screenshots/simulink/
  ```
- Modelica:
  ```
  docs/performance_screenshots/modelica/
  ```

---

#### NRMSE Computation

Run:

```bash
python src/python/eva.py
```
This script computes the NRMSE (Normalized Root Mean Square Error) between Simulink and Modelica simulation outputs.

#### Structural Metrics (MIC & Lines)
- Analyze:
 - Generated ARXML files
 - XML configuration file: `src/configuration/autosar_swc_mo_configuration.xml`

- Statistical results are recorded in:`docs/paper_related/elements_arxml_count.xlsx`

These metrics support the evaluation of model complexity and structural consistency.


### Step 4: Open-Source Scope and Extensibility

This framework is open-sourced for reproducibility.

The AUTOSAR Dictionary and Mapping interfaces are implemented in a Qt-based environment within MWorks Sysplorer.
The same methodology can be re-implemented in other Modelica environments (e.g., OpenModelica).

code-generation open-source components include:

- ARXML transformation: `src/python/convertARXML/`

- AUTOSAR C code generation: `src/python/CCodeGenerate/`

These modules are implemented in Python and can be executed independently, enabling integration into external toolchains.

---

## 📚 Documentation and Experimental Records

All experimental cases corresponding to the paper are documented in:

📄 **docs/matlab_document_record.md**

This document contains **eight experimental cases**, each with:

- **AUTOSAR Dictionary** subsection (showing data element definitions)  
- **AUTOSAR Mappings** subsection (showing mapping screenshots)

Performance comparison screenshots, NRMSE computation outputs, and ARXML statistics are also included in the  
`docs/performance_screenshots/` and `docs/paper_related/` directories.

---




## 🧠 Citation

If you use this repository in your research, please cite the associated paper:

> XXX, et al.  
> *Acausal Modeling and Code Generation for AUTOSAR Applications Based on Modelica.*  
XXX

---

## ⚖️ License

This project is released under the **GPL License**.  
See the `LICENSE` file for details.

---

## 🧩 Contact

For technical discussions or collaboration inquiries, please contact:



