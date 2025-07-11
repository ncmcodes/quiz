# Backend

1. Go to parent directory
2. `podman build --tag quizback:latest -f docker/backend/Dockerfile .`
3. `podman volume create quiz`
4. `podman run --rm -it -v quiz:/data/ -p8080:8000 --name quizbackend quizback:latest`

# Frontend

1. Go to parent directory
2. `podman build --tag quizfront:latest -f docker/frontend/Dockerfile .`
3. `podman run --rm -it -p3000:3000 --name quizfrontend quizfront:latest`

---

# TESTS

```bash
# Build
podman build --tag quizback:latest -f docker/backend/Dockerfile .
podman build --tag quizfront:latest -f docker/frontend/Dockerfile .

# Run
COMPOSE_FILE=docker/docker-compose.yaml podman-compose up --force-recreate
```
