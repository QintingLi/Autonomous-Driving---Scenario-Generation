# Autonomous Driving Scenario Generation

This project provides a comprehensive framework for generating autonomous driving scenarios using **CARLA** (CAR Learning Autonomous Driving Scenarios) and integrating **Scenic** for scenario descriptions. The repository consists of both front-end and back-end components, enabling efficient visualization, simulation, and control of autonomous driving scenarios.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project integrates:
1. **CARLA Simulator**: A flexible simulator for autonomous driving research.
2. **Scenic**: A probabilistic programming language for scenario generation.
3. **Front-end Application**: A web-based interface to visualize and interact with the scenarios.
4. **Back-end Server**: Handles data flow, scenario compilation, and communication with the CARLA simulator.

### Objectives
- Real-time visualization of autonomous driving scenarios.
- Flexible scenario creation and management.
- AI-driven interaction and analysis for generated scenes.

---

## Features

- **Scenario Generation**: Use Scenic scripts to create diverse driving scenarios.
- **Integration with CARLA**: Communicates with the CARLA simulator for rendering and data collection.
- **Web-based Front-end**: A dynamic React-based interface for visualization.
- **Back-end with Python**: Flask-based server for managing scenario data and simulation processes.
- **Real-time Interaction**: Update scenarios and control simulation parameters dynamically.

---

## Project Structure

```
Autonomous-Driving---Scenario-Generation/
├── .vscode/                  # Editor configuration files
├── public/                   # Static assets for the web application
├── src/                      # React front-end source code
│   ├── components/           # Reusable UI components
│   ├── App.tsx               # Main application file
│   └── index.tsx             # React entry point
├── backend/                  # Python back-end code
│   ├── server.py             # Flask server for communication
│   ├── test_webcam.py        # Test script for webcam integration
│   ├── poetry.lock           # Poetry dependency lock file
│   └── pyproject.toml        # Poetry project configuration
├── package.json              # Front-end dependencies
├── tsconfig.json             # TypeScript configuration
├── vite.config.ts            # Vite configuration for front-end build
└── README.md                 # Documentation
```

---

## Requirements

### Front-end:
- Node.js (v16 or higher)
- npm or Yarn

### Back-end:
- Python (v3.8 or higher)
- Poetry (for dependency management)
- CARLA Simulator (v0.9.13 or higher)

---

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/Autonomous-Driving---Scenario-Generation.git
cd Autonomous-Driving---Scenario-Generation
```

### Step 2: Install Front-end Dependencies
Navigate to the root directory and install dependencies:
```bash
cd src
npm install
```

### Step 3: Install Back-end Dependencies
Navigate to the `backend` folder and install Python dependencies:
```bash
cd backend
poetry install
```

### Step 4: Configure CARLA Simulator
Download and set up the CARLA simulator from [CARLA Releases](https://carla.org/).

---

## Usage

### Running the Project

#### 1. Start the Back-end Server
From the `backend` folder, run:
```bash
poetry run python server.py
```

#### 2. Start the Front-end
Navigate to the `src` folder and run:
```bash
npm run dev
```

#### 3. Open in Browser
Visit `http://localhost:3000` to access the web application.

#### 4. Run CARLA Simulator
Start the CARLA simulator on your machine, ensuring it is set to the default port.

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with detailed information about your changes.

---

Feel free to modify this README to suit additional specifics about the project!
