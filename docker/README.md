# Backend

1. Go to parent directory
2. `podman build --tag quiz -f docker/backend/Dockerfile .`
3. `podman volume create quiz`
4. `podman run --name quizbackend --rm -v quiz:/data/ -p8080:8000 quiz`
