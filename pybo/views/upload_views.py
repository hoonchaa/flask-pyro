from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Upload
from pybo.forms import UploadForm
from pybo.views.auth_views import login_required

bp = Blueprint('upload', __name__, url_prefix='/upoload')


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():

        f = request.files['file']
        filename = f.filename
        file_path = './pybo/upload_file/' + filename
        f.save(file_path)

        upload = Upload(subject=form.subject.data, content=form.content.data,
                            create_date=datetime.now(), user=g.user,
                        filename=filename, file_path=file_path,
                        process=request.form['process'], device=request.form['device'])
        db.session.add(upload)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('upload/upload_form.html', form=form)
