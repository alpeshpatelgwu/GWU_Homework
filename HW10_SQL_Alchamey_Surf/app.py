import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#@app.route("/")
#def welcome():
#    """List all available api routes."""
#    return (
#        f"Available Routes:<br/>"
#        f"/api/v1.0/precipitation<br/>"
#        f"/api/v1.0/stations<br/>"
#        f"/api/v1.0/tobs<br/>"
#        f"/api/v1.0/<start><br/>"
#        f"/api/v1.0/<start>/<end><br/>"
#        
#    )
#
#

@app.route("/")
def welcome():
    return(
            """
            <html>
            <h1>List all available api routes.</h1>
            <ul>
            <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
            <li><a href="/api/v1.0/stations">/api/v1.0/stations</li></a>
            <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</li></a>
            <li><a href="/api/v1.0/<start>">/api/v1.0/<start></li></a>
            <li><a href="/api/v1.0/<start>/<end>">/api/v1.0/<start>/<end></li></a>
            </ul>
            <img src="Images/surfs-up.jpeg" alt="Surf's Up" style="width:100px; height:100px;">
            <h1> Cowabunga!</h1>
        
            </html>
            """
            )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    annualprecip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # Calculate the date 1 year ago from the last data point in the database
    latest_date = annualprecip[0]
    date_object = dt.datetime.strptime(latest_date, "%Y-%m-%d").date()
    year_ago = date_object - dt.timedelta(days=365)

    precipquery = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    # Convert list of tuples into normal list
    
    all_precip = []
    for precip in precipquery:
        precip_dict = {}
        precip_dict["date"] = Measurement.date
        precip_dict["precip"] = Measurement.prcp
        all_precip.append(precip_dict)

    all_precip = list(np.ravel(precipquery))

    return jsonify(all_precip)


@app.route("/api/v1.0/stations")
def stations():
    #Return a JSON list of stations from the dataset.
    session = Session(engine)
    stations_available = session.query(Measurement.station).all()
    return jsonify(stations_available)

@app.route("/api/v1.0/tobs")
def tobs():
    #query for the dates and temperature observations from a 
    # year from the last data point.
    #Return a JSON list of Temperature Observations (tobs) 
    # for the previous year.
    session = Session(engine)
    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    annualprecip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # Calculate the date 1 year ago from the last data point in the database
    latest_date = annualprecip[0]
    date_object = dt.datetime.strptime(latest_date, "%Y-%m-%d").date()
    year_ago = date_object - dt.timedelta(days=365)
    annual_tobs = session.query(Measurement.tobs).filter(Measurement.date >= year_ago).all()

    return jsonify(annual_tobs)

# Return a JSON list of the minimum temperature, the average temperature, 
# and the max temperature for a given start or start-end range.

@app.route("/api/v1.0/<start>")
def start_date(start):
    # When given the start only, calculate TMIN, TAVG, and TMAX for 
    # all dates greater than and equal to the start date.

    session = Session(engine)
    startdate = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    return jsonify(startdate)

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX 
    # for dates between the start and end date inclusive.    
    session = Session(engine)
    
    start_stop = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date == start).filter(Measurement.date == end).all()

    return jsonify(start_stop)
    
# Stopping flask can be a pain, so I recommend this ONLY in dev
# Avoid using this in production

    
from flask import request

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True)