from GlobalControl.Config import ReadFliter_Detail_Show, ReadFliter_Detail_Show_paperID


def publicationDate_Fliter(paid,date,recentnum):
    datearrry=date.split('/')
    if len(datearrry)!=3:
        if ReadFliter_Detail_Show:
            print("in publicationDate_Fliter:")
            print("paid: "+paid+" date: "+date+" not qualified")
        return False
    else:
        year=datearrry[0]
        month=datearrry[1]
        day=datearrry[2]
        return 2023-(int)(year)<recentnum
def paperID_Fliter(paid,k):
    if not paid.isalnum():
        if ReadFliter_Detail_Show_paperID:
            print("in paperID_Fliter:")
            if paid=="":
                print("paid: none, not qualified")
            else:
                print("paid: " + paid +" not qualified")
    return paid.isalnum()
