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
  Completed v1 version of gender predictor. https://www.pyimagesearch.com/2019/01/14/machine-learning-in-python/
  
 ## day 20 (Jan 20, 2019)
  Improved accuracy of gender predictor to 88% from 78% https://github.com/v-adhithyan/gender-guess-indiannames/commit/d98f642ce751cedc15165ab76a3a8c25c46738ea.