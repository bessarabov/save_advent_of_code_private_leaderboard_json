# save_advent_of_code_private_leaderboard_json

This is a simple script to download [Advent of Code](https://adventofcode.com/)'s private leaderboard data as JSON.

For convenience of use, this script is wrapped in Docker image.

On the site [Advent of Code](https://adventofcode.com/) there is a request:

> Please don't make frequent automated requests to this service -
> avoid sending requests more often than once every 15 minutes (900 seconds).

Please follow this request when using this script.

## Usage

For docker image to work in needs `/input/settings.json`. It must contain such info:

```
{
    "leaderboard_id" : 123,
    "year" : 2023,
    "cookie_session" : "asdf..."
}
```

Script running in docker downloads json as `/output/output.json`

Here is an example how you can run this docker image:

```
docker run \
    --rm \
    -v `pwd`/settings.json:/input/settings.json \
    -v `pwd`:/output/ \
    bessarabov/save_advent_of_code_private_leaderboard_json:1.0.0 \
    ;
```
