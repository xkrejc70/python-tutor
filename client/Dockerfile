FROM node:16-alpine
WORKDIR /app

COPY package.json ./
RUN npm install
COPY . .

EXPOSE 8501
CMD ["npm", "start"]