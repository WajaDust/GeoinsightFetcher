# GeoinsightFetcher
GeoinsightFetcher test task gor Madgicx com.

Project requirements: python>3.6, pip3

Running script requirements:
1) Pull project from git
   
    $ mkdir geoinsight_fetcher
   
    $ cd geoinsight_fetcher

    $ git init

    $ git remote add origin https://github.com/WajaDust/GeoinsightFetcher.git

    $ git pull origin master


2) Create virtualenv:

    $ pip3 install virtualenv
   
    $ virtualenv venv --python=python3.6

    $ source venv/bin/activate


3) Install project requirements:
   
   pip3 install -r requirements.txt


4) Run help command to see commands explanation:
   
   python madgicx_geo.py --help


Build project from scratch:
1) Create project:
   
    $ mkdir geoinsight_fetcher
   
    $ cd geoinsight_fetcher
   
    
2) Create virtualenv:

    $ pip3 install virtualenv
   
    $ virtualenv venv --python=python3.6

    $ source venv/bin/activate
   

3) Create needed basic files:
   
   requirements.txt
   .gitignore
   readme.md
   

4) Create main execute file and subfolders:
   
   madgicx_geo.py, api, common

