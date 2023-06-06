FROM node:16
WORKDIR /code
COPY package*.json ./
RUN npm install
COPY . ./
EXPOSE 4000
CMD ["npm", "run", "start"]