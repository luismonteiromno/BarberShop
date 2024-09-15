FROM node:14 AS frontend

WORKDIR /app/front

COPY front/BarberShopFront/package.json front/BarberShopFront/package-lock.json ./front/
RUN npm install

COPY front/ ./
RUN npm build

EXPOSE 8080
