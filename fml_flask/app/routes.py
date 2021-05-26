from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
from app.forms import LoginForm, ConfigForm, TankForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
import pandas as pd

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    df = pd.read_csv("./app/data/config.csv", header=0)
    config_list=list(df.values)
    df = pd.read_csv("./app/data/tank_params.csv", header=0)
    tank_params_list=list(df.values)
    
    return render_template("index.html", title="FMLv0.1", config_list=config_list, tank_params_list=tank_params_list)

@app.route('/config', methods=["GET", "POST"])
@login_required
def config():
    form = ConfigForm()
    config_df = pd.read_csv("./app/data/config.csv", header=0, index_col="parameter")

    if form.validate_on_submit():
        # update parameters
        config_df.loc["display brightness (normal operating mode)", "value"] = form.normal_display_brightness.data
        config_df.loc["display brightness (active operating mode)", "value"] = form.active_display_brightness.data
        config_df.loc["active display brightness duration", "value"] = form.active_display_brightness_duration.data
        config_df.loc["fuel display duration", "value"] = form.fuel_display_duration.data
        config_df.loc["refill display duration", "value"] = form.refill_display_duration.data
        config_df.loc["flow encoder ratio", "value"] = form.flow_encoder_ratio.data
        config_df.loc["debounce time (reed)", "value"] = form.debounce_time_reed.data
        config_df.loc["debounce time (hall)", "value"] = form.debounce_time_hall.data
        config_df.loc["run out duration", "value"] = form.run_out_duration.data
        config_df.loc["run out level", "value"] = form.run_out_level.data

        # write updated values to the csv file
        config_df.to_csv("./app/data/config.csv", encoding="utf-8")

        # set flash message
        flash("Configuration updated successfully!", "success")

        # redirect
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("index")
        return redirect(next_page)
    
    # render template
    return render_template("config.html", title="FMLv0.1 - Configure Device Parameters", form=form, config_df=config_df)

@app.route('/tank', methods=["GET", "POST"])
@login_required
def tank():
    form = TankForm()

    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save("./app/data/tank_params.csv")

        flash("Tank parameter file uploaded successfully!", "success")

        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("tank.html", title="FMLv0.1 - Tank Parameters", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="FMLv0.1 - Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))
