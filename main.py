from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the request body model
class CommentRequest(BaseModel):
    comment: str

# Mock sentiment analysis function
async def analyze_comment(request: CommentRequest):
    comment = request.comment.lower()

    # Basic keyword rules for mock sentiment
    if any(word in comment for word in ["love", "amazing", "great", "awesome", "excellent"]):
        sentiment = "positive"
        rating = 5
    elif any(word in comment for word in ["bad", "hate", "terrible", "awful", "poor"]):
        sentiment = "negative"
        rating = 1
    else:
        sentiment = "neutral"
        rating = 3

    return {"sentiment": sentiment, "rating": rating}

# Define the POST endpoint
@app.post("/comment")
async def comment_sentiment(request: CommentRequest):
    try:
        result = await analyze_comment(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API error: {str(e)}")