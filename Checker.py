from datetime import datetime, timedelta

from typing import List
from zoneinfo import ZoneInfo

from model.models import  Duty
import pytz




def now() -> datetime:
    ireland_tz = pytz.timezone("Europe/Dublin")
    now = datetime.now()
    return now.astimezone(ireland_tz)


def _within_period(target_time: datetime,frequency_days: int) -> bool:
    return abs(target_time - now()) <= timedelta(days=frequency_days)


def _readTimeFromStr(date_str) -> datetime:
    dt_naive = datetime.strptime(date_str, "%Y-%m-%d")
    dt_aware = dt_naive.replace(tzinfo=ZoneInfo("Europe/Dublin"))
    return dt_aware


def check_need_notified_duties(duties:List[Duty]) -> List[Duty]:
    need_notified_duties :List[Duty] = []
    for duty in duties:
        last_assigned_date = _readTimeFromStr(duty.assigned_date)
        frequency_days = duty.frequency
        needNotified = _within_period(last_assigned_date, frequency_days) == False
        if needNotified:
            need_notified_duties.append(duty)

    return need_notified_duties



