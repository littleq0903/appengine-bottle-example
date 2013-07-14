<img src="" alt="google app engine with bottle">

appengine-bottle-example
========================

Example for quickly bootstrapping a Google App Engine project with Bottle Python web framework.

## Preliminaries

You need to install Google App Engine SDK in your computer, and make sure it is already in your `PATH` variable.

### Mac

1. Download [Google App Engine SDK for Mac](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python) and install it.
1. Launch the `/Applications/GoogleAppEngineLauncher.app` first time for extracting the SDK into your system
1. Put `/usr/local/google_appengine` into your `PATH`. (You can set it in your `~/.profile`)

### Linux

1. Download [Google App Engine SDK for Linux](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
2. Extract it and put `google_appengine` in wherever you like (For example, I put it in `~/opt`)
3. Add `/path/to/google_appengine` into `PATH`. (In my case, it's `~/opt/google_appengine`)


#### HOW DO I KNOW I AM DOING IT RIGHT?
	
Open your terminal, and just type `dev_appserver`, if it didn't show `Command not found` but the manual of that command, than you're doing it right ;)

