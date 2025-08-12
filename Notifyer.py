

import requests



url = "http://localhost:3001/api/sendText"
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": "yoursecretkey"
}


def build_notify_data(content: str, group_chat_id: str,member_chat_id: str):

    return {
        "session": "default",
        "chatId": group_chat_id,
        "text": content,
        "mentions": [
            member_chat_id
        ]
    }


def send_notification(content: str, group_chat_id: str, member_chat_id: str) -> bool:
    notify_data = build_notify_data(content, group_chat_id, member_chat_id)
    response = requests.post(url, json=notify_data, headers=headers)

    if response.status_code == 201:
        print(f"Sending notification for {content} to user {member_chat_id} successfully.")
        return True
    else:
        print(response)
        print(f"Failed to send for {content} to user {member_chat_id} successfully.")
        return False



