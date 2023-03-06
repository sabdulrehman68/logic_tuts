class MovieInfo: 
    def __init__(self,title,year,awards,nomination,country): 
        self.title=title 
        self.year=year 
        self.awards=awards 
        self.nomination=nomination 
        self.country=country 

class Award: 
    def __init__(self,lstAward): 
        self.lstAward=lstAward 
    
    def Awardcountry(self,cyear): 
        if len(self.lstAward)==0:
            return None 
        
        else: 
            lst=[] 
            
            for i in self.lstAward: 
                if i.year==cyear:
                    if i.country!='America': 
                        lst.append(i) 
        
        return lst

    def dict_Award(self): 
        if len(self.lstAward)==0: 
            return None 
        
        else: 
            d=dict() 
            
            for i in self.lstAward: 
                srate=(i.awards/i.nomination)*100 
                srate=int(srate) 
                d[i.title]=srate 
                srted=dict(sorted(d.items(), key=lambda item: item[1],reverse=True)) 
                
        return srted 
        
n=int(input()) 
mlist=[] 
for i in range(n): 
    title=input() 
    year=int(input()) 
    awards=int(input()) 
    nomination=int(input()) 
    country=input()
    mlist.append(MovieInfo(title,year,awards,nomination,country)) 

obj=Award(mlist) 
Awardyear=int(input()) 
res1=obj.Awardcountry(Awardyear) 
if res1: 
    for i in res1: 
        print(i.title) 
        print(i.year) 
        print(i.awards)
        print(i.nomination)
        print(i.country) 

else:
    print("No Movie found") 

res2=obj. dict_Award () 

if res2: 
    for k,v in res2.items(): 
        print(k,v) 

else: 
    print("Unable to create dictionary")
