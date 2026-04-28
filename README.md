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
- GitHub Actions enabled on the repository

## Run locally

```bash
docker compose up --build
```

Then open `http://localhost:8080`.

To stop the application:

```bash
docker compose down
```

## Validate the project

```bash
python scripts/validate_site.py
```

## CI/CD workflow

The GitHub Actions pipeline:

1. checks out the repository
2. validates the static project structure
3. builds the Docker image

## Branch protection

To stay aligned with the DS2 specification, the `main` branch should be protected in GitHub:

1. Open the repository settings
2. Go to `Branches`
3. Add a rule for `main`
4. Enable `Require status checks to pass before merging`
5. Select the CI workflow check

## Demonstration checklist

For the final presentation and screenshots:

1. Run `docker compose up --build`
2. Show the homepage on `http://localhost:8080`
3. Show the contact page on `http://localhost:8080/contact.html`
4. Run `docker ps`
5. Open the `Actions` tab on GitHub and show a successful CI run

## DS2 checklist

- Dockerized static site with `nginx:alpine`
- `docker-compose.yml` to run the service
- CI workflow for validation and image build
- README updated with setup steps
