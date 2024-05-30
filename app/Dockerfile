FROM node:22.0.0-alpine3.18

WORKDIR /app/frontend/

COPY package*.json /app/frontend/

RUN npm ci

COPY . /app/frontend/

RUN npm run build

RUN npm install -g next

EXPOSE 3000

CMD [ "npm", "run", "dev"]
