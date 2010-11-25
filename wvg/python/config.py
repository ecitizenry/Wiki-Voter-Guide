import web

# Where am I?
app_root = '/var/www/wvg/wvg/'

# Project VoteSmart API Key
api_key = ''

# Feedback email addresses
email_sender = 'support@wikivoterguide.com'
email_recipient = 'support@wikivoterguide.com'

# These variables probably don't need to be changed

app_path = app_root + '/python'
template_path = app_root + '/templates'

state_ballots = {
'NA': 'http://www.ballotpedia.org/wiki/index.php/National_2010_ballot_measures', 
'AS': 'http://www.ballotpedia.org/wiki/index.php/American_Samoa_2010_ballot_measures', 
'FL': 'http://www.ballotpedia.org/wiki/index.php/Florida_2010_ballot_measures', 
'MI': 'http://www.ballotpedia.org/wiki/index.php/Michigan_2010_ballot_measures', 
'MO': 'http://www.ballotpedia.org/wiki/index.php/Missouri_2010_ballot_measures', 
'MT': 'http://www.ballotpedia.org/wiki/index.php/Montana_2010_ballot_measures', 
'ID': 'http://www.ballotpedia.org/wiki/index.php/Idaho_2010_ballot_measures', 
'DC': 'http://www.ballotpedia.org/wiki/index.php/November_2,_2010_ballot_measures_in_Washington,_D.C.',
'GA': 'http://www.ballotpedia.org/wiki/index.php/Georgia_2010_ballot_measures', 
'HI': 'http://www.ballotpedia.org/wiki/index.php/Hawaii_2010_ballot_measures', 
'IN': 'http://www.ballotpedia.org/wiki/index.php/Indiana_2010_ballot_measures', 
'MN': 'http://www.ballotpedia.org/wiki/index.php/Minnesota_2010_ballot_measures', 
'CT': 'http://www.ballotpedia.org/wiki/index.php/Connecticut_2010_ballot_measures', 
'DE': 'http://www.ballotpedia.org/wiki/index.php/Delaware_2010_ballot_measures', 
'IA': 'http://www.ballotpedia.org/wiki/index.php/Iowa_2010_ballot_measures', 
'IL': 'http://www.ballotpedia.org/wiki/index.php/Illinois_2010_ballot_measures', 
'NC': 'http://www.ballotpedia.org/wiki/index.php/North_Carolina_2010_ballot_measures', 
'NY': 'http://www.ballotpedia.org/wiki/index.php/New_York_2010_ballot_measures', 
'PA': 'http://www.ballotpedia.org/wiki/index.php/Pennsylvania_2010_ballot_measures', 
'OH': 'http://www.ballotpedia.org/wiki/index.php/Ohio_2010_ballot_measures', 
'AK': 'http://www.ballotpedia.org/wiki/index.php/Alaska_2010_ballot_measures', 
'AR': 'http://www.ballotpedia.org/wiki/index.php/Arkansas_2010_ballot_measures', 
'CA': 'http://www.ballotpedia.org/wiki/index.php/California_2010_ballot_measures', 
'CO': 'http://www.ballotpedia.org/wiki/index.php/Colorado_2010_ballot_measures', 
'KS': 'http://www.ballotpedia.org/wiki/index.php/Kansas_2010_ballot_measures', 
'AZ': 'http://www.ballotpedia.org/wiki/index.php/Arizona_2010_ballot_measures', 
'OR': 'http://www.ballotpedia.org/wiki/index.php/Oregon_2010_ballot_measures', 
'AL': 'http://www.ballotpedia.org/wiki/index.php/Alabama_2010_ballot_measures', 
'ND': 'http://www.ballotpedia.org/wiki/index.php/North_Dakota_2010_ballot_measures', 
'RI': 'http://www.ballotpedia.org/wiki/index.php/Rhode_Island_2010_ballot_measures', 
'SC': 'http://www.ballotpedia.org/wiki/index.php/South_Carolina_2010_ballot_measures', 
'SD': 'http://www.ballotpedia.org/wiki/index.php/South_Dakota_2010_ballot_measures', 
'TX': 'http://www.ballotpedia.org/wiki/index.php/Texas_2010_ballot_measures', 
'TN': 'http://www.ballotpedia.org/wiki/index.php/Tennessee_2010_ballot_measures', 
'UT': 'http://www.ballotpedia.org/wiki/index.php/Utah_2010_ballot_measures', 
'WV': 'http://www.ballotpedia.org/wiki/index.php/West_Virginia_2010_ballot_measures', 
'WY': 'http://www.ballotpedia.org/wiki/index.php/Wyoming_2010_ballot_measures', 
'WI': 'http://www.ballotpedia.org/wiki/index.php/Wisconsin_2010_ballot_measures', 
'OK': 'http://www.ballotpedia.org/wiki/index.php/Oklahoma_2010_ballot_measures', 
'NE': 'http://www.ballotpedia.org/wiki/index.php/Nebraska_2010_ballot_measures', 
'WA': 'http://www.ballotpedia.org/wiki/index.php/Washington_2010_ballot_measures', 
'NH': 'http://www.ballotpedia.org/wiki/index.php/New_Hampshire_2010_ballot_measures', 
'ME': 'http://www.ballotpedia.org/wiki/index.php/Maine_2010_ballot_measures', 
'MD': 'http://www.ballotpedia.org/wiki/index.php/Maryland_2010_ballot_measures', 
'NM': 'http://www.ballotpedia.org/wiki/index.php/New_Mexico_2010_ballot_measures', 
'NV': 'http://www.ballotpedia.org/wiki/index.php/Nevada_2010_ballot_measures', 
'MA': 'http://www.ballotpedia.org/wiki/index.php/Massachusetts_2010_ballot_measures', 
'VT': 'http://www.ballotpedia.org/wiki/index.php/Vermont_2010_ballot_measures', 
'GU': 'http://www.ballotpedia.org/wiki/index.php/Guam_2010_ballot_measures', 
'PR': 'http://www.ballotpedia.org/wiki/index.php/Puerto_Rico_2010_ballot_measures', 
'VI': 'http://www.ballotpedia.org/wiki/index.php/Virgin_2010_ballot_measures', 
'KY': 'http://www.ballotpedia.org/wiki/index.php/Kentucky_2010_ballot_measures', 
'VA': 'http://www.ballotpedia.org/wiki/index.php/Virginia_2010_ballot_measures', 
'NJ': 'http://www.ballotpedia.org/wiki/index.php/New_Jersey_2010_ballot_measures', 
'MS': 'http://www.ballotpedia.org/wiki/index.php/Mississippi_2010_ballot_measures', 
'LA': 'http://www.ballotpedia.org/wiki/index.php/Louisiana_2010_ballot_measures'} 
