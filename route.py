from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime

import forms

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all() # db 내에 모든 정보 접근
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        
        t = Task(title=form.title.data, date=datetime.utcnow()) # data 형태
        
        db.session.add(t)
        db.session.commit()
        # data 저장
        
        flash('Task added to the database')
        
        return redirect(url_for('index')) # 'index' is a function name
        #return render_template('about.html', form=form, title=form.title.data)

    return render_template('add.html', form = form)

@app.route('/edit/<int:task_id>', methods=['GET','POST']) # <int:task_id>를 통해 task_id 에 접근 가능
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    
    if task: # 존재 하지 않을 시 Break
        if form.validate_on_submit():
            task.title = form.title.data
            # updated the task title
            task.date = datetime.utcnow()
            # updated the task time
            db.session.commit()
            # 이미 존재하기 때문에 생성하지 않고 commit
            flash('Task has been updated')
            return redirect(url_for('index'))
            # index 로 이동
            
        else:
            flash('Task not found')
         
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET','POST']) # <int:task_id>를 통해 task_id 에 접근 가능
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskFrom()
    
    if task: # 존재 하지 않을 시 Break
        if form.validate_on_submit():
            db.session.delete(task)
            # Task 삭제
            db.session.commit()
            # 변경사항 commit
            flash('Task has been deleted')
            return redirect(url_for('index'))
            # index 로 이동
         
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    
    else:
        flash('Task not found')
        
    return redirect(url_for('index'))