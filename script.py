import pandas as pd
from datetime import datetime
from user.models import DummyCitizenInfo
df = pd.read_csv('DummyCitizenData.csv')            
for i in range(len(df)):
    can = DummyCitizenInfo(
        name= df['Name'][i],
        father_name = df['Father Name'][i],
        mother_name = df['Mother Name'][i],
        nid = df['nid'][i],
        gender = df['gender'][i],
        email = df['Email'][i],
        phone = df['Phone Number'][i],
        area_name = df['Area Name'][i],
        ward_number = df['Ward Number'][i],
        dob = datetime.now().date(),
        elec_Worker = df['elec_Worker'][i]
    )
    can.save()