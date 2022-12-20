from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .api import nfRequiredData, fnfRequiredData, bnfRequiredData

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/nifty')
@login_required
def nifty():
    return render_template("nifty.html", user=current_user, data = nfRequiredData, length = len(nfRequiredData))

@views.route('/finnifty')
@login_required
def finnifty():
    return render_template("finnifty.html", user=current_user, data = fnfRequiredData, length = len(fnfRequiredData))

@views.route('/banknifty')
@login_required
def banknifty():
    return render_template("banknifty.html", user=current_user, data = bnfRequiredData, length = len(bnfRequiredData))