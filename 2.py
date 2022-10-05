from ast import Delete
from pickle import FALSE
from flask import Flask, request

app = Flask(__name__)
cpath = r"C:\Users\User105\Desktop\config.txt"
dpath = r"C:\Users\User105\Desktop\users.txt"

mainroute = "music"

def register_user(user):
    ntag = "name"
    ptag = "password"
    try:
        if(user[ntag] == None):
            return "noNameData"
        if(user[ptag] == None):
            return "noPasswordData"
        if(len(user[ntag]) <= 4 or len(user[ptag]) <=4):
            return "TooShortNameOrPassword"
    except:
        return "JSON is not in correct form"

    f = open(cpath, "r")
    s = f.read()
    if(s.isdigit()):
        max_id = int(s) + 1
        user_data = open(dpath, "a")
        user_data.write(f"id: {max_id} {user[ntag]} {user[ptag]}\n")
        user_data.close()
        open(cpath, "w").write(str(max_id))
        return "Success"
    else:
        return "UnexpectedError"

def get_all_users():
    userList = list();
    with open(dpath, "r") as data:
        for line in data:
            userList.append(line.replace("\n", "").split(" ")[1:4])
    return userList;

            
        
def modify_user(iuser, id):

    ntag = "name"
    ptag = "password"
    user_name = ""
    user_password = ""

    try:
        if(iuser[ntag] == None):
            return "Username is void"
        if(len(iuser[ntag]) <= 4):
            return "Username is too short"
        user_name = iuser[ntag]
    except:
        pass

    try:
        if(iuser[ptag] == None):
            return "Password is void"
        if(len(iuser[ptag]) <= 4):
            return "Password is too short"
        user_password = iuser[ptag]
    except:
        pass
    
    if(user_name == "" and user_password == ""):
        return "JSON is not in correct format"

    output_message = "UserNotFound"
    users_data = open(dpath, "r")
    users = users_data.readlines()
    new_users = list()
    for user in users:
        if (user.startswith(f"id: {str(id)}")):
            user_fields = user.split(" ")[1:4]
            if(user_name == ""):
                new_users.append(f"id: {str(id)} {user_fields[1]} {user_password}\n")
            elif (user_password == ""):
                new_users.append(f"id: {str(id)} {user_name} {user_fields[2]}\n")
            else:
                new_users.append(f"id: {str(id)} {iuser[ntag]} {iuser[ptag]}\n")
            output_message = f"User {id} was modified"
        else:
            new_users.append(user)
    users_data.close()
    users_data = open(dpath, "w")
    users_data.writelines(new_users)
    users_data.close()
    return output_message

def delete_user(id):
    output_message = "NotFound"
    users_data = open(dpath, "r")
    users = users_data.readlines()
    new_users = list()
    for user in users:
        if(not user.startswith(f"id: {str(id)}")):
            new_users.append(user)
        else:
            output_message = F"Deleted {id}"
    users_data.close()
    users_data = open(dpath, "w")
    users_data.writelines(new_users)
    users_data.close()
    return output_message




@app.route(f"/{mainroute}", methods = ["POST"])
def add_user():
    content = request.get_json()
    return register_user(content), 200

@app.route(f"/{mainroute}", methods = ["GET"])
def get_users():
    return get_all_users(), 200
        
@app.route(F"/{mainroute}/<id>", methods = ["PUT"])
def mod_user(id):
    content = request.get_json()
    return modify_user(content, id), 200

@app.route(f"/{mainroute}/<id>", methods = ["DELETE"])
def del_user(id):
    return delete_user(id), 200




app.run(host="localhost", port=3005)

    



