FROM selenium/standalone-chrome:latest

## Install latest stable Chrome
## https://gerg.dev/2021/06/making-chromedriver-and-chrome-versions-match-in-a-docker-image/
#RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | \
#    tee -a /etc/apt/sources.list.d/google.list && \
#    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | \
#    apt-key add - && \
#    apt-get update && \
#    apt-get install -y google-chrome-stable libxss1
#
## Install the Chromedriver version that corresponds to the installed major Chrome version
## https://blogs.sap.com/2020/12/01/ui5-testing-how-to-handle-chromedriver-update-in-docker-image/
#RUN google-chrome --version | grep -oE "[0-9]{1,10}.[0-9]{1,10}.[0-9]{1,10}" > /tmp/chromebrowser-main-version.txt
#RUN wget --no-verbose -O /tmp/latest_chromedriver_version.txt https://chromedriver.storage.googleapis.com/LATEST_RELEASE
#RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$(cat /tmp/latest_chromedriver_version.txt)/chromedriver_linux64.zip && rm -rf /opt/selenium/chromedriver && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium && rm /tmp/chromedriver_linux64.zip && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$(cat /tmp/latest_chromedriver_version.txt) && chmod 755 /opt/selenium/chromedriver-$(cat /tmp/latest_chromedriver_version.txt) && ln -fs /opt/selenium/chromedriver-$(cat /tmp/latest_chromedriver_version.txt) /usr/bin/chromedriver

RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
RUN sudo apt-get install -y nodejs


# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./
#RUN npm ci

# Bundle app source
COPY . .

#RUN npm install -g mocha --silent
#RUN npm install chai webdriverio --silent
RUN npm run test
