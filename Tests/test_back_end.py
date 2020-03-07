import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import *

import os

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('TEST_DATABASE_URI'))
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()
        usRoles = ["Guest","Couple","2nd line","Wedding party"]

        for i in usRoles:
            roleAdd = User_roles(role = i)
            db.session.add(roleAdd)
            db.session.commit()

        # create test admin user
        admin = User(first_name="admin", last_name="admin",permission="Couple", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        employee = User(first_name="test", last_name="user",permission = "Guest", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)


    #account page
    def test_admin_redirect(self):
        target_url = url_for('account')
        redirect_url = url_for('home', next=target_url)
        response = self.client.get(target_url)
        self.assertRedirects(response, redirect_url)
    #logout
    #delete account
    def test_admin_redirect(self):
        target_url = url_for('account_delete')
        redirect_url = url_for('home', next=target_url)
        response = self.client.get(target_url)
        self.assertRedirects(response, redirect_url)
    #admin
    def test_admin_redirect(self):
        target_url = url_for('admin')
        redirect_url = url_for('home', next=target_url)
        response = self.client.get(target_url)
        self.assertRedirects(response, redirect_url)
    #edit user
    def test_admin_redirect(self):
        target_url = url_for('edit_users')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertRedirects(response, redirect_url)
    #delete gifts

