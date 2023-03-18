class Users:
    def __init__(self, first, last, id, points):
        self.first_name = first
        self.last_name = last
        self.user_id = id
        self.points = points

    def __repr__(self):
        return "Users('{}','{}','{}',{})".format(self.first_name,self.last_name,self.user_id,self.points)
      
