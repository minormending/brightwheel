from typing import List, Dict, Any, Iterable
from requests import Session, Response

from .models import User, Student, Activity


class BrightwheelClient:
    _BASE_URL = "https://schools.mybrightwheel.com/api/v1/"

    def __init__(self, auth_cookie: str) -> None:
        self.session: Session = Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            }
        )
        self.session.headers.update({"Cookie": f"_brightwheel_v2={auth_cookie}"})

    def get_me(self) -> User:
        resp: Response = self.session.get(f"{self._BASE_URL}/users/me")
        return User(resp.json())

    def get_students(self, guardian_id: str) -> Iterable[Student]:
        resp: Response = self.session.get(
            f"{self._BASE_URL}/guardians/{guardian_id}/students?include[]=schools"
        )
        for student in resp.json().get("students", []):
            yield Student(student)

    def get_activities(
        self, student_id: str, page: int, count: int = 100
    ) -> Iterable[Activity]:
        params: Dict[str, Any] = {
            "page": page,
            "page_size": count,
            "include_parent_actions": False,
        }
        resp: Response = self.session.get(
            f"{self._BASE_URL}/students/{student_id}/activities", params=params
        )
        for activity in resp.json().get("activities", []):
            yield Activity(activity)

    def get_all_activities(self, student_id: str) -> Iterable[Activity]:
        page: int = 1
        while True:
            activities: List[Activity] = list(self.get_activities(student_id, page, count=1000))
            page += 1
            if not activities:
                break
            for activity in activities:
                yield activity
