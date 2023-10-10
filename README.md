# FIFA-Song-Analysis
## Overview
[Link to Github Repository](https://github.com/ryanwonghc/FIFA-Song-Predictions)

From Bakermat to John Newman, EA Sport's FIFA games have introduced me to countless new artists and iconic songs across genres that have come to define my childhood. Ask any avid FIFA player, and they will likely tell you the same. FIFA soundtracks hold a unique significance in the realm of sports and entertainment- they offer a glimpse into the collective music trends and tastes of a global community.  

This project aims to identify the music selection criteria for songs in FIFA playlists and how this criteria has evolved over time. 

#### Tools/Libraries Used
- Python: Spotipy, Pandas, NumPy, Matplotlib, Seaborn

## Analyzing Past FIFA Playlists
I used [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) to access Spotify data for songs from 10 FIFA playlists (2014-2023). The data I pulled can be broadly split into three categories:
- Song data
    - Song popularity, length, whether or not it's marked explicit
    - Song audio data: a list of a song's [audio features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features), including variables such as danceability, loudness, and tempo
- Album data
    - Album release date, whether the song was released as a single (if album only has one song in it), album popularity
    - I was unable to find the data for the song release date, so although this is not always the case, I am making the assumption that the song was released on the same date as the album
- Artist data
    - Artist popularity, number of followers, and genre classification
    - I was unable to find song specific genre data, so I am making the assumption that each song is classified under the same genre as its artist

#### Song Genre Data
<p align="center">
    <img src="charts/wordcloud.png"><br>
    <i>Most Frequent Song Genres In FIFA Playlists</i>
</p>
FIFA playlists contain songs across a diverse set of genres but a few genres stand out in particular as a popular choice for EA Sport's picks:

- House
- Pop
- Hip Hop

Indie, dance, alternative, modern, and rock are also popular keywords. Additionally, although not as prominent, we also see a few region specific keywords, namely: Australian, UK, Belgian, French, Dutch, English, Nigerian, and Latino.

2014 | 2015 | 2016 | 2017 | 2018
:-------------------------:|:-------------------------:|:---------------------:|:---------------------:|:---------------------:
![2014](charts/2014_wordcloud.png)  |  ![2015](charts/2015_wordcloud.png) | ![2016](charts/2016_wordcloud.png) | ![2017](charts/2017_wordcloud.png) | ![2018](charts/2018_wordcloud.png)

2019 | 2020 | 2021 | 2022 | 2023
:-------------------------:|:-------------------------:|:---------------------:|:---------------------:|:---------------------:
![2019](charts/2019_wordcloud.png)  |  ![2020](charts/2020_wordcloud.png) | ![2021](charts/2021_wordcloud.png) | ![2022](charts/2022_wordcloud.png) | ![2023](charts/2023_wordcloud.png)
<p align="center">
    <i>Wordclouds of the Most Frequent Song Genres Each Year</i>
</p>

Taking a closer look at how genre choices have changed over time, we arrive at several insights:
- Genre choice has definitely evolved over time. Categories such as House, Dance, and Rock went from being extremely popular in 2014 to being all but phased out by 2015. They were replaced by Indie, Pop, and Alternative, which are still the dominant categories today.
    - It's interesting that although house music was not a popular choice for most of the selected timespan, it is such a big part of the overall wordcloud. This suggests that it was extremely prominent when it was in fashion back in 2014.
- Hip hop has remained consistently popular throughout the 10 years.
- From 2020 onwards, there seems to be a more diverse mix of music in the playlist (popular genres are not as overwhelmingly dominant in the wordclouds)
- 2020 appeared to be a year with a very diverse selection of music- the sizes of the genres are more evenly spread out in the 2020 wordcloud.

#### Song and Album Data
Due to the abundance of new music every year and the propensity of FIFA playlists to reflect the most current musical trends, it would make sense that FIFA playlists each year are curated with songs released within the past year. This is evidenced in the chart below- at least 75% of the songs picked in each year's playlist were released within 1 year of the playlist compilation date.

<p align="center">
    <img src="charts/release_vs_compilation_date_ex_outliers.png"><br>
</p>

The chart assumes that the playlist for each year was compiled on the first day of the year (eg. 2014-01-01). There are several negative numbers here, which is due to instances of the song being released prior to the album it is on (and it was assumed that the song and album release day are the same). The median time elapsed hovers consistently at around 200 days prior to playlist release. 2023's playlist had a median time elapsed of 268 days, which is significantly higher than the 200 days mark from previous years. This however may be due to the fact that the 2023 playlist was much larger than recent years (81 songs compared to 30-40 songs in years prior). As a result, EA Sports may have felt that it was appropriate to add more "throwback" songs on top of the songs from 2023. EA Sports also released a [World Cup playlist](https://www.theloadout.com/fifa-23/world-cup-mode-soundtrack) for FIFA 2023 which contained songs from prior playlists, which could suggest an emphasis on nostalgia and older songs.

<p align="center">
    <img src="charts/line_song_dur.png"><br>
</p>

In the above chart, the bands represent 1 standard deviation. There seems to be a wide range of song lengths, but most are 2.5 to 5 minutes long, which reflects the average song length in general. The average song length seems to be trending slightly downwards, but that could just be reflective of [overall industry trends](https://www.vice.com/en/article/qjv8pq/pop-songs-shorter-than-ever).

<p align="center">
    <img src="charts/explicit.png"><br>
</p>

Given that FIFA games are rated E for Everyone, it may be the case the playlist avoids explicit songs. This was definitely the case in 2014, with only 1 song being marked as explicit. However, though still a minority, the number of explicit songs as well as the proportion of songs in the playlist has been trending upwards. At the peak in 2022, a third of the playlist's songs were marked as explicit. 

<p align="center">
    <img src="charts/popularity2.png"><br>
</p>

I was hesitant to read too deeply into popularity scores because I suspect that a song's placement in the FIFA playlist heavily impacts its popularity score by increasing listenership. In the chart above, I plotted each song's popularity against its album popularity score. Points above the dotted line indicate that the album is more popular than the song, which would suggest that there are more popular tracks on the album (ie. the song was not the most popular song on the album). In the chart, we see there are more points under the line (48% under line, 20% over line), meaning that songs in FIFA playlists typically are the most popular songs in its album. 

We see that on average, points above the line are farther away from the line than points under the line. The farther above the line a song is, the less popular it is compared to the most popular song in the album. To illustrate this, the purple point on the graph represents the song "People" by *Kungs* and *The Knocks*. That song has 4.2M plays on Spotify, which pales in comparison to "Never Going Home" and "Clap Your Hands" in the album which have 265M and 118M plays respectively.

About 30% of songs have a popularity of 0. Since recent plays weigh more in Spotify's popularity scoring algorithm, This suggests that they haven't been played recently. The percentage of songs with a popularity score of 0 each year is illustrated in the chart below:

<p align="center">
    <img src="charts/popularity0.png"><br>
</p>

This suggests that on average, the older the songs are, the less popular they get, which makes sense. However, it is surprising that the percentage isn't higher for the older playlists: except for 2014 (51% 0 popularity), a majority of each year's playlists have a non-zero popularity score. Whether or not the FIFA game is responsible for the sustained plays is unclear.


#### Artist Data

I elected to look at artist follower count over artist popularity score to determine artist popularity because I am making the assumption that people only choose to follow an artist if they are interested in their music. In contrast, since the artist's popularity score is calculated using the popularity scores of their music, an artist's popularity score can be temporarily inflated by their song being selected to appear in the FIFA playlist as it will receive more plays. 

<p align="center">
    <img src="charts/artist_followers_bar.png"><br>
    <i>Artist Follower Count Distribution (Logarithmic Scale)</i>
</p>

In the above chart, we see that in the earlier years (2014-2018), distribution of artist follower count was more left skewed, meaning there was an emphasis on selecting songs from more heavily followed artists. Nowadays, there is more representation from artists with different sized followings. In more recent years, FIFA has starting including artists with smaller followings (follower count < 1000), though it is still a small proportion of the playlist.

According to [Chartmasters](https://chartmasters.org/spotify-most-followed-artists/), the 100th most followed artist on Spotify is 2pac with a follower count of 16,362,807. Given that FIFA is such a mainstream game, I assumed they would pick mainstream music. However, top 100 artists only make up 1.5% of the playlist. Going a step down, artists with 1M+ followers only make up 25% of the playlist (75th percentile). This is illustrated in the chart below:

<p align="center">
    <img src="charts/artist_followers_step.png"><br>
</p>

From the chart, we can also see the 25th percentile for follower count is around 50,000.

#### Audio Data

Spotify's audio data consists of 12 different audio features measuring factors such as a song's energy, instrumentalness, and key. See Spotify's [API reference page](https://developer.spotify.com/documentation/web-api/reference/get-audio-features) for how to interpret audio data. I used the findings in [this website](https://dkhurjekar.shinyapps.io/spotify/) and correlated [article]((https://dhruv-khurjekar.medium.com/investigating-spotifys-danceability-index-other-song-attributes-1983142f7dfd)), which contained analyses on the distributions of each of the audio features, to serve as a baseline to compare FIFA playlist audio features to.  

<p align="center">
    <img src="charts/audio_radar.png"><br>
</p>


In the chart above, we can see that over the years, FIFA is fairly consistent with song selection. There isn't too much deviation in most features- the biggest variations I can see are in mode, danceability, and energy. The following charts allow us to get a clearer understanding of how FIFA's selection of songs evolve over time.

<p align="center">
    <img src="charts/audio_line.png"><br>
</p>

**Mode**
This variable measures the modality (major or minor) of the track, with 1 being major and 0 being minor. We see that there has been a fairly large deviation in EA Sport's propensity to select songs in major or minor key over the year, with no obvious trend year over year (this is more clear in the chart below). This shows the diversity in music selection. Almost every year though has an average score > 0.5, indicating that there is a larger selection of songs in a major key. This may be because major scales and chord progressions do a better job of relating happy or up-beat emotions.

**Energy**
Compared to the median energy score of 0.465, we see that FIFA songs are typically extremely energetic (1.5-2x the score on average). This may be because associating high energy music with your game gives gamers more energy when playing the game, which is a positive. We do see though that energy scores are trending down over time, which make sense given the shift from genres such as House to genres such as Indie. 

**Danceability, Tempo**
Similar to the Energy section above, we see Tempo trending downwards but still largely above the median (115). Interestingly, it seems that danceability is trending in the opposite direction. Given that tempo plays a role in danceability, the data seems to suggest that music with tempo too high may not be danceable to, and that ~110-120bpm may be the sweet spot danceability. From the data, it is clear that FIFA is prioritizing music with high danceability. The average of 0.72 for a danceability score is greatly above the median of 0.55. 

**Acousticness, Liveness**
The data indicates that songs are neither acoustic nor live recordings. This makes sense, as most if not all tracks are studio recorded and professionally produced before making it onto the FIFA playlist.

**Valence**
Valence describes the "positiveness" of a song: whether it leaves the user feeling happy or sad. The score skew slightly higher than neutral (score of 0.5) but it does not appear that EA Sports has a strong preference for selecting "happy" music. We see the score spikes up in 2021, matching the high danceability score for the same year.

**Speechiness**
Speechiness was interesting to interpret because my initial thought was that these values seemed way too low. From Spotify's documentation, Speechiness should be in the range [0.66,1] for spoken word tracks such as podcasts, [0.33,0.66] for tracks that contain music and speech, either in sections or layered, and [0,0.33] for music heavy tracks. Given that anecdotally most if not all songs on the playlist contain words, the fact that the average scores were all in the [0.06,0.15] range every year surprised me. Nevertheless, this seems to suggest that FIFA prioritizes fairly melodic/ music heavy tracks with few or simple lyrics. We see the score is quite high in 2020, and this is due to the selection of a few rap heavy tracks such as "Unemployed", "Where Do I Begin", and "Where & When". For these songs, there are notably a few sections where the artist is not rapping over a beat, leading to a high speechiness score. 

**Instrumentalness**
Instrumentalness represents how music heavy (or vocal-less) a track is. At first glance, instrumentalness scores seem to contradict the conclusions made in the previous section, as the scores are quite low (~0.1 on a [0,1] scale). However, consulting historical distribution data, we see that the median instrumentalness score is 0.0005, which is one order of magnitude lower than the averages we see.


**Key**
<p align="center">
    <img src="charts/key_bar.png"><br>
</p>
Key represents the key a track is in, which consists of notes from A to G. Data about the song's key was not included in the charts above because it is categorical data that cannot be interpreted via averages. In the bar chart above, we see that the natural keys (not sharps or flats) are more prominently featured in the playlist. This reflects musical trends, according to this [website](https://www.hooktheory.com/cheat-sheet/key-popularity). "C","D", "A", and "G" are the most popular keys to write songs in- more than a third of all songs are written in these keys.

<p align="center">
    <img src="charts/key_line_reg.png">
</p>

The chart above illustrates what proportion of the playlist each year was written in each key. These lines are all lines of best fit, to illustrate the trend of key usage over time rather than to identify the exact proportions for each year. From the chart, we see that the "G" key has halved in prominence. Interestingly, while "C", "D", "A", and "G" are the most widely used keys in absolute terms, they are not the most commonly used in proportional terms. The period between 2018 and 2020 seemed to have the most even distribution in terms of key selection, especially if you ignore D#/Eb which has consistently low usage.


#### Ideas for Future Work
- Multi label classification problem: given a song, classify which FIFA playlist it belongs to
    - maybe instead of each year, classify by decade/ half a decade: years close to each other are quite similar