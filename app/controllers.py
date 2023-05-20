class UserController():
    
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(id=form.id.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for('index'))
    
    
    
    def logout():
        logout_user()
        return redirect(url_for('index'))