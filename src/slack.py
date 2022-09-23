import os
from slackclient import SlackClient





def send_slack_msg(channel: str, text=None):

    attachments = []

    slack = SlackClient(os.environ["slackToken"])
    result = slack.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        attachments=attachments,
        as_user=True,
        unfurl_links=False,
    )

    return result

def send_adjust_size(service, desiredCount, reason):
    text = ""
    if reason == "scaleIn":
        text = (
            f"scale in \n- Target: {service}\n- Scale: {desiredCount}EA",
        )
    elif reason == "scaleOut":
        text = (
            f"scale out \n- Target: {service}\n- Scale: {desiredCount}EA",
        )
    send_slack_msg("yout-channel-name", text)



