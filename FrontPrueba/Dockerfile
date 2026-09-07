FROM node:20-slim

WORKDIR /app

COPY package.json .
COPY src .
COPY index.html .
COPY vite.config.js .

RUN npm install --include=optional

CMD ["npm", "run", "dev", "--", "--host"]