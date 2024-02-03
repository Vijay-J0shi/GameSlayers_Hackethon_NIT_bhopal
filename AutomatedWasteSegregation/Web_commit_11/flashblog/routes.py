from flask import flash, render_template, url_for, redirect,jsonify
from flashblog.forms import *
from flashblog.forms2 import *
from flashblog.models import *
from flashblog import app,db




@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/join")
def join():
    return render_template("join.html")

@app.route("/partner", methods=["GET","POST"])
def partner():
    form=Partner_with_us_Form()
    if form.validate_on_submit():
        user=User(company=form.company_name.data,industry=form.industry.data,contact_name=form.contact_person_name.data,position=form.position.data,email=form.email.data,
                 phone_number=form.phone.data ,objective=form.content.data,integration=form.integration.data)
        db.session.add(user)
        db.session.commit()
        flash("Your response has been recorded")  #Flash messages are typically displayed in the next request 
        return redirect(url_for("home"))# redirect is used to send user to another page (this is next request)
    return render_template("partner.html",form=form)



@app.route("/collaborate", methods=["GET","POST"])
def collaborate():
    form=Collaborate_with_us_Form()
    if form.validate_on_submit():
        info=Personal_Info(contact_name=form.full_name.data,email=form.email.data,phone_number=form.phone.data,skills=form.content.data)
        db.session.add(info)
        db.session.commit()
        flash("Your response has been recorded")  #Flash messages are typically displayed in the next request 
        return redirect(url_for("home"))# redirect is used to send user to another page (this is next request)
    return render_template("collaborate.html",form=form)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/detection")
def detection():
    return render_template("detection.html")



@app.route("/supporter")
def supporter():
    return render_template("supporter.html")

if __name__ == "__main__":  # used to run directly python module
    app.run(debug=True)
