def build_report(emails):
    count=len(emails)
    sender_count={}
    for email in emails:
        sender=email["sender"]
        if sender not in sender_count:
            sender_count[sender]=0
        sender_count[sender]+=1
    
    lines=[]
    lines.append("Yesterday Mail Report")
    lines.append("")
    lines.append(f"Total emails: {count}")
    lines.append("")
    lines.append("Top senders:")
    for sender,count in sender_count.items():
        lines.append(f"{sender} - {count} emails")
    return "\n".join(lines)