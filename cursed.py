from random import randint
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file('cool.html')

@app.route("/one")
def one():
    qs = [["Do you look at food waste and think of what a good meal that would be?", "(a) Yes, Trash is such a waste of good food", "(b) Ew no, wtf mate","(c) I mean, maybe, depends on how it looks"],
    ["Are you very territorial?", "(a) Come into my room, I stab you", "(b) I let close friends use my things and come into my room", "(c) Communism is great"],            
    ["Do you expect to live more than 15 years?", "(a) Yes","(b) No", "(c) Questionable"],
    ["Do you have a strong body and weirdly elongated legs?", "(a) Nah, I think I have good proportions","(b) Well, yeah I guess", "(c) I don't but I think it looks pretty good"],
    ["Could you easily chug a glass of seawater for a bet?", "(a) for a Tenner? Sure", "(b) I could but I don't want to, so no", "(c) I would drink it for free"]]

    output=""" ARE YOU A SEAGULL? The official quiz<br />
        ----------------<br />
        If you identify with some of these situations, Science says you could be a seagull!!!!!
        <form action='two' method='post'>
        """
    for i in range(len(qs)):
        for j in range(len(qs[i])):
            if j == 0:
                output+= "<br />" + qs[i][0] + "<br />"
            else:
                output+= "<input type='radio' name=" + str(i) + " value=" + str(j-1) + ">" + qs[i][j] + "<br />"
    output+= """<br /><input type="submit" value="Submit">
    </form>  """
    return output
        
@app.route("/two", methods=['POST'])
def two():
    counter = 0
    
    for q in range(len(request.form)):
        a = int(request.form[str(q)])
        
        if q == 0 and a==0:
            counter += 1
        if q == 1 and a==0:
            counter += 1
        if q == 2 and a==1:
            counter += 1
        if q == 3 and a==1:
            counter += 1
        if q == 4 and a==2:
            counter += 1

    if counter >= 3:
        return "CONGRATULATIONS YOU ARE A SEAGULL!!!"
    else:
        return "oops, sorry you CANNOT be a seagull :( maybe start looking for a dayjob"
    
        
    return output
if __name__ == "__main__":
    app.run()