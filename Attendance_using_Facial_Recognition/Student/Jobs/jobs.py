from MyApp.models import attendance
import pandas as pd
import os
import pdfkit
from .sendmail import send_email_to_person

def modify_db():
    results = attendance.objects.all().order_by('roll')
    df = pd.DataFrame()
    Roll, Name, MRec = [], [], []
    for x in results:
        Roll.append(x.roll)
        Name.append(x.name)
        MRec.append(x.mrec)
    df['Roll']=Roll
    df['Name']=Name
    df['MRec']=MRec
    df.to_csv('Results/rec.csv', index=False)
    CSV = pd.read_csv('Results/rec.csv')
    CSV.to_html('Results/rec.html')
    pdfkit.from_file('Results/rec.html', 'Results/Output.pdf')
    send_email_to_person()
    os.remove(r"Results\Output.pdf")
    os.remove(r"Results\rec.csv")
    os.remove(r"Results\rec.html")
    attendance.objects.update(mrec=0)    