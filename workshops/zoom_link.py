def zoom(link):
    link = link.split('/')
    meeting_id = link[4]
    if len(meeting_id) == 9:
        meeting_id = (meeting_id[0:3] + " " + meeting_id[3:6] + " " + meeting_id[6:9])
    elif len(meeting_id) == 10:
        meeting_id = (meeting_id[0:3] + " " + meeting_id[3:6] + " " + meeting_id[6:10])
    else:
        meeting_id = (meeting_id[0:3] + " " + meeting_id[3:7] + " " + meeting_id[7:11])
    return meeting_id
