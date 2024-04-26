from typing import List, Dict, Optional, Any


class Actor:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.first_name: Optional[str] = data.get("first_name")
        self.last_name: Optional[str] = data.get("last_name")
        self.email: Optional[str] = data.get("email")
        self.user_type: Optional[str] = data.get("user_type")
        self.role: Optional[Role] = data.get("role")


class Role:
    def __init__(self, data: Dict[str, Optional[bool]]):
        self.is_administrator: Optional[bool] = data.get("is_administrator")


class ProfilePhoto:
    def __init__(self, data: Dict[str, Optional[str]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.image_url: Optional[str] = data.get("image_url")
        self.thumbnail_url: Optional[str] = data.get("thumbnail_url")
        self.thumbnail_image_url: Optional[str] = data.get("thumbnail_image_url")


class Target:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.billing_status: Optional[str] = data.get("billing_status")
        self.first_name: Optional[str] = data.get("first_name")
        self.last_name: Optional[str] = data.get("last_name")
        self.email: Optional[str] = data.get("email")
        self.auth_phone_number: Optional[str] = data.get("auth_phone_number")
        self.phone_1: Optional[str] = data.get("phone_1")
        self.phone_2: Optional[str] = data.get("phone_2")
        self.profile_photo: Optional[ProfilePhoto] = (
            ProfilePhoto(data["profile_photo"]) if data.get("profile_photo") else None
        )
        self.raw_passcode: Optional[str] = data.get("raw_passcode")
        self.user_type: Optional[str] = data.get("user_type")
        self.created_at: Optional[str] = data.get("created_at")
        self.activated: Optional[bool] = data.get("activated")
        self.invite_code: Optional[str] = data.get("invite_code")
        self.enrollment_status: Optional[str] = data.get("enrollment_status")
        self.authentication_methods: Optional[List[str]] = data.get(
            "authentication_methods"
        )


class Room:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.is_archive_ready: Optional[bool] = data.get("is_archive_ready")
        self.created_at: Optional[str] = data.get("created_at")
        self.name: Optional[str] = data.get("name")
        self.show_checkin_status: Optional[bool] = data.get("show_checkin_status")
        self.sort_by_checkin_status: Optional[bool] = data.get("sort_by_checkin_status")
        self.sort_by_last_name: Optional[bool] = data.get("sort_by_last_name")
        self.school_id: Optional[str] = data.get("school_id")
        self.max_capacity: Optional[int] = data.get("max_capacity")
        self.min_age: Optional[int] = data.get("min_age")
        self.max_age: Optional[int] = data.get("max_age")
        self.max_ratio: Optional[int] = data.get("max_ratio")
        self.color: Optional[str] = data.get("color")
        self.icon: Optional[str] = data.get("icon")
        self.is_demo_room: Optional[bool] = data.get("is_demo_room")


class Media:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.height: Optional[int] = data.get("height")
        self.image_url: Optional[str] = data.get("image_url")
        self.is_archive_ready: Optional[bool] = data.get("is_archive_ready")
        self.thumbnail_url: Optional[str] = data.get("thumbnail_url")


class DetailsBlob:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.tags: Optional[List[str]] = data.get("tags")


class CategoryTag:
    def __init__(self, data: Dict[str, Optional[str]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.name: Optional[str] = data.get("name")
        self.tag_type: Optional[str] = data.get("tag_type")


class Video:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.streamable_url: Optional[str] = data.get("streamable_url")
        self.downloadable_url: Optional[str] = data.get("downloadable_url")
        self.thumbnail_url: Optional[str] = data.get("thumbnail_url")
        self.transcoding_status: Optional[str] = data.get("transcoding_status")
        self.is_archive_ready: Optional[bool] = data.get("is_archive_ready")
        self.created_at: Optional[str] = data.get("created_at")
        self.updated_at: Optional[str] = data.get("updated_at")


class Activity:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.object_id: Optional[str] = data.get("object_id")
        self.actor: Optional[Actor] = (
            Actor(data.get("actor")) if data.get("actor") else None
        )
        self.target: Optional[Target] = (
            Target(data.get("target")) if data.get("target") else None
        )
        self.room: Optional[Room] = Room(data.get("room")) if data.get("room") else None
        self.media: Optional[Media] = (
            Media(data.get("media")) if data.get("media") else None
        )
        self.action_type: Optional[str] = data.get("action_type")
        self.details_blob: Optional[DetailsBlob] = (
            DetailsBlob(data.get("details_blob")) if data.get("details_blob") else None
        )
        self.event_date: Optional[str] = data.get("event_date")
        self.state: Optional[str] = data.get("state")
        self.note: Optional[str] = data.get("note")
        self.is_archive_ready: Optional[bool] = data.get("is_archive_ready")
        self.staff_only: Optional[bool] = data.get("staff_only")
        self.created_at: Optional[str] = data.get("created_at")
        self.updated_at: Optional[str] = data.get("updated_at")
        self.video_info: Optional[Video] = (
            Video(data.get("video_info")) if data.get("video_info") else None
        )
        self.dropoff_report: Optional[str] = data.get("dropoff_report")
        self.observation_milestones: Optional[str] = data.get("observation_milestones")
        self.health_check: Optional[str] = data.get("health_check")
        self.health_screen_display: Optional[str] = data.get("health_screen_display")
        self.source: Optional[str] = data.get("source")
        self.likes: Optional[int] = data.get("likes")
        self.category_tags: Optional[List[CategoryTag]] = (
            [CategoryTag(c) for c in data.get("category_tags")]
            if data.get("category_tags")
            else None
        )
        self.scale_tags: Optional[List[str]] = data.get("scale_tags")
        self.progress_tags: Optional[List[str]] = data.get("progress_tags")
        self.menu_item_tags: Optional[List[str]] = data.get("menu_item_tags")


class ActivityWrapper:
    def __init__(self, data: Dict[str, Optional[Any]]):
        self.count: int = data.get("count")
        self.offset: int = data.get("offset")
        self.page: int = data.get("page")
        self.page_size: int = data.get("page_size")
        self.activities: List[Activity] = [
            Activity(activity) for activity in data.get("activities", [])
        ]
