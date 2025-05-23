def solution(id_pw, db):
    id_input, pw_input = id_pw
    for user_id, user_pw in db:
        if user_id == id_input:
            if user_pw == pw_input:
                return "login"
            else:
                return "wrong pw"
    return "fail"