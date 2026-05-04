# 🚆 Transport Network Analysis & Optimization System

## Overview

This project analyzes public transport systems using GTFS data and builds toward a **multi-modal journey simulation system**.

The analysis is conducted at two levels:

* 🇩🇪 **Germany (Macro Level)** → Rail network structure and performance
* 🏙️ **Berlin (Micro Level)** → Urban multi-modal transport dynamics

Berlin is used as a detailed case study within a broader transport system analysis.

---

## Objectives

- Analyze transport network structure and efficiency  
- Evaluate travel time patterns, service frequency, and connectivity  
- Identify key routes, corridors, and transport hubs  
- Simulate multi-modal journeys across transport modes 
- Assess travel performance using time, transfers, and reliability  

---

## Key Analysis

### Germany — Rail Network

- Travel time distribution across the network  
- Service hierarchy (RB, RE, ICE, IC)  
- High-frequency corridors  
- Network connectivity and major stations  

### Berlin — Urban Transport

- Mode-wise distribution (Bus, S-Bahn, U-Bahn)  
- Segment-level travel performance  
- Network density and structure  
- Station centrality and connectivity  
- Route-level operational intensity 

---

## Dashboard

Interactive Tableau dashboard:  
https://public.tableau.com/views/BerlinPublicTransportNetworkAnalysis/Dashboard

The dashboard highlights:

- Travel time distribution  
- Demand vs travel time relationships  
- High-demand routes and congestion patterns  
- Mode-wise performance differences  

---

## Key Insights

- Travel times are heavily skewed toward short segments, with a long tail of slower connections  
- High-demand routes tend to exhibit longer travel times, indicating congestion hotspots  
- S-Bahn routes show higher average travel times compared to U-Bahn and Bus  
- Certain stations function as critical network hubs  

---

## Tech Stack

- Python (Pandas, NumPy)  
- NetworkX (graph modeling)  
- SQL  
- Tableau (visualization)  
- GTFS data 

---

## 📁 Project Structure

```
data/
├── raw/
├── processed/
│ ├── germany/
│ └── berlin/
├── bi/

notebooks/
├── germany/
├── berlin/
├── simulation/

src/
├── simulation/
├── data/
├── features/

dashboard/
└── berlin_transport_dashboard.twbx
```

---

---

## Simulation Engine

The project includes a simulation framework to evaluate journeys based on:

- Total travel time  
- Number of transfers  
- Delay impact  
- Route alternatives  

This forms the basis for future optimization and predictive modeling.

---

## Future Work

- Machine learning for delay prediction  
- Multi-criteria route optimization  
- Real-time simulation and dynamic routing  
- Expansion to larger transport networks  

---

## Author

Nitin Singh  
MSc Data Analytics  
Berlin School of Business & Innovation  

---

## Notes

Trip frequency is used as a proxy for service intensity and not actual passenger demand.