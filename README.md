Software:
1. Fix the upper/lower case mismatch
2. < br >
3. The problem of Mr and Mr..
3. Add Easter eggs, bible verses, and other things. Especially one quote from my novel-to-write.
4. Configure the gui

So now I basically have every 10 minute covered by at least one quote.

Hardware:
1. Purchase a raspberry pi or whatever with the same functionality
2. Get a touchscreen


Update 19 Oct:
After an intense study of available devices, I finally decided to use Raspberry Pi 3 A+ and a touchscreen to implement the literature clock. They cost around 100 usd in total. The budget is 200 usd so I can still afford some extra accessories and the international shipping fee. It is very slow to get electronic devices shipped to Singapore from abroad so I chose a local supplier, which would still take me 1-3 days. Hope I can make it ASAP. In fact, I am thinking of extending the project to include other cool stuff that could bring surprises my Ni. My eyes are opened!
In the mean-time I could continue modifying the softwares.

# literature-clock
Clock using time quotes from the literature, based on work and idea by
        [Jaap Meijers](http://www.eerlijkemedia.nl/) ([E-reader clock](https://www.instructables.com/id/Literary-Clock-Made-From-E-reader/)).

Force light or dark theme with the `theme` query parameter. E.g. https://literature-clock.jenevoldsen.com?theme=dark

The working site is in the docs/ folder, and can be visited at http://literature-clock.jenevoldsen.com/. To run it locally you may need to serve docs/ with an HTTP server (e.g. `python3 -m http.server`) ... or just open index.html in Firefox (thanks [@gbear605](https://github.com/gbear605)).

> ℹ️ NB: Some quotes are potentially NSFW. See issue [#11](https://github.com/JohannesNE/literature-clock/issues/11).
> To filter out (most) NSFW quotes, use the `sfw` query parameter. E.g. https://literature-clock.jenevoldsen.com?sfw=true
> 

# Convert .csv quotes to .json quotes

Quotes are kept in `litclock_annotated.csv`. These are converted into a `.json` file for each minute with `csv_to_json.R`. To run the R script, install R and use the package manager, {packrat}, to install the correct version of the packages: `packrat::restore()`.

## Other related projects

- **[litime](https://github.com/ikornaselur/litime)** - A command line tool that shows a timely quote when it is executed.
