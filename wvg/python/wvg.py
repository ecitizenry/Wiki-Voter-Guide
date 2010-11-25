import web
import re
import smtplib
from web import form
from config import *
from votesmart import votesmart

votesmart.apikey = api_key

render = web.template.render(template_path, base='base')

urls = (
    '/', 'index',
    '/getraces', 'getraces',
    '/about', 'about',
    '/news', 'news',
    '/guide', 'guide',
    '/contributing', 'contributing',
    '/feedback', 'feedback',
    '/privacy', 'privacy'
)

zipform = form.Form(form.Textbox("zipplusfour"))

feedbackform = form.Form(
	form.Textbox("name"),
	form.Textbox("email"),
	form.Textbox("zipplusfour"),
	form.Textarea("feedback", form.notnull))

class index:
    def GET(self):
        return render.home('')

class about:
    def GET(self):
        return render.about()

class news:
    def GET(self):
        return render.news()

class guide:
    def GET(self):
        return render.guide()

class contributing:
    def GET(self):
        return render.contributing()

class feedback:
    def GET(self):
        form = feedbackform()
        return render.feedback(form, '')

    def POST(self):
        form = feedbackform()
	if not form.validates():
             return render.feedback(form, 'Error: No Feedback Text Received')
	else:
	     msg = "Subject: [WVG] Received Feedback\r\n" 
	     msg = msg + "\r\n" 
	     msg = msg + "Sender: " + form.d.name + "\r\n" 
	     msg = msg + "Email: " + form.d.email + "\r\n" 
	     msg = msg + "Zip: " + form.d.zipplusfour + "\r\n\r\n" 
	     msg = msg + form.d.feedback + "\r\n" 
	     server = smtplib.SMTP('localhost')
             server.sendmail(email_sender, email_recipient, msg)
             server.quit()
             return render.feedback(form, 'Feedback submitted successfully!')

class privacy:
    def GET(self):
        return render.privacy()

class getraces:
    def POST(self):
        ballotlink = ''
        form = zipform()
        if not form.validates():
            return render.home()
        else: 
            try:
                basezip = str(int(form.d.zipplusfour[0:5]))
                plusfour = str(int(form.d.zipplusfour[6:10]))
                districts = votesmart.district.getByZip(basezip, plusfour)
                elections = votesmart.election.getElectionByZip(basezip, plusfour)
                allmycandidates = list()
                allmyoffices = list()
                myelections = list()
                for election in elections:
                        election.fullname = election.name       
                        myelections.append(election)       
                #	thiselection = votesmart.election.getElection(election.electionId)
                #        for stage in thiselection.stages:
                #                  #Flush out the stage
                #                  stage.electionId = election.electionId 
                #                  stage.fullname = election.name + " (" + stage.name + ")" 
                #                  myelections.append(stage)       
                for election in myelections:
                        mycandidates = list()
                        offices = list()
                        #candidates = votesmart.candidates.getByElection(election.electionId, election.stageId)
                        candidates = votesmart.candidates.getByElection(election.electionId)
                        for candidate in candidates:
                             if candidate.electionStatus == 'Running':
                                 offices.append(candidate.electionOffice)
                                 if candidate.electionDistrictId:
                                      for district in districts:
                                           if not ballotlink:
                                                ballotlink = state_ballots[district.stateId]
                                           if candidate.electionDistrictId == district.districtId:
                                                thiscandidate = prepareCandidate(candidate) 
                                                mycandidates.append(thiscandidate)
                                 else:
                                      thiscandidate = prepareCandidate(candidate) 
                                      mycandidates.append(thiscandidate)
                        myoffices = set(offices)
                        allmyoffices.append(myoffices)
                        allmycandidates.append(mycandidates)	
                return render.getraces(myelections, allmycandidates, allmyoffices, ballotlink)
            except: 
                return render.home('Error processing your Zip+4 code. You MUST enter your Zip+4 and not just your regular 5 digit Zip code to proceed. Did you enter it correctly? (For example: 20500-0001)')


def prepareCandidate(candidate):
     if candidate.middleName and candidate.suffix: 
          candidate.ballotname = candidate.firstName + ' ' + candidate.middleName + ' ' + candidate.lastName + ' ' + candidate.suffix
     elif candidate.middleName: 
          candidate.ballotname = candidate.firstName + ' ' + candidate.middleName + ' ' + candidate.lastName
     elif candidate.suffix: 
          candidate.ballotname = candidate.firstName + ' ' + candidate.lastName + ' ' + candidate.suffix
     else:
          candidate.ballotname = candidate.firstName + ' ' + candidate.lastName
     candidate.wikiname = makeWikiName(candidate.ballotname)
     if candidate.electionParties:
         candidate.party = '(' + candidate.electionParties[0] + ')' 
     elif candidate.officeParties:
         candidate.party = '(' + candidate.officeParties[0] + ')' 
     else:
         candidate.party = ' '
     return candidate

def makeWikiName(wikiname):
      wikiname = wikiname.replace(",","")
      wikiname = re.sub("\".*\" ","",wikiname)
      wikiname = wikiname.replace(" ","_") 
      return wikiname

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
