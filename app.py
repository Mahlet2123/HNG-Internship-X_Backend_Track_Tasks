#!/usr/bin/env python3
""" the app module """
from flask import Flask, request, jsonify
import datetime
import pytz


app = Flask(__name__)


@app.route("/api", methods=["GET"])
def get_info():
    """return informations required"""
    # get query parameters from url
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    # current day of the week
    current_day = datetime.datetime.now(pytz.UTC).strftime("%A")

    # Get the current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.now(pytz.UTC)
    current_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%S") + "Z"

    # github URLs
    github_file_url = (
        "https://github.com/Mahlet2123/HNG-Internship-X_Backend_Track_Tasks/blob/main/app.py"
    )
    github_repo_url = (
        "https://github.com/Mahlet2123/HNG-Internship-X_Backend_Track_Tasks"
    )

    # the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
