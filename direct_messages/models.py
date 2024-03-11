from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):

    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
<<<<<<< Updated upstream
        related_name="chattingrooms",
=======
        related_name="chattingroom",
>>>>>>> Stashed changes
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
<<<<<<< Updated upstream
        related_name="messages",
=======
        related_name="message",
>>>>>>> Stashed changes
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
<<<<<<< Updated upstream
        related_name="messages",
=======
        related_name="message",
>>>>>>> Stashed changes
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
