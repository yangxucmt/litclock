Software:
1. Fix the upper/lower case mismatch
2. < br >
3. The problem of Mr and Mr.
3. Add Easter eggs
4. Solve the problem of not having the time I want.
5. Configure the gui 

Hardware:
1. Purchase a raspberry pi or whatever with the same functionality
2. Get a touchscreen
3. 


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
