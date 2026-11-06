# SeCoNet: Heterosexual Contact Network Growth Model & HPV Transmission Simulation

This repository contains the source code, network generation scripts, and simulation output datasets for the paper:
> **"Influence of Network Topology and Vaccination Strategies on HPV Dynamics: A Simulation Study Using the SeCoNet Growth Model"**

---

## 1. System & Software Requirements

### Hardware Requirements
- **Local Desktop / Workstation (Testing & Small Scale):** 
  - CPU: 4-core processor (8-core recommended)
  - RAM: 8 GB minimum (16 GB recommended)
- **HPC Cluster / Server (Full Experiment Replication):**
  - High-throughput parallel cluster (PBS/SLURM scheduler)
  - Recommended per node: 48 CPU cores, 192 GB RAM

### Software Environment
- **Operating System:** Linux / macOS / Windows
- **Python Version:** Python 3.9+

### Dependencies
Install all required libraries via `pip`:
```bash
pip install -r requirements.txt
