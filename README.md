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

## day 38 (Feb 07, 2019)
  Added few methods to my memcache and endpoint to flush out cache to db.

## day 39 (Feb 08, 2019)
  Initiated namma pollachi project.

## day 40 (Feb 09, 2019)
  Added a endpoint to my india elections project to dynamically map candidates or query terms with alliance.

## day 41 (Feb 10, 2019)
  Scraped of memcache from india elections as it would be a overkill.

## day 42 (Feb 11, 2019)
  Read some wagtail tutorial for my upcoming nammapollachi project which is a blog site.

## day 43 (Feb 12, 2019)
  Came up with some ideas for my 2016 project Autologout and opened issues in my Github repo.
Tried out Instagram streetart detection with machine learning.

## day 44 (Feb 13, 2019)
  Added a permission class to my india-elections project which enables the job to be run only
from the local machine.

## day 45 (Feb 14, 2019)
  Fixed a production error in my india elections project where db insert was getting timed out, due to which 500 was thrown.

## day 46 (Feb 15, 2019)
  Modified the code to show sentiment data in percentage for my india elections project.

## day 47 (Feb 16, 2019)
  Added terms and conditions page to my india-elections project.

## day 48 (Feb 17, 2019)
  Started redesign of my AutoLogout (chrome extension) UI.

## day 49 (Feb 18, 2019)
  Learnt about python itertools and it's application. Tried out some functions from itertools.

## day 50 (Feb 19, 2019)
  Completed design prototype of AutoLogout v2 version.

## day 51 (Feb 20, 2019)
  Added footer, updated navbar and linked tags to their wordcloud in my india-elections project.

## day 52 (Feb 21, 2019)
  Did some initial coding on showing remaining time left in my AutoLogout project.

## day 53 (Feb 22, 2019)
  Started refactoring of my india-elections project.
z  
## day 54 (Feb 23, 2019)  
  Project is getting bigger. So refactored generate view data method into 1. Previously it was duplicated into 2 methods one for generating india data and other for tn data with party names hardcoded. Now removed all hardcoded values and made the method generic and also fixed related test cases.

## day 55 (Feb 24, 2019)
  Added precommit hooks for flake8 check and added a management command to populate initial data for Alliance table to my india elections project.


## day 56 (Feb 25, 2019)
  Had two templates for rendering india and tamilnadu data. Refactored and converted to single template for my india-elections project.

## day 57 (Feb 26, 2019)
  Added opinion poll to my india elections project.

## day 58 (Feb 27, 2019)
  Modified opinion poll to show states and their corresponding constituencies.

## day 59 (Feb 28, 2019)
  Removed some unwanted code and made few optimizations in my india elections project.

## day 60 (March 01, 2019)
  Added sentiment timeseries plot for my india elections project. (my birthday :cake:)

## day 61 (March 02, 2019)
  Started UI redesign of india elections project.

## day 62 (March 03, 2019)
  Modified the code to use new design.

## day 63 (March 04, 2019)
  Brought the wordcloud page under new redesign

## day 64 (March 05, 2019)
  Came to know about statistics stdlib in python.

## day 65 (March 06, 2019)
  Read pycoders weakly newsletter. (issue 357.)

## day 66 (March 07, 2019)
  Wrote a python script to set a bing daily image as a wallpaper for my ubuntu.

## day 68 (March 08, 2019)
  Read about pathlib and os.path
  
## day 69 (March 09, 2019)
  Update the introduction content in my india elections project and added opinion poll in navbar menu.

## day 70 (March 10, 2019)
  Updated the backend code of india elections project. to filter tweetstats by today, yesterday, thisweek and all time.
  
## day 71 (March 11, 2019)
  Added the timerange filter to frontend. Now users can filter tweetstats by time from frontend.
  
## day 72 (March 12, 2019)
  Add some inference to win count prediction in both frontend and backend.
  
## day 73 (March 13, 2019)
  Officially completed india elections project. Added caching to views. Only bug fixes and no more daily development.

## day 74 (March 14, 2019)
  Tmp directory getting full in production of indiaelections. I have only 1 GB. So wrote a management command to clear tmp directory. It will be run as a cron job once everyday.

## day 75 (March 15, 2019)
  Read pycoders March 5, 2018 issue and tried some tutorial.

## day 76 (March 16, 2019)
  Added profile decorator to indiaelections to profile endpoints.

## day 77 (March 17, 2019)
  Added some twitter apis to get available trends in my india elections project.

## day 78 (March 18, 2019)
  Read pycoders March 12, 2018 issue.

## day 79 (March 19, 2019)
  Added a bot to daily tweet about prediction results.

## day 80 (March 20, 2019)
  Starting 30 days of Javascript challenge. 

## day 81 (March 21, 2019)
  Added a management command to bootstrap development environment for india elections.

## day 82 (March 22, 2019)
  Completed day 1 of JS 30 challenge.

## day 83 (March 23, 2019)
  Completed day 2 of JS 30 Challenge.

## day 84 (March 24, 2019)
  Added a helper to india election project to generate image with text.

## day 85 (March 25, 2019)
  Refactored job runner script in india elections project.

## day 86 (March 26, 2019)
  Completed day 3 of JS 30 Challenge.

## day 87 (March 27, 2019)
  Refined job access permission check in india-elections project.

## day 88 (March 28, 2019)
  Completed day 4 of JS 30 Challenge.

## day 89 (March 29, 2019)
  Completed day 5 of JS 30 Challenge.

## day 90 (March 30, 2019)
  Learnt about threading in python from pycoder's newsletter.

## day 91 (March 31, 2019)
  Added a python script to convert a day to timestamp relative to today.

## day 92 (April 1, 2019)
  Completed day 6 of JS 30 Challenge.

## day 93 (April 2, 2019)
  Completed day 7 of JS 30 Challenge.

## day 94 (April 3, 2019)
  Completed day 8 of JS 30 Challenge.

## day 95 (April 4, 2019)
  Completed day 9 of JS 30 Challenge.

## day 96 (April 5, 2019)
  Learnt about strategy pattern in python.

## day 97 (April 6, 2019)
  Completed day 10 of JS 30 Challenge.

## day 98 (April 7, 2019)
  Started another project unspam. The goal is to clean gmail inbox periodically by automatically unsubscribing from non important/promotion/spam mails.

## day 99 (April 8, 2019)
  Started day 11 of JS 30 Challenge.

## day 100 (April 9, 2019)
  Completed day 11 of JS 30 Challenge.

## day 100 (April 10, 2019)
  Completed day 12 of JS 30 Challenge.

## day 101 (April 11, 2019)
  Completed day 13 of JS 30 Challenge.

## day 102 (April 12, 2019)
  Completed day 14 of JS 30 Challenge.

## day 103 (April 13, 2019)
  Wrote a test wrapper for rest framework serializers wherein serializer and data is enough to run validations for a serializer

## day 104 (April 14, 2019)
  Coded a integration test wrapper for django rest framework, where just valid and invalid data is enough
  to test a viewset.

## day 105 (April 15, 2019)
  Completed day 15 of JS 30 Challenge.

## day 106 (April 16, 2019)
  Modified my python script to organize movies based on language.

## day 107 (April 17, 2019)
  Completed day 16 of JS 30 challenge.

## day 108 (April 18, 2019)
  Added windows support for reddit daily wallpaper setter.
  
## day 109 (April 19, 2019)
  Read pycoder newsletter.

## day 110 (April 20, 2019)
  Started with day 17 of JS 30 challenge.

## day 111 (April 21, 2019)
  Completed JS 30 day 17.

## day 112 (April 22, 2019)
  Fixed a bug in android ticketing app where the application was crashing when trying to connect with bluetooth printer.

## day 113 (April 23, 2019)
  Added check or request permissions to android ticketing app.

## day 114 (April 24, 2019)
  Show toast message when vehicle number is empty or less than 4 characters. Bump gradle to latest version and use jdk 8 in ticketing app.

## day 115 (April 25, 2019)
  Improved error messages and optimized connecting with bluetooth printer for ticketing app.

## day 116 (April 26, 2019)
  Added a flag to check and connect with printer, if not connected for my ticketing app. (ordered a macbook :smile: )

## day 117 (April 27, 2019)
  Added a alert to ask for confirmation before opening shift in android ticketing app.

## day 118 (April 28, 2019)
  Do not close ticket again, if it already closed (ticketing app).

## day 119 (April 29, 2019)
  Added a context menu to close ticket from vehicle search activity.

## day 120 (April 30, 2019)
  Modified close ticket function to process close using either token number or using table primary key (ticketing app).

## day 121 (May 1, 2019)
  Started refactoring of ticketing app. Moved hardcoded strings to strings.xml for easy i18n, refactored db util and used common functions
  for creating progress dialog and showing toast.

## day 122 (May 2, 2019)
  Moved print ticket and connect printer to async task. Used a common function to create and show alert dialog.

## day 123 (May 3, 2019)
  Move worker thread, that listens for data to async task and refactored connect printer method.

## day 124 (May 4, 2019)
  Completed refactoring by refactoring generateTicket method, SearchActivity and SummaryActivity.

## day 125 (May 5, 2019)
  Modified code to save token entry to db, only when ticket printing is success.

## day 126 (May 6, 2019)
  Added a new launcher icon and changed a toast message in search activity.

## day 127 (May 7, 2019)
  Added tamil translation and moved some missed hardcoded strings to strings.xml

## day 128 (May 8, 2019)
  Started with unit testing for ticketing app. Learnt about android unit testing and wrote unit tests.

## day 129 (May 9, 2019)
  Completed unit tests for DBHelper class in ticketing app.

## day 130 (May 10, 2019)
  Added unit tests for Extensions in ticketing app.

## day 131 (May 11, 2019)
  Added integration tests for SearchActivity.

## day 132 (May 12, 2019)
  Added integration tests for PinActivity.

## day 133 (May 13, 2019)
  Read pycoders newsletter and tried some new stuff.

## day 134 (May 14, 2019)
  Started with UI redesign of my ticketing app.

## day 135 (May 15, 2019)
  Refactored Shift activity and added unit tests.

## day 136 (May 16, 2019)
  Changed UX and added new font in ticketing app.
