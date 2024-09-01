# Genesys Cloud Project

This project connects to the Genesys Cloud API, retrieves user details using the `get_analytics_users_details` query, extracts the primary presence from the results, and saves the information to the database.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/tharlesamaro/genesys-cloud-insert-primary-presence.git
cd genesys-cloud-insert-primary-presence
```

### 2. Create and activate a virtual environment (optional, but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project includes a CLI script located in `app/cli.py`. To run commands, use the following format:

```bash
python app/cli.py <command> [options]
```

### Example:

```bash
python app/cli.py insert-data-primary-presence '2024-08-08T00:00:00/2024-08-08T23:59:59';
```

This command will fetch user data from the Genesys Cloud API and save the information to the database.

This command will fetch user data from the Genesys Cloud API and save the information to the database.

## Running the project using Docker

### 1. Build the Docker image

In the root of the project, run:

```bash
docker build -t genesys-cloud-app .
```

### 2. Run the container

```bash
docker run -d genesys-cloud-app
```

This will start the container and run the project.

### 3. Access the container interactively (optional)

If you need to access the container to run commands interactively:

```bash
docker run -it genesys-cloud-app /bin/bash
```

### 4. Running commands inside the container

You can run the `cli.py` script inside the container:

```bash
docker run genesys-cloud-app python app/cli.py <command> [options]
```

### 5. Stopping and removing the container

To stop and remove the container:

```bash
docker stop <container_id>
docker rm <container_id>
```