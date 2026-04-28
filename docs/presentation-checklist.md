# DS2 Presentation Checklist

Use this checklist during the oral presentation and for Blackboard proof files.

## 1. Local Docker demonstration

Run:

```bash
docker compose up --build
```

Take a screenshot showing:

- the image build
- the container startup
- the service listening without errors

## 2. Website proof

Open:

- `http://localhost:8080`
- `http://localhost:8080/contact.html`

Take screenshots of:

- the homepage
- the contact page
- the success message after submitting the form

## 3. Container proof

Run:

```bash
docker ps
```

Take a screenshot showing the running `student-hub-web` container.

## 4. GitHub Actions proof

Open the repository Actions tab and capture:

- one successful workflow run
- the workflow steps

If no run appears yet:

1. enable GitHub Actions for the repository
2. push a small commit
3. wait for the workflow to finish

## 5. GitHub branch protection proof

Open the branch protection settings for `main` and show:

- protected `main` branch
- required status checks before merge

## 6. Slides to include

The slides should contain:

- final Docker architecture
- explanation of `docker-compose.yml`
- GitHub Actions screenshots
- `docker ps` screenshot
- short explanation of the Dockerfile and CI pipeline
