# Algo-Trader-Py

Algorithmic trading platform developed in Python for financial market analysis, strategy backtesting, and automated trade execution.

## Project Structure

This project follows the hexagonal architecture (ports and adapters) pattern:

- **src/domain**: Contains the core domain model (entities, value objects, domain services)
- **src/application**: Contains the application services and use cases
- **src/ports**: Contains the interfaces (ports) that define how components interact
- **src/adapters**: Contains the implementations (adapters) of the interfaces
- **tests**: Contains unit, integration, and end-to-end tests

## Getting Started

```bash
# Clone the repository
git clone https://github.com/jrosco85/algo-trader-py.git
cd algo-trader-py

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m src.main
```

## Development

```bash
# Run tests
python -m pytest tests/
```
