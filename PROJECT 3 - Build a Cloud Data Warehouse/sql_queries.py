import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

ARN = config.get("IAM_ROLE", "ARN")
LOG_DATA = config.get("S3", "LOG_DATA")
LOG_JSONPATH = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events 
(
  artist            VARCHAR NOT NULL,
  auth              VARCHAR,
  first_name        VARCHAR,
  gender            VARCHAR,
  iteminSession     INT,
  last_name         VARCHAR,
  length            DECIMAL,
  level             VARCHAR,
  location          VARCHAR,
  method            VARCHA,
  page              VARCHAR,
  registration      VARCHAR,
  session_id        INT NOT NULL,
  song              VARCHAR,
  status            INT,
  ts                TIMESTAMP,
  user_agent        VARCHAR,
  user_id           INT 
);
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs
(
  num_songs         INT NOT NULL,
  artist_id         VARCHAR NOT NULL,
  artist_latitude   FLOAT,
  artist_longitude  FLOAT,
  artist_location   VARCHAR,
  artist_name       VARCHAR,
  song_id           VARCHAR NOT NULL,
  title             VARCHAR,
  duration          FLOAT,
  year              INT
);
""")

songplay_table_create = ("""
CREATE TABLE songplay
(
  songplay_id   INT NOT NULL,
  start_time    TIMESTAMP,
  user_id       INT NOT NULL, 
  level         VARCHAR, 
  song_id       VARCHAR NOT NULL, 
  artist_id     VARCHAR NOT NULL, 
  session_id    INT NOT NULL, 
  location      VARCHAR, 
  user_agent    VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE user
(
  user_id      INT NOT NULL,
  first_name   VARCHAR, 
  last_name    VARCHAR, 
  gender       VARCHAR, 
  level        VARCHAR
);
""") 

song_table_create = ("""
CREATE TABLE song
(
  song_id     INT NOT NULL,
  title       VARCHAR, 
  artist_id   VARCHAR NOT NULL, 
  year        INT, 
  duration    FLOAT
);
""") 

artist_table_create = ("""
CREATE TABLE artist
(
  artist_id  VARCHAR NOT NULL,
  name       VARCHAR NOT NULL,
  location   VARCHAR NOT NULL, 
  lattitude  FLOAT, 
  longitude  FLOAT
""") 

time_table_create = ("""
CREATE TABLE time
(
  start_time   TIMESTAMP NOT NULL,
  hour         INT NOT NULL,
  day          INT NOT NULL, 
  week         INT NOT NULL,
  month        INT NOT NULL, 
  year         INT NOT NULL, 
  weekday      INT NOT NULL
""")

# STAGING TABLES

staging_events_copy = ("""
    copy staging_events
    from {0}
    iam_role {1}
    json {2};
""").format(LOG_DATA, ARN, LOG_JSONPATH)

staging_songs_copy = ("""
    copy staging_songs
    from {0}
    iam_role {1}
    json 'auto';
""").format(SONG_DATA, ARN)

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent)
SELECT DISTINCT 
    timestamp with time zone 'epoch' + se.ts/1000 * interval '1 second', 
    se.userId, 
    se.level, 
    ss.song_id, 
    ss.artist_id, 
    se.sessionId, 
    se.location, 
    se.userAgent
FROM staging_events AS se 
    INNER JOIN staging_songs AS ss ON se.song = ss.title AND se.artist = ss.artist_name AND se.length = ss.duration
WHERE 
    se.page = 'NextSong'
""")

user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level)
SELECT DISTINCT 
    userId, 
    firstName, 
    lastName, 
    gender, 
    level
FROM staging_events
WHERE 
    page = 'NextSong' 
    AND userId IS NOT NULL
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration)
SELECT DISTINCT 
    song_id, 
    title, 
    artist_id, 
    year, 
    duration
FROM staging_songs
WHERE 
    song_id IS NOT NULL
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id,
    name, 
    location, 
    latitude, 
    longitude)
SELECT DISTINCT 
    artist_id, 
    artist_name,
    artist_location, 
    artist_latitude, 
    artist_longitude
FROM staging_songs
WHERE 
    artist_id IS NOT NULL
""")

time_table_insert = ("""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday)
SELECT 
    start_time, 
    extract(hour from start_time), 
    extract(day from start_time), 
    extract(week from start_time), 
    extract(month from start_time), 
    extract(year from start_time), 
    extract(weekday from start_time)
FROM songplays
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
