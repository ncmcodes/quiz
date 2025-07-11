# TODO: Muli stage build with a standalone output
# https://github.com/vercel/next.js/blob/canary/examples/with-docker/Dockerfile
# https://nextjs.org/docs/pages/api-reference/config/next-config-js/output
# Should allow us to run: node server.js

FROM node:18-alpine

# Install dependencies
WORKDIR /app
COPY frontend/*.json frontend/*.mjs /app
RUN npm install --include=dev

# Now copy code
COPY docker/frontend/docker-entrypoint /app
COPY frontend/src /app/src
COPY frontend/public /app/public

ENTRYPOINT ["/app/docker-entrypoint"]
