from task.extension.database_extension import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(30), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
