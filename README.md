# Network Flow Simulator — Ford–Fulkerson Algorithm

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Python version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

A simulator for **network flow** problems using the **Ford–Fulkerson algorithm**, with support for visualizing augmenting paths and residual graphs.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Authors (and Hardships)](#authors)

---

## Overview

This project provides a tool to model and solve **maximum flow** problems on directed graphs using the classical **Ford–Fulkerson method**, **Edmond-Karp Method** and **Dinic's Algorithm**. It visualizes the residual graph, tracks augmenting paths, and helps users understand how flow evolves step by step.

Typical use cases include:

- Educational demonstrations of flow algorithms
- Visual simulation of flow networks
- Comparing algorithmic performance on custom input data

---

## Features

- Build **directed graphs** with edge capacities
- Compute **maximum flow** using Ford–Fulkerson
- Track **augmenting paths** iteratively
- Visualize or output **residual graphs**
---

## Getting Started

### Prerequisites

- Python 3.6+
- `networkx` — for graph structure and manipulation
- `pandas` — to read datasets
- `pyvis`, `webbrowser`, `os` — for interactive visualization of complex graphical structures
Install dependencies:

```bash
pip install -r requirements.txt
```
### Installation
Clone the repository

```bash
git clone https://github.com/paulpseudoman/Network-Flow-Simulation-Ford-Fulkerson-Algorithm.git
cd Network-Flow-Simulation-Ford-Fulkerson-Algorithm
```
### Using the repository
Now you can browse through the pseudocodes to understand the working principle, can execute the codes to get desired outputs. Note that if you use a `*.csv` file as input, then use the `Converter.py` to convert it, and paste the output in original code.
Also, you can go through the datasets we have used, and view the interactive outputs. You can also create your own interactive visualization, just choose the corresponding directed (eg. `Gport.html`) or undirected code (eg. `GNH.html`).

## Authors
- [_Aritrabha Majumdar_](https://paulpseudoman.github.io) (BMAT2311)
- [_Aanchal Saraf_](https://github.com/aanchal-0303) (BMAT2301)

Aanchal has put a lot of efforts a lot of efforts converting the highway data of India in a *comma separated value* format. And she has provided and compiled all the other available datasets...***Kudos!!!***
