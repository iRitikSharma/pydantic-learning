from typing import List, Optional
from pydantic import BaseModel

# Comment model that can contain replies of the SAME type (recursive model)
class Comment(BaseModel):
    id: int                     # Unique comment ID
    content: str                # Comment text
    replies: Optional[List['Comment']] = None  
    # Optional list of child comments (self-reference)

# Required to resolve forward reference ('Comment' inside Comment)
Comment.model_rebuild()

# Creating a comment with nested replies
comment = Comment(
    id=1,
    content="Hey Github",
    replies=[
        Comment(id=2, content="reply 2"),        # First reply
        Comment(id=3, content="reply 3"),        # Second reply
        Comment(id=4, content="nested reply"),   # Another reply
    ]
)

print(comment)
