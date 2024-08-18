class Room:
    def __init__(self,client1,client2):
        self.questions,self.answers = self.generate_questions()
        self.finished = False
        self.indexs = {client1:0,client2:0} 
    
    def generate_questions(self):
        return ["2+2","3+2","5+1"] , [4,5,6]

    def verify_ans(self,client,attempt):
        if self.finished:
            return False
        
        index = self.indexs[client]
        answer = self.answers[index]

        correct = answer == attempt
        
        if correct:
            self.indexs[client] +=1
        return correct
         