# Imports Libraries
from fastapi import FastAPI, HTTPException, status
from fastapi import UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from video_processing import video_to_text
from chunking import split_into_chunks
from summarization import generate_summary
from mom import generate_mom
from rag import rag_qna

# Creates the output folder if not already there
if not os.path.exists(os.path.join(os.getcwd(),'output')):
    os.mkdir(os.path.join(os.getcwd(),'output'))

# Defines Pydantic data models for summary and question
class LanguageSummary(BaseModel):
    language: str
    summary:str

class Query(BaseModel):
    question:str
    # message: str

# Initializes a FastAPI application
app = FastAPI()

# Adds CORS middleware to allow cross-origin requests.
# Customizes origins, methods, and headers as needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to a specific origin or origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Checks if the uploaded file in UI has mp4 signature
def is_video(content):
    # Check for MP4 signature: the file often starts with "ftyp" near the beginning
    if b'ftyp' in content[:32]:  # Look in the first 32 bytes for the 'ftyp' marker
        return True
    # Add other video signatures as needed
    return False


# Simulated storage for operation cancellation status
# This would typically be a more robust solution (e.g., database, Redis)
cancellation_status = {"cancelled": False}


@app.post("/cancel")
async def cancel_operations(data: bool):
    """
        Endpoint to cancel the ongoing operation.

        Args:
            data (bool): Boolean value indicating whether to cancel the operation.

        Returns:
            dict: A dictionary containing a message indicating the cancellation request status.
    """
    cancellation_status["cancelled"] = data #empty form value evaluates to False.
    return {"message": "Cancellation requested"}


@app.post("/UploadFile")
async def upload_file(file: UploadFile):

    """
        Endpoint to perform operation1 : Reading txt/mp4 file from UI -> extract content -> split text into chunks
        Args:
            file (UploadFile): The uploaded file to process.
        Returns:
            dict: A dictionary containing a message indicating the status of the operation.
    """

    # Read the content of the uploaded file and store its filename
    file_content = file.file.read()  
    file_name = file.filename

    # Check if cancellation status is true, if so, raise an HTTPException
    if cancellation_status["cancelled"]:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Operation cancelled")
    
    # Define paths for video and text files in the output directory
    vp = os.path.join(os.getcwd(),'output','temp.mp4')
    tp = os.path.join(os.getcwd(),'output','temp.txt')

    # Check if the uploaded file is a video
    if is_video(file_content):   
        # If it is a video, save it to disk     
        with open(vp, 'wb') as file:
            file.write(file_content)

        # Convert the video to text and split it into chunks
        res,vtp = video_to_text(vp)
        if res=='Complete':
            response = split_into_chunks(vtp)
            if response=='Complete':
                return {"message": response}      
        else:
            return {"message": 'Error in Loading transcript'}

    # If the uploaded file is a text file    
    if file_name.split('.')[-1] == 'txt':
        # Save the text file to disk
        with open(tp, 'wb') as file:
            file.write(file_content)
        # Split the text file into chunks
        response = split_into_chunks(tp)
        if response=='Complete':
            return {"message": response}



@app.get("/summary")
async def generate_summary():

    """
        Endpoint to perform operation2 : Summarizing chunks -> Collating summaries 

        Returns:
            dict: A dictionary containing a summary generated from processed chunks.
    """
    
    # Check if cancellation status is true, if so, raise an HTTPException
    if cancellation_status["cancelled"]:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Operation cancelled")
    # Define paths for chunks in the output directory
    chunks_path = os.path.join(os.getcwd(),'output','chunks.json')
    # print(chunks_path)

    # Summarize chunks and make a final summary
    response = generate_summary(chunks_path)
    # print(response)

    return {"summary": response}



@app.post("/generate_mom")
async def generate_mom(item: LanguageSummary):

    """
        Endpoint to perform operation3 : Generate MOM and translation using summary input

        Args:
            item (LanguageSummary): An instance of the LanguageSummary class containing language and summary attributes.

        Returns:
            dict: A dictionary containing the generated MOM.
    """

    # Check if cancellation status is true, if so, raise an HTTPException
    if cancellation_status["cancelled"]:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Operation cancelled")
    # Set language and summary input path for MOM and translation 
    lang = item.language
    summary = item.summary
    summaries_path = os.path.join(os.getcwd(),'output','summaries.json')

    # Generate MOM with translation if selected by the user
    mom = generate_mom(summary_path=summaries_path, lang=lang)

    start_tag = "<!DOCTYPE html>"
    end_tag = "</html>"
    if not mom.strip().startswith(start_tag):
        mom = f"{start_tag}\n{mom}"
    if not mom.strip().endswith(end_tag):
        mom = f"{mom}\n{end_tag}"

    # print("mom in operation3", mom)
    return {'mom':mom}


@app.post("/query_search")
async def query_search(query: Query):

    """
        Endpoint to perform query search.

        Args:
            query (Query): An instance of the Query class containing a question attribute.

        Returns:
            dict: A dictionary containing the answer generated from the user query.
    """

    # Check if cancellation status is true, if so, raise an HTTPException
    if cancellation_status["cancelled"]:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Operation cancelled")
    
    # Define paths for temporary text files in the output directory
    file_path = os.path.join(os.getcwd(),'output','temp.txt')
    # print(chunks_path)

    # Fetch user query
    question = query.question
    print("Making api call")

    # Generating response from the user query
    response = rag_qna(file_path, question = question)
    # print(response)
    
    return {"answer": response}