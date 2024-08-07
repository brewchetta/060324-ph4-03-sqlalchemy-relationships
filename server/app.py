#!/usr/bin/env python3

from datetime import datetime
from flask import request
from config import app, db
from models import VideoGame, Publication, Review, Doctor, Appointment


# ROUTES #

# READ
@app.get('/doctors')
def all_doctors():
    all_doctors = Doctor.query.all()
    doctor_dicts = []
    for doctor in all_doctors:
        doctor_dicts.append( doctor.to_dict() )
    return doctor_dicts, 200


# CREATE
@app.post('/doctors')
def create_doctor():
    data = request.json
    new_doctor = Doctor(name=data['name'])
    db.session.add(new_doctor)
    db.session.commit()

    return new_doctor.to_dict(), 201



# READ
@app.get('/appointments')
def all_appointments():
    all_appointments = Appointment.query.all()
    appointment_dicts = []
    for appointment in all_appointments:
        appointment_dicts.append( appointment.to_dict() )
    return appointment_dicts, 200


# CREATE
@app.post('/appointments')
def create_appointment():
    data = request.json

    new_date = datetime.strptime(data['datetime'], '%m-%d-%Y') # '8-6-2024'

    new_appointment = Appointment(
        doctor_id=data['doctor_id'], 
        patient_id=data['patient_id'], 
        datetime=new_date
    )

    db.session.add(new_appointment)
    db.session.commit()

    return new_appointment.to_dict(), 201











# EXERCISES #

# VideoGame ROUTES #

@app.get('/video-games')
def video_games_index():
    return [ v.to_dict() for v in VideoGame.query.all() ], 200


@app.get('/video-games/<int:id>')
def video_game_by_id(id):
    vg = VideoGame.query.where(VideoGame.id == id).first()
    if vg:
        return vg.to_dict(), 200
    else:
        return { 'error': 'Not found' }, 404


@app.post('/video-games')
def post_video_game():
    vg = VideoGame(name=request.json.get('name'))
    db.session.add(vg)
    db.session.commit()
    return vg.to_dict()


@app.delete('/video-games/<int:id>')
def delete_video_games():
    vg = VideoGame.query.where(VideoGame.id == id).first()
    if vg:
        db.session.delete(vg)
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404



# Publication ROUTES #

@app.get('/publications')
def publications_index():
    return [ p.to_dict() for p in Publication.query.all() ], 200


@app.get('/publications/<int:id>')
def publication_by_id(id):
    pub = Publication.query.where(Publication.id == id).first()
    if pub:
        return pub.to_dict(), 200
    else:
        return { 'error': 'Not found' }, 404


@app.post('/publications')
def post_publication():
    pub = Publication(name=request.json.get('name'))
    db.session.add(pub)
    db.session.commit()
    return pub.to_dict()


@app.delete('/publications/<int:id>')
def delete_publication():
    pub = Publication.query.where(Publication.id == id).first()
    if pub:
        db.session.delete(pub)
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404



# Review ROUTES #

@app.get('/reviews')
def reviews_index():
    return [ r.to_dict() for r in Review.query.all() ], 200


@app.get('/reviews/<int:id>')
def review_by_id(id):
    rev = Review.query.where(Review.id == id).first()
    if rev:
        return rev.to_dict(), 200
    else:
        return { 'error': 'Not found' }, 404


@app.post('/reviews')
def post_review():
    rev = Review(
        rating=request.json.get('rating'),
        videogame_id=request.json.get('videogame_id'),
        publication_id=request.json.get('publication_id')
    )
    db.session.add(rev)
    db.session.commit()
    return rev.to_dict()


@app.delete('/reviews/<int:id>')
def delete_review():
    rev = Review.query.where(Review.id == id).first()
    if rev:
        db.session.delete(rev)
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404



# RUN APP #

if __name__ == '__main__':
    app.run(port=5555, debug=True)