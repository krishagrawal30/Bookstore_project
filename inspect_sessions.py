import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from django.contrib.sessions.models import Session

# Query all sessions
sessions = Session.objects.all()

# Decode and print session data
for session in sessions:
    try:
        session_data = session.get_decoded()
        print(f"Session Key: {session.session_key}")
        print(f"Session Data: {session_data}")
    except Exception as e:
        print(f"Error decoding session {session.session_key}: {e}")