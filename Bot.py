
import json
from typing import List
from datetime import datetime
from Checker import check_need_notified_duties
from Notifyer import send_notification
from model.models import Duty, Group, Member
import textwrap
from dataclasses import asdict




def write_new_duties(duties:List[Duty]):
    dict_list = [asdict(d) for d in duties]
    with open("duties.json", "w", encoding="utf-8") as f:
        json.dump(dict_list, f, ensure_ascii=False, indent=4)


def load_duties() -> List[Duty]:
    result :List[Duty] = []
    with open("duties.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            result.append(Duty(**item)) 
        print("=====> Duties loaded <=====")
        return  result




def load_group()->Group:
    with open("group.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        members = [Member(**m) for m in data["group"]["members"]]
        print("=====> GROUP loaded <=====")
        return Group(
        name=data["group"]["name"],
        chatId=data["group"]["chatId"],
        members=members
    )




def get_next_duty_member_id(cur_member_id:int, group:Group) -> Member:
    member_count = len(group.members)
    next_member_id = (cur_member_id + 1) % member_count
    if(next_member_id == 0):
       return member_count
    else:
        return next_member_id



def get_member_by_id(cur_member_id:int, group:Group) -> Member:
    for member in group.members:
        if member.id == cur_member_id:
            return member
  

 
def send(duty:Duty,member:Member,date:str) -> bool:
    content = f''' 
            🚨🚨🚨 Hey {member.name} @{member.phoneId}
            {duty.duty_name} is on you this week!

            🗓️ {date} — don’t forget! ⏰✨
       '''
    return send_notification(textwrap.dedent(content).strip(), "120363422151287330@g.us", member.phoneId)


if __name__ == "__main__":
  
    duties =  load_duties()   
    group = load_group()
  
    need_notified_duties = check_need_notified_duties(duties)

    for duty in need_notified_duties:
      next_duty_member_id =  get_next_duty_member_id(duty.assigned_to, group)
      next_member = get_member_by_id(next_duty_member_id,group)
      
      new_assign_date = datetime.now().strftime("%Y-%m-%d")
      
      if next_member != None:
       
        notify_result = send(duty= duty, member=next_member,date=new_assign_date)

        if notify_result == True:
            print(next_member)  
            duty.assigned_to = next_duty_member_id
            duty.assigned_date = new_assign_date
           
    write_new_duties(duties)


      







   







