# weatherlogr
A weather logging system for Twitter, logs every hour.

twitter.com/weatherlogr

cammarata.info/services/weatherlogr

# setup
index.html is the homepage source, and has nothing to do with the service, besides a website. init.py is the file you want to download and have ready to be used.

You need to install python-tweepy, json, and urllib2. All setup instructions are based on CentOS 6.7 minimal but should easily work with other distros of GNU/Linux.

```
# sudo yum install python-pip
# pip install tweepy
```

You have two options as to running this.

Having it run on boot.
```
# vi /etc/rc.d/rc.local
---------------------
python /path_to_file/init.py
```

Simply running it.
```
python /path_to_file/init.py
```

You'll also need to register a Twitter account for the logs, and signup for the API, which should take a few minutes. Then signup for the Wunderground API. Once you did this, you just have to go into the init.py script and change the API key variables accordingly.

# license
read the LICENSE file. do whatever the fuck you want.
