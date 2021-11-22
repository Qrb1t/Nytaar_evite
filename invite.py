from flask import (
    app, flash, g, redirect, render_template, request, url_for
)
from nytaar_evite_main.db import get_db

@app.route('/rsvp', methods=('GET', 'POST'))
def rsvp():
    if request.method == 'POST':
        name = request.form['username']
        attending = request.form['attending']
        db = get_db
        error = None

        if not name:
            error = 'Navn skal udfyldes.'
        elif not attending:
            error = 'Du skal svare "ja" eller "nej".'

        if error is None:
            db.execute(
                "INSERT INTO guest (tName, bAttending) VALUES (?, ?)",
                (name, attending),
            )
            db.commit()
            return redirect(url_for("guestlist"))
    
        flash(error)
    
    return render_template('rsvp.html')