# Backend

1. Go to parent directory
2. `podman build --tag quiz -f docker/backend/Dockerfile .`


## Test

1. `podman volume create quiz`
2. `podman run --name quizbackend --rm -v quiz:/data/ -p8080:8000 quiz`
