import match_objects as mo

import os.path
import inflect
import json

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

def get_creds():
    SCOPES = ['https://www.googleapis.com/auth/forms.body', 
              'https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/forms.responses.readonly']
    
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def make_claims_form(creds, num_choices, name_source, ages_required, title):
    service = build('forms', 'v1', credentials=creds)
    p = inflect.engine()

    form = {
        "title": title,
        "questions": []
    }

    form["questions"].append({
        "question": f"What is your username on {name_source}? Please enter the exact username, not a nickname or display name.",
        "type": "TEXT"
    })

    if ages_required:
        form["questions"].append({
            "question": "What is your age? Note that 'PREFER NOT TO SAY' will be treated as a minor for purposes of matching with adult content, and will not allow you to match with anyone who has selected to only match with minors/adults.",
            "type": "MULTIPLE_CHOICE",
            "options": 
            [
                {
                    "value": "ADULT"
                },
                {
                    "value": "MINOR"
                },
                {
                    "value": "PREFER NOT TO SAY"
                }
            ]
        })

    for i in range(num_choices):
        form["questions"].append({
            "question": f"Enter the work Id of your {p.number_to_words(p.ordinal(i + 1))} choice",
            "type": "TEXT"
        })
    form = service.forms().create(body=form).execute()

    return form

def make_submissions_form(creds, title):
    service = build('forms', 'v1', credentials=creds)
    form = {
        "title": title,
        "questions": []
    }

    form["questions"].append({
        "question": f"Enter the title of your work:",
        "type": "TEXT"
    })

    form["questions"].append({
        "question": f"Enter a summary for your work:",
        "type": "TEXT"
    })

    form["questions"].append({
        "question": f"Enter the ages you are willing/comfortable working with on your work. IF YOUR WORK IS 18+ YOU MUST SELECT ADULTS ONLY:",
        "type": "MULTIPLE_CHOICE",
        "options": 
        [
            {
                "value": "ADULTS ONLY"
            },
            {
                "value": "MINORS ONLY"
            },
            {
                "value": "ANY AGES"
            }
        ]
    })

    form = service.forms().create(body=form).execute()
    return form

def get_form_responses(creds, form_id):
    service = build('forms', 'v1', credentials=creds)
    response = service.forms().get(formId=form_id).execute()
    return response