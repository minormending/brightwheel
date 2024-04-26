import os
import argparse
from typing import Any, List, Dict
from datetime import datetime
from requests import Session, Response

from .brightwheel import BrightwheelClient
from .models import Activity, Student, User
from urllib.parse import urlparse


def get_media_path(url: str, activity: Activity, output_dir: str) -> str:
    # Get the file extension from the URL
    parsed_url = urlparse(url)
    path_without_query = parsed_url.path
    extension: str = os.path.splitext(path_without_query)[1]

    # Get the date and category from the activity for the filename
    created_on: datetime = datetime.fromisoformat(activity.created_at)
    date: str = created_on.strftime("%Y-%m-%d_%H%M%S")
    category: str = (
        activity.category_tags[0].name if activity.category_tags else "uncategorized"
    )

    # Create the filename and full path
    filename: str = f"{date}_{category}{extension}"
    return os.path.join(output_dir, filename)


def download_media(
    url: str, activity: Activity, session: Session, output_dir: str
) -> str:
    # Get the path to save the media
    media_path: str = get_media_path(url, activity, output_dir)

    # Check if media already exists and skip if it does
    if os.path.exists(media_path):
        print(f"Skipping, media already exists: {media_path}")
        return None

    # Download the media
    response: Response = session.get(url)
    with open(media_path, "wb") as f:
        f.write(response.content)

    return media_path


def export_media_for_student(
    student: Student, client: BrightwheelClient, output_dir: str
) -> None:
    print(
        f"Exporting media for student: {student.student.first_name} {student.student.last_name}"
    )

    # Download images and videos from each activity
    count: int = 0
    for activity in client.get_all_activities(student.student.object_id):
        if activity.media and activity.media.image_url:
            url: str = activity.media.image_url
            image_path: str = download_media(url, activity, client.session, output_dir)
            if image_path:
                count += 1
                print(f"Downloaded image ({count}): {image_path}")
        if activity.video_info and activity.video_info.downloadable_url:
            url: str = activity.video_info.downloadable_url
            video_path: str = download_media(url, activity, client.session, output_dir)
            if video_path:
                count += 1
                print(f"Downloaded video ({count}): {video_path}")

    print(
        f"Downloaded {count} media items for {student.student.first_name} {student.student.last_name}"
    )


def export_media(auth_cookie: str, output_dir: str) -> None:
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    client: BrightwheelClient = BrightwheelClient(auth_cookie)
    guardian: User = client.get_me()

    students: List[Student] = list(client.get_students(guardian.object_id))
    for student in students:
        export_media_for_student(student, client, output_dir)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download images and videos from Brightwheel activities"
    )
    parser.add_argument("auth_cookie", help="Auth cookie for the Brightwheel API")
    parser.add_argument(
        "output_dir",
        help="Output directory to save the downloaded media",
    )
    args = parser.parse_args()

    export_media(args.auth_cookie, args.output_dir)


if __name__ == "__main__":
    main()
