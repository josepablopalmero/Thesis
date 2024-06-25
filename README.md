# Biomechatronic Rehabilitation System

## Overview

This project focuses on the design and development of a biomechatronic system aimed at the rehabilitation of patients with hand pathologies. The primary objective is to replicate the rehabilitation movements of patients through a robotic hand in the physiotherapist's clinic, enabling real-time monitoring of the patient's progress. The system combines image capture software tools with hardware that replicates the movements, offering a hybrid solution that optimizes both in-person and telematic sessions for patients and physiotherapists.

## Features

- Real-time monitoring of rehabilitation movements.
- Hybrid solution combining in-person and remote sessions.
- Designed for patients on waiting lists for physical rehabilitation and those with reduced mobility.

## Installation

### Prerequisites

Ensure you have the following libraries installed:

- [LX16A Library by danjperron](https://github.com/danjperron/LX16A)
- [Lewansoul LX-16A Library by maximkulkin](https://github.com/maximkulkin/lewansoul-lx16a/tree/master/lewansoul-lx16a)

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/josepablopalmero/Thesis.git
   cd Thesis
   ```

2. Install the required libraries:

   ```sh
   pip install lx16a
   pip install lewansoul-lx16a
   ```

3. Run the main script:

   ```sh
   python main.py
   ```

## Usage

1. Connect the robotic hand hardware as per the instructions in the hardware setup guide.
2. Launch the software application.
3. Follow the on-screen instructions to start a rehabilitation session.
4. Monitor the real-time progress of the patient's rehabilitation movements.

## Libraries Used

- **[LX16A Library by danjperron](https://github.com/danjperron/LX16A):** A Python library to control LX-16A servos.
- **[Lewansoul LX-16A Library by maximkulkin](https://github.com/maximkulkin/lewansoul-lx16a/tree/master/lewansoul-lx16a):** A Python package to interface with LewanSoul LX-16A servos.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all those who supported me throughout this project.

---
