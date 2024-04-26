class ProfilePhoto:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.image_url = data.get("image_url")
        self.thumbnail_url = data.get("thumbnail_url")
        self.thumbnail_image_url = data.get("thumbnail_image_url")


class AuthenticationMethod:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.verified = data.get("verified")
        self.type = data.get("type")
        self.email = data.get("email")
        self.phone_number = data.get("phone_number")


class School:
    def __init__(self, data):
        self.object_id = data.get("object_id")


class SchoolInvite:
    def __init__(self, data):
        self.school = School(data.get("school"))
        self.invite_status = data.get("invite_status")


class User:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.billing_status = data.get("billing_status")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.email = data.get("email")
        self.auth_phone_number = data.get("auth_phone_number")
        self.phone_1 = data.get("phone_1")
        self.phone_2 = data.get("phone_2")
        self.profile_photo = (
            ProfilePhoto(data["profile_photo"]) if "profile_photo" in data else None
        )
        self.raw_passcode = data.get("raw_passcode")
        self.user_type = data.get("user_type")
        self.created_at = data.get("created_at")
        self.activated = data.get("activated")
        self.invite_code = data.get("invite_code")
        self.intro_seen = data.get("intro_seen")
        self.demo_user = data.get("demo_user")
        self.authentication_methods = [
            AuthenticationMethod(method)
            for method in data.get("authentication_methods", [])
        ]
        self.school_invites = [
            SchoolInvite(invite) for invite in data.get("school_invites", [])
        ]
