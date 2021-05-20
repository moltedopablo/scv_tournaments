FROM node:10
WORKDIR /usr/src/app/scv_tournaments
COPY package*.json ./
ENV NODE_ENV=development
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm", "run", "serve"]
