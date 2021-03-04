### STAGE 1: Build ###
FROM node:14.15.4-alpine AS build
WORKDIR /src/app
COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install -g @angular/cli@11.0.6
COPY . .
RUN npm run build

### STAGE 2: Run ###
#COPY default.conf /etc/nginx/conf.d/default.conf
#COPY --from=build /usr/src/app/dist/ /usr/share/nginx/html
EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]
