# Student Hub - DS2 Problem Solving

This repository contains the DS2 version of the Student Hub mini-site project.

## Project content

- `html/`: static pages
- `css/`: shared styles
- `js/`: client-side behavior
- `Dockerfile`: image definition for the web app
- `docker-compose.yml`: local startup configuration
- `.github/workflows/ci.yml`: GitHub Actions workflow
- `scripts/validate_site.py`: local validation script

## Prerequisites

- Docker 26 or newer
- Docker Compose v2
- Python 3.10 or newer

## Run locally

```bash
docker compose up --build
```

Then open `http://localhost:8080`.

## Validate the project

```bash
python scripts/validate_site.py
```

## CI/CD workflow

The GitHub Actions pipeline:

1. checks out the repository
2. validates the static project structure
3. builds the Docker image

## DS2 checklist

- Dockerized static site with `nginx:alpine`
- `docker-compose.yml` to run the service
- CI workflow for validation and image build
- README updated with setup steps
