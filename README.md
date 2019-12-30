# 365  Days of code

## Todo projects list

- [ ] Simple snake game in python without any external lib
- [ ] Chrome extension using localstorage to highlight stuff.

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

## day 137 (May 17, 2019)
  Added mechanism to prevent clearing app data.

## day 138 (May 18, 2019)
  Added functionality to log number of incorrect password attempts.

## day 139 (May 19, 2019)
  Added support to change manage password in ticketing app.

## day 140 (May 20, 2019)
  Show ticket details, whem closing ticket.

## day 141 (May 21, 2019)
  Show payment due, when closing ticket.

## day 142 (May 22, 2019)
  Added manage menu to backup data to file and email in ticketing app.

## day 143 (May 23, 2019)
  Show overstay count in manage summary.

## day 144 (May 24, 2019)
  Completed day 18 of Javascript 30.

## day 145 (May 25, 2019)
  Completed day 19 of Javascript 30.

## day 146 (May 26, 2019)
  Changed some ouput ticket data in ticketing app.

## day 147 (May 27, 2019)
  Completed day 20 of Javascript 30.

## day 148 (May 28, 2019)
  Completed day 21 of Javascript 30.

## day 149 (May 29, 2019)
  Started with edge detection for my document scanner app.

## day 150 (May 30, 2019)
  Made some progress in document detection. Have to improve.

## day 151 (May 31, 2019)
  Finally stablized the document detection algorithm for ticketing app.

## day 152 (June 01, 2019)
  Completed day 22 of Javascript 30

## day 153 (June 02, 2019)
  Completed day 23 of Javascript 30.

## day 154 (June 03, 2019)
  Successfully completed adding document detection to scan2pdf.

## day 155 (June 04, 2019)
  Read pycoders tutorial. #May last week issue

## day 156 (June 05, 2019)
  Learnt about django templates, static files rendering.

## day 157 (June 06, 2019)
  Got to know about django print sql and tracing sql queries.

## day 158 (June 07, 2019)
  Started to learn about *args in python.

## day 159 (June 08, 2019)
  Learnt about **kwargs in python.

## day 160 (June 09, 2019)
  Complete day 24 of Javascript 30.

## day 161 (June 10, 2019)
  Complete day 25 of Javascript 30.

## day 162 (June 11, 2019)
  Started a new Django project to support android ticketing app.

## day 163 (June 12, 2019)
  Added token model and dummy post save signal to print token.

## day 164 (June 13, 2019)
  Show overstay details if out time is entered for a token.

## day 165 (June 14, 2019)
  Add base printer setup code for ticket web.

## day 166 (June 15, 2019)
  Add delete permission only for super user, use presave signal to prevent adding out time second time.

## day 167 (June 16, 2019)
  Added README.md for ticket-web.

## day 168 (June 17, 2019)
  Add Shift model in ticket-web.

## day 169 (June 18, 2019)
  Add summary action to print shift summary.

## day 170 (June 19, 2019)
  Integrated win32api in ticket-web project.

## day 171 (June 20, 2019)
  Move printing to background job in windows in local machine using sqlalchemy.

## day 172 (June 21, 2019)
  Add admin action to download shift data as csv.

## day 173 (June 22, 2019)
  Add tamil translation to ticket-web.

## day 174 (June 23, 2019)
  Add admin action to print today's shift data.

## day 175 (June 24, 2019)
  Complete JS 30 - day 26.

## day 176 (June 25, 2019)
  Add account model to ticket web.

## day 177 (June 26, 2019)
  Changed account model and linked with token model.

## day 178 (June 27, 2019)
  send sms whenever a token is created.

## day 179 (June 28, 2019)
  Add OverstayTokens model.

## day 180 (June 29, 2019)
  Added mysql support for ticket web.

## day 181 (June 30, 2019)
  Send sms using msg 91 api and other minor changes.

## day 182 - 186 (July 01, 2019 - July 04, 2019)
  Some changes to ticket-web.

## day 187 (July 05, 2019)
  Complete JS 30 day 27.

## day 188 (July 06, 2019)
  Complete JS 30 day 28.

## day 189 (July 07, 2019)
  Learnt some css stuff from medium.

## day 190 - 193 (July 08, 2019 - July 11, 2019)
  Worked on a twitter bot.

## day 194 (July 12, 2019)
  Complete JS 30 day 29.

## day 195 (July 13, 2019)
  Learnt some css.

## day 196 (July 14, 2019)
  Completed JS 30 day 30.

## day 197 (July 15, 2019)
  Learnt about command pattern in python.

## day 198 (July 16, 2019)
  Learnt about singleton pattern in python.

## day 199 (July 17, 2019)
  Learnt about creational patterns in GOF in general.

## day 200 (July 18, 2019)
  Learnt about facade pattern.

## day 201 (July 19, 2019)
  Started dev work for retro snake game in python.

## day 202 (July 20, 2019)
  Use arrow keys to move snake and eat food.

## day 203 (July 21, 2019)
  Show score board in snake game.

## day 204 (July 22, 2019)
  Add edge detection to snake game.

## day 205 (July 23, 2019)
  Add auto move functionality to snake game.

## day 206 (July 24, 2019)
  Add best score to snake game.

## day 207 (July 25, 2019)
  Read pycoder newsletter.

## day 208 (July 26, 2019)
  Started with snake size increasing based on score for snake game.

## day 209, 210 (July 27,28 2019)
  Work on snake size

## day 211-213 (July 29-31, 2019)
  Read some tutorials on good coding practices.

## day 214 (August 01, 2019)
  Tried a sample django docker app with nginx config.

## day 215 (August 02, 2019)
  Tried a sample flask SQLAlchemy crud app.

## day 216 (August 03, 2019)
  Read pycoder's tutorial.

## day 217 (August 04, 2019)
  Checked out the source code of grid studio PYTHON.

## day 218 (August 05, 2019)
  Started working on highlight chrome extension.

## day 219 (August 06, 2019)
  Highlight-save selection to localstorage.

## day 220, 221 (August 07,08 2019)
  Revisited itertools of python.

## day 222 (August 09, 2019)
  Add selected word to existing saved content of current page.

## day 223 (August 10, 2019)
  Reused some code from word-highlighter github extension for my highlight chrome extension.

## day 224 (August 11, 2019)
  Read about quopri, binascii and base64 libraries in python.
  
## day 225 (August 12, 2019)
  Started with unspam project. Added base gmail api wrapper.

## day 226 (August 13, 2019)
  Unspam, add gmail api.

## day 227, 228 (August 14, 15, 2019)
  Learn about stack and queues.
  
## day 229 (August 16, 2019)
  Read pycoders newsletter.
  
## day 230, 231 (August 17, 18 2019)
  Read about bit manipulation.

## day 232 (August 19, 2019)
  Refactored scan2pdf android app.
  
## day 233 (August 20, 2019)
  Add runtime permission check for Scan2Pdf app.

## day 234 (August 21, 2019)
  Bugfix - Scan2Pdf - Correct document outline to fall inside image.

## day 235 (August 22, 2019)
  Drag and crop functionality added to Scan2Pdf.

## day 236 (August 23, 2019)
  Bugfix: Save pdf crash and also add cropped image to images list (Scan2Pdf)
  
## day 237 (August 24, 2019)
  Added menu to choose new scan either from camera or gallery.
 
## day 238 (August 25, 2019)
  Fix merge conflict and review the pick image and manual crop code.

## day 239 (August 26, 2019)
  Show all pdf files created using the app in MainActivity.

## day 240 (August 27, 2019)
  Fix app crash when clicking file in MainActivity (Scan2Pdf)

## day 241 (August 28, 2019)
  Add base context menu to pdf list.
  
## day 242 (August 29, 2019)
  Added rename file functionality to scanned files.

## day 243 (August 30, 2019)
  Add minor change to not show crop view when image is cropped.

## day 244 (August 31, 2019)
  Read some pycoder newsletter.

## day 245 (September 01, 2019)
  Viewed and read some source code of requests python lib.

## day 246 (September 02, 2019)
  Optimized rename media files code.

## day 247 (September 03, 2019)
  Made some minor changes to snake game.

## day 248 (September 04, 2019)
  Optimized crop image code.
  
## day 249 (September 05, 2019)
  Added exception handling to document detection code and disable crop button in
  case of exception.
  
## day 250 (September 06, 2019)
  Complete login flow of sma android.
  
## day 251 (September 07, 2019)
  Add splash screen to sma android.
  
## day 252 (September 08, 2019)
  Complete dashboard menu.

## day 253 (September 09, 2019)
  Complete attendance mock.
  
## day 254 (September 10, 2019)
  Complete messages mock.

## day 255 (September 11, 2019)
  Changed login screen design and font.

## day 256 (September 12, 2019)
  Added some options ot nav drawer.

## day 257 (September 13, 2019)
  Read pycoder newsletter.
  
## day 258 (September 14, 2019)
  Add share context menu option in Scan2Pdf app.
  
## day 259 (September 15, 2019)
  Optimize image scaling during pdf creation in Scan2Pdf.
  
## day 260 (September 16, 2019)
  Add delete context menu option in Scan2Pdf.

## day 261 (September 17, 2019)
  Read pycoder newsletter
  
## day 262 (September 18, 2019)
  Worked on python itertools.

## day 263 (September 19, 2019)
  Read source code of Flask python.

## day 264 (September 20, 2019)
  Checked out 30 seconds of python github repo.

## day 265 (September 21, 2019)
  Brushed up some react.

## day 266 (September 22, 2019)
  Brushed up some react native.

## day 267 (September 23, 2019)
  Learnt about jetpack compose.

## day 268 (September 24, 2019)
  Learnt about memory management in python.

## day 269 (September 25, 2019)
  Fixed a bug in scan2pdf.

## day 270 (September 26, 2019)
  Optimized pdf deletion logic.

## day 271 (September 27, 2019)
  Remove context menu if no scans are present.

## day 272 (September 28, 2019)
  Add graph adjacency lists.
  
## day 273 (September 29, 2019)
  Add graph bfs, dfs
  
## day 274 (September 30, 2019)
  Add topological sort.

## day 275 (October 1, 2019)
  Add simple voting bot.

## day 276 (October 2, 2019)
  Read pycoders news letter.

## day 277 (October 3, 2019)
  Learn about generators in python.

## day 278 (October 4, 2019)
  Read about preventing sql injection in python.

## day 279 (October 5, 2019)
  StringIO vs BytesIO python.

## day 280 (October 6, 2019)
  Multiprocessing vs threading in python.

## day 281 (October 7, 2019)
  Learn about typing module in python.

## day 282 (October 8, 2019)
  Python url slugify different approaches (https://www.peterbe.com/plog/fastest-python-function-to-slugify-a-string)

## day 283 (October 9, 2019)
  Try out some pandas lib (https://www.dataschool.io/python-pandas-tips-and-tricks/)

## day 284 (October 10, 2019)
  Learn about python zip builtin
  
## day 285 (October 11, 2019)
  Add watermark support for Scan2Pdf.

## day 286  (October 12, 2019)
  Minor optimization in india-elections
  
## day 287 (October 13, 2019)
  Add readme in snake game

## day 288 (October 14, 2019)
  Learn about unittest module python.

## day 289 (October 15, 2019)
  Learn about mock module in python.

## day 290 (October 16, 2019)
  Read pycoders news letter.

## day 291 (October 17, 2019)
  Learn about pydoc and doc test module in python.

## day 292 (October 18, 2019)
  Complete 30 days of react - day 1

## day 293 (October 19, 2019)
  Learn about JSX - day 2 of 30 days of react.

## day 294 (October 20, 2019)
  Complete 30 days of react - day 3

## day 295 (October 21, 2019)
  Complete 30 days of react - day 4.

## day 296 (October 22, 2019)
  Complete 30 days of react - day 5.

## day 297 - day 331 (October 23, 2019 - November 27, 2019)
  Read various tutorials, python stand library docs.

## day 332 (November 28, 2019)
  Complete 30 days of react - day 6.

## day 333 (November 29, 2019)
  Complete 30 days of react - day 7.

## day 334 (November 30, 2019)
  Complete 30 days of react - day 8.

## day 335 (December 01, 2019)
  Complete 30 days of react - day 9.

## day 336 (December 02, 2019)
  Complete 30 days of react - day 10.

## day 337 (December 03, 2019)
  Complete 30 days of react - day 11.
  
## day 338 (December 04, 2019)
  Complete 30 days of react - day 12.

## day 339 (December 05, 2019)
  Complete 30 days of react - day 13.

## day 340 (December 06, 2019)
  Complete 30 days of react - day 14.

## day 341 (December 07, 2019)
  Complete 30 days of react - day 15.

## day 342 (December 08, 2019)
  Complete 30 days of react - day 16.

## day 343 (December 09, 2019)
  Complete 30 days of react - day 17.

## day 344 (December 10, 2019)
  Complete 30 days of react - day 18.

## day 345 (December 11, 2019)
  Complete 30 days of react - day 19.

## day 346 (December 12, 2019)
  Complete 30 days of react - day 20.

## day 347 (December 13, 2019)
  Complete 30 days of react - day 21.

## day 348 (December 14, 2019)
  Complete 30 days of react - day 22.

## day 349 (December 15, 2019)
  Complete 30 days of react - day 23.

## day 350 (December 16, 2019)
  Complete 30 days of react - day 24.

## day 351 (December 17, 2019)
  Complete 30 days of react - day 25.

## day 352 (December 18, 2019)
  Complete 30 days of react - day 26.

## day 353 (December 19, 2019)
  Complete 30 days of react - day 27.

## day 354 (December 20, 2019)
  Complete 30 days of react - day 28.

## day 355 (December 21, 2019)
  Complete 30 days of react - day 29.

## day 356 (December 22, 2019)
  Complete 30 days of react - day 30.

## day 357 (December 23, 2019)
  Read pycoders weekly newsletter.

## day 358 (December 24, 2019)
  Spell checker implementation in python.

## day 359 (December 25, 2019)
  Merge MP3 android app add a function to extract file path from uri.

## day 360 (December 26, 2019)
  Added file explorer in merge mp3 app to choose files.

## day 361 (December 27, 2019)
  Completed initial version of merge android mp3 app.

## day 362 (December 28, 2019)
  Fixed a bug in mp3 merge android app.

## day 363 (December 29, 2019)
  Revamped UI and added Recent Files section to merge mp3 android app.

## day 364 (December 24, 2019)
  Show files chosen during merge activity.
