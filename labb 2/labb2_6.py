class bilar:
    def __init__(self, vilken_bil_har_du, är_din_bil_på_eller_av ):
        self.bil=vilken_bil_har_du
        self.on_off=är_din_bil_på_eller_av

    def __str__(self):
        return f"din bil är {self.bil} och den är {self.on_off} just nu "
    
    def bilen_du_har(self):
        return f"bilen du äger är {self.bil}"

    def är_bilen_på_eller_av(self):
        if self.är_bilen_på_eller_av==True:
            return f"bilen du äger är på just nu"
        else:
            return f"bilen du äger är inte på just nu"

min_bil= bilar ( "ferari", True)

print(min_bil)
print(min_bil.bilen_du_har())
print(min_bil.är_bilen_på_eller_av())


class sports:

    def __init__(self,VIlken_sport_kör_du, hur_längr_har_du_tränat):
        self.sport=VIlken_sport_kör_du
        self.hurlängeg= hur_längr_har_du_tränat

    def __str__(self):
        return f"du tränar {self.sport} och du har tränat i  {self.hurlängeg} år "
    

    def info_om_dig(self):
        return f"du tränar {self.sport}"

    def hur_länge_du_har_tränat(self):
        return f"du har tränat i {self.hurlängeg}"

ibbe=sports("fotboll", 2)
print(ibbe)
print(ibbe.info_om_dig())
print(ibbe.hur_länge_du_har_tränat())


