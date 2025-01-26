import match_objects as mo
import google_api_calls as gac

creds = gac.get_creds()
gac.make_claims_form(creds, 3, "Discord", True, "Test Form")
gac.make_submissions_form(creds, 3, "Discord", True, "Test Form")