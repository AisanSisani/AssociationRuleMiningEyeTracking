
def get_dataset(file_path):
    f = open(file_path, "r")
    users = list()
    for line in f:
        user = eval(line)
        user_segments = set()
        for item in user:
            user_segments.add(item[0])
        users.append(list(user_segments))
        #print(user_segments)
    return users


