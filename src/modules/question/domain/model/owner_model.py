from typing import Optional

class Owner:
    def __init__(self,
                 reputation: int,
                 user_id: int,
                 user_type: str,
                 accept_rate: Optional[int],
                 profile_image: str,
                 display_name:str,
                 link:str):
        self.reputation = reputation
        self.user_id = user_id
        self.user_type = user_type
        self.accept_rate = accept_rate
        self.profile_image = profile_image
        self.display_name = display_name
        self.link = link

    def to_dict(self):
        return {
            "reputation": self.reputation,
            "user_id": self.user_id,
            "user_type": self.user_type,
            "accept_rate": self.accept_rate,
            "profile_image": self.profile_image,
            "display_name": self.display_name,
            "link": self.link
        }