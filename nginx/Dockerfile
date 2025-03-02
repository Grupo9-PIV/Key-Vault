FROM node:23-alpine AS builder

WORKDIR /app

COPY frontend/package.json frontend/yarn.lock ./

RUN yarn install --frozen-lockfile

COPY frontend/ . 

RUN yarn build

FROM nginx:alpine

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
