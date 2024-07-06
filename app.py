from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
import secrets

# Generate a random 32-byte (256-bit) hex-encoded secret key
random_secret_key = secrets.token_hex(32)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SECRET_KEY'] = random_secret_key

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bank_name = db.Column(db.String(50), nullable=False)
    account_number = db.Column(db.String(20), nullable=False)
    balance = db.Column(db.Float, default=0.0)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) if user_id is not None else None


@app.route('/')
@login_required
def dashboard():
    user_accounts = BankAccount.query.filter_by(user_id=current_user.id).all()

    # Check if the user has any bank accounts
    if not user_accounts:
        flash('Welcome! It looks like you need to add a bank account.')
        return redirect(url_for('bank_form'))

    return render_template('dashboard.html', accounts=user_accounts)


@app.route('/bank_form', methods=['GET', 'POST'])
@login_required
def bank_form():
    if request.method == 'POST':
        bank_name = request.form.get('bank_name')
        account_number = request.form.get('account_number')
        balance = float(request.form.get('balance'))

        # Check for duplicate account numbers
        existing_account = BankAccount.query.filter_by(user_id=current_user.id, account_number=account_number).first()
        if existing_account:
            flash('Bank account with the same account number already exists.')
        else:
            # Create a new bank account for the user
            new_account = BankAccount(user_id=current_user.id, bank_name=bank_name, account_number=account_number, balance=balance)
            db.session.add(new_account)
            db.session.commit()

            flash('Bank account added successfully!')

        return redirect(url_for('dashboard'))

    return render_template('bank_form.html')


@app.route('/delete_account/<int:account_id>')
@login_required
def delete_account(account_id):
    account_to_delete = BankAccount.query.get(account_id)

    if account_to_delete and account_to_delete.user_id == current_user.id:
        db.session.delete(account_to_delete)
        db.session.commit()
        flash('Bank account deleted successfully!')
    else:
        flash('Failed to delete bank account.')

    return redirect(url_for('dashboard'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username is already taken
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already taken. Please choose another.')

        # Create a new user
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('dashboard'))

    return render_template('register.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)