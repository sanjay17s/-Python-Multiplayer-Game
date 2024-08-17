class Room:
    def __init__(self,client1,client2):
        self.questions,self.answers = self.generate_questions()
    
    def generate_questions(self):
        return ["2+2","3+2","5+1"] , [4,5,6]
         