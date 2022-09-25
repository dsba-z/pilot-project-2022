def zoom(link):
    link = link.split('/')
    id = link[4]
    if len(id) == 9:
        meeting_id = (id[0:3] + " " + id[3:6] + " " + id[6:9])
    elif len(id) == 10:
        meeting_id = (id[0:3] + " " + id[3:6] + " " + id[6:10])
    else:
        meeting_id = (id[0:3] + " " + id[3:7] + " " + id[7:11])
    return meeting_id

