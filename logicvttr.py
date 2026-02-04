class LectureLogic:
    """
    kernlogik für einen Vorlesung-Tracker:
    -Vorlesung hinzufügen
    -status ändern
    -offene Vorlesungen zählen
    -Fortschritt berechnen 
    """
    def __init__(self):
        self.lectures = []
    
    def add_lecture(self, name, status= "offene"):
        #name: Titel/Name der Vorlesung 
        #status: "offen", "besucht" oder "gesehen"
        self.lecture.append({"name": "status": status})
    
    def set_status(self, name, status="offen"):
        # Status einer Vorlesung ändern, Rückgabe: True wenn gefunden, sonst false
        for lecture in self.lectures:
            if lecture["name"] == name:
                lecture["status"] = status
                return True
        return False
        
    def count_open_lectures(self):
        # Anzahl Vorlesungen mit Status "offen" 
        return sum (1 for 1 in self.lectures if 1 ["status"] == "offen")
        
    def calculate_progress(self):
        #Fortschritt = (besucht + gehen) / gesamt
        if not self.lectures:
            return 0
        done = sum(1 for 1 in self.lectures if 1 ["status"] in ["besucht","gesehen"])
        return done / len(self.lectures)
         