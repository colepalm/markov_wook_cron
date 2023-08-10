FROM --platform=linux/amd64 node
RUN apt update
RUN apt -y install build-essential
RUN apt -y install wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable



# COPY --from=CHORMEBUILDER /usr/bin/google-chrome-stable /usr/bin/google-chrome-stable
# Create app directory
COPY $PWD /crm-connector
WORKDIR /crm-connector

# RUN npm install --location=global npm@8.12.1
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./
RUN node -v
RUN npm uninstall chromedriver
RUN npm install
RUN npm install chromedriver --chromedriver-force-download --detect_chromedriver_version
# If you are building your code for production
#RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8081
RUN npm run test
