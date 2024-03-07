from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itsm.db'
metadata = SQLAlchemy(app)

class Ticket(metadata.Model):
    id = metadata.Column(metadata.Integer, primary_key=True)
    title = metadata.Column(metadata.String(100), nullable=False)
    description = metadata.Column(metadata.Text, nullable=False)
    status = metadata.Column(metadata.String(20), nullable=False, default='open')

@app.route('/')
def home():
    tickets = Ticket.query.all()
    return render_template('home.html', tickets=tickets)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ticket = Ticket(title=title, description=description)
        metadata.session.add(ticket)
        metadata.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    ticket = Ticket.query.get_or_404(id)
    if request.method == 'POST':
        ticket.title = request.form['title']
        ticket.description = request.form['description']
        ticket.status = request.form['status']
        metadata.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', ticket=ticket)

@app.route('/delete/<int:id>')
def delete(id):
    ticket = Ticket.query.get_or_404(id)
    metadata.session.delete(ticket)
    metadata.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        # Create the database and tables if they don't exist
        metadata.create_all()
    # Start the application
    app.run(debug=True)
