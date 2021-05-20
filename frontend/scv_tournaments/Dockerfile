FROM node:10
WORKDIR /usr/src/app/scv_tournaments
COPY package*.json ./
RUN npm install
RUN npm install @vue/cli@4.5.13 -g
EXPOSE 8080
CMD ["npm", "run", "serve"]