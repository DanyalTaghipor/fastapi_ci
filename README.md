# FastAPI CRUD for Cryptocurrency Exchange

This project provides a simple CRUD API for managing cryptocurrencies in a mock exchange environment.

## Features

- Add a new coin to the exchange
- Update details of an existing coin
- Retrieve details of a specific coin
- List all coins in the exchange
- Delete a coin from the exchange

## Setup and Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd path-to-repository
```

2. **Install the required packages:**

```bash
pip install -r requirements.txt
```

3. **Run the FastAPI server:**

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

## Endpoints

- `POST /coins/`: Add a new coin
- `GET /coins/{coin_id}`: Retrieve details of a specific coin
- `PUT /coins/{coin_id}`: Update details of a specific coin
- `DELETE /coins/{coin_id}`: Delete a coin
- `GET /coins/`: List all coins

## Testing

Tests are available in the `tests` directory. To run them, use:

```bash
pytest
```

## Continuous Integration

This project uses GitHub Actions for continuous integration. Check the `.github/workflows` directory for workflow configurations.

## Contributions

Contributions are welcome. Please fork the repository, create a new branch for your changes, and submit a pull request. 
