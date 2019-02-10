# 365  Days of code

## Jan 1, 2019
  *I am publicly committing to 365 days of code. Everyday I will code for atleast one hour or learn some new stuff related to coding and log my progress here.*
  
## day 1 (Jan 1, 2019)
. Lets see how this turns out. Today I converted poc my [india-elections](<https://github.com/v-adhithyan/india-elections>) project to load some dynamic data.

## day 2 (Jan 2, 2019)
  Fixed a bug in my [india-elections](<https://github.com/v-adhithyan/india-elections>) where cleaned tweet was not used to generate word cloud.
  
## day 3 (Jan 3, 2019)
  Added sentry integration to my [india-elections](<https://github.com/v-adhithyan/india-elections>) where cleaned tweet was not used to generate word cloud, and fixed
  environment variable import error in production.
  
## day 4 (Jan 4, 2019)
  Fixed a simple bug in my [india-elections](<https://github.com/v-adhithyan/india-elections>) project to add allowed hosts, where in the app was not loading
  in production.
  
## day 5 (Jan 5, 2019)
  Optimized my [india-elections](<https://github.com/v-adhithyan/india-elections>) project, so that
  instead of generating wordcloud for a same query again and again, on first generation
  the file path will be saved in db and on subsequent calls to same query the file
  will be served from already generated one.
  
## day 6 (Jan 6, 2019)
  Modified clean tweet function for my [india-elections](<https://github.com/v-adhithyan/india-elections>) to exclude
  retweets from visualizations. Also the complexity is coming up
  a way to not store tweets but also it should not hinder visualizations.
  
## day 7 (Jan 7, 2019)
  Read 2 python related tutorials. <https://www.pingshiuanchua.com/blog/post/2018-trending-english-searches-on-google-us-uk-in-sg-my-ph-google-trends> <https://realpython.com/python-string-formatting/>
  
## day 8 (Jan 8, 2019)
  Read a white paper regarding analysing sentiments from tweets to predict election results.

## day 9 (Jan 9, 2019)
  Studied about building dashboards with python. <https://pusher.com/tutorials/live-dashboard-python> <https://blog.sicara.com/bokeh-dash-best-dashboard-framework-python-shiny-alternative-c5b576375f7f?gi=bb613743bcf1> I think this will be useful for my india elections project. After finalising v1 of project, have to come up with dashboard.
  
## day 10 (Jan 10, 2019)
  Mostly into reading pycoder issue 350 and trying out some stuff from tutorial.

## day 11 (Jan 11, 2019)
  Added contour detection to my android app. I am trying to reverse engineer Camscanner app. This was started long back. Switching to it for fresh breath of air. Only for today.

## day 12 (Jan 12, 2019)
  Coded a simple python script to rename media files.
  
## day 13 (Jan 13, 2019)
  Changed db model to not store tweets. Now only search term and corresponding count will be stored in db.
  
## day 14 (Jan 14, 2019)
  Fixed a bug in my india elections project from sentry.
  
## day 15 (Jan 15, 2019)
  Fixed a bug in day 12 python script where colors were improperly named.
  
## day 16 (Jan 16, 2019)
  Made an enhancement in day 12 python script to include directories also while renaming.
  
## day 17 (Jan 17, 2019)
  For my india elections project, I need gender of twitter users.Since twitter api does not
  provide gender data, I thought of predicting gender names from twitter names.
  Since my project focusses only on india and there is no good open source library to
  predict gender from indian names, forked a gender guessor python
  library and modified to predict gender from indian names.
  Repo link: <https://github.com/v-adhithyan/gender-guesser-indian> 
  
 ## day 18 (Jan 18, 2019)
  Refreshed machine learning basics from this tutorial <https://www.pyimagesearch.com/2019/01/14/machine-learning-in-python/> and tried them.
 
 ## day 19 (Jan 19, 2019)
  I was not satisfied with the forked repo. So started from scratcha and completed v1 version of gender predictor. https://github.com/v-adhithyan/gender-guess-indiannames/commit/ab7d033ff4907e7b084e08332a9aad0b919765f9
  
 ## day 20 (Jan 20, 2019)
  Improved accuracy of gender predictor to 88% from 78% https://github.com/v-adhithyan/gender-guess-indiannames/commit/d98f642ce751cedc15165ab76a3a8c25c46738ea.
  
## day 21 (Jan 21, 2019)
  Modified gender predictor to upload to pypi. The package is live at https://pypi.org/project/guess-indian-gender/

## day 22 (Jan 22, 2019)
  Integrated my library gender-guess-indian with my india elections project and added
  columns male and female to my database model.

## day 23 (Jan 23, 2019)
  Added gender chart to front end of india elections dashboard.

## day 24 (Jan 24, 2019)
  Modified frontend code to show charts in seperate cards for my india elections dashboard. 
  
## day 25 (Jan 25, 2019)
  Fixed a bug in my indiaelections <https://github.com/v-adhithyan/india-elections> project where party and candidates were mapped to wrong alliance.

## day 26 (Jan 26, 2019)
  Added unit tests to my india elections project to improve coverage <https://github.com/v-adhithyan/india-elections>

## day 27 (Jan 27, 2019)
  Added a new column in core model Tweetstats to associate party. Also, Optimized some util functions. These changes were performed to accomodate timeseries tweet plot change.

## day 28 (Jan 28, 2019)
  Modified the frontend to show timeseries plot.
  
## day 29 (Jan 29, 2019)
  Took a break from my india elections project. Read pycoders issue 352 and tried out some stuff. Also read about django cms for my upcoming project after india elections. <https://www.accordbox.com/blog/wagtail-tutorials/> <http://mezzanine.jupo.org>
  
## day 30 (Jan 30, 2019)
  Fixed a bug in my india elections <https://github.com/v-adhithyan/india-elections> where alliance was not getting associated with new tweets.
  
## day 31 (Jan 31, 2019)
  Added unittests to cover timeseries change for my india elections project. <https://github.com/v-adhithyan/india-elections>. Merged this branch with master.
  
## day 32 (Feb 01, 2019)
  Performed a self review of timeseries change and merged with master.

## day 33 (Feb 02, 2019)
  Fixed a memory leak bug in indiaelections project. This bug caused 500 error. The bug was due to matplot open frames which keeps references to all plots created using matplot untill explicitly closed.
  
## day 34 (Feb 03, 2019)
  Modified india elections <https://github.com/v-adhithyan/india-elections> to use mysql in production. Will continue to use sqlite for testing and development.

## day  35 (Feb 04, 2019)
  Added a memcache wrapper to store today's tweet stats in cache. Tried to setup in pythonanywhere, due to user restrictions was unable to install memcache in pythonanywhere.

## day 36 (Feb 05, 2019)
  Setup memcachier in production for india elections project.
  
## day 37 (Feb 06, 2019)
  Took a break from coding project and read pycoder weakly newsletter and tried stuff..
  
## day 37 (Feb 07, 2019)
  Added few methods to my memcache and endpoint to flush out cache to db.
    
## day 37 (Feb 08, 2019)
  Initiated namma pollachi project.
      
## day 37 (Feb 09, 2019)
  Added a endpoint to my india elections project to dynamically map candidates or query terms with alliance.
        
## day 37 (Feb 10, 2019)
  Scraped of memcache from india elections as it would be a overkill.