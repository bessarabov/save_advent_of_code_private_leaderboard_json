#!/usr/local/bin/python

import json
import requests
from datetime import datetime, timezone

class DataFetchError(Exception):
    pass

def log_message(message):
    current_time_utc = datetime.now(timezone.utc)
    timestamp_iso8601 = current_time_utc.replace(microsecond=0, tzinfo=None).isoformat() + 'Z'
    print(f"{timestamp_iso8601} {message}")

def get_data_from_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        return data

def raise_error_on_incorrect_settings(settings):
    if not isinstance(settings, dict):
        raise ValueError("Incorrect type of settings")

    if not "leaderboard_id" in settings:
        raise ValueError("Missing leaderboard_id")

    if not "year" in settings:
        raise ValueError("Missing year")

    if not "cookie_session" in settings:
        raise ValueError("Missing cookie_session")

def get_private_leaderboard_json(settings):
    url = f"https://adventofcode.com/{settings['year']}/leaderboard/private/view/{settings['leaderboard_id']}.json"

    headers = {
        'Cookie': f'session={settings["cookie_session"]}',
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            raise DataFetchError(f"Failed to fetch data from URL {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        raise DataFetchError(f"Request Exception: {e}")


def get_pretty_json(text):
    parsed_json = json.loads(text)
    pretty_json = json.dumps(parsed_json, indent=4, sort_keys=True) + '\n'
    return pretty_json

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except IOError as e:
        raise FileWriteError(f"Error writing to file '{file_name}': {e}")


if __name__ == '__main__':

    log_message('Started')

    settings = get_data_from_json_file('/input/settings.json')

    raise_error_on_incorrect_settings(settings)

    content = get_private_leaderboard_json({
        'leaderboard_id': settings['leaderboard_id'],
        'year': settings['year'],
        'cookie_session': settings['cookie_session'],
    })

    write_file('/output/output.json', get_pretty_json(content))

    log_message('Saved private leaderboard json to output.json')
