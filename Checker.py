from datetime import datetime, timedelta

from typing import List

from model.models import  Duty



def _within_period(target_time: datetime,frequency_days: int) -> bool:
    now = datetime.now()
    return abs(target_time - now) <= timedelta(days=frequency_days)




def _readTimeFromStr(dt_str:str)->datetime:
    return datetime.strptime(dt_str.replace(" ",""), "%Y-%m-%d")





def check_need_notified_duties(duties:List[Duty]) -> List[Duty]:
    need_notified_duties :List[Duty] = []
    for duty in duties:
        last_assigned_date = _readTimeFromStr(duty.assigned_date)
        frequency_days = duty.frequency
        needNotified = _within_period(last_assigned_date, frequency_days) == False
        if needNotified:
            need_notified_duties.append(duty)

    return need_notified_duties



