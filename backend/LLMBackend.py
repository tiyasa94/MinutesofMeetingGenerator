from genai import Client
from genai.credentials import Credentials
from dotenv import load_dotenv

class LLMBackendGenAI():
    """
    Implementation of the LLM call from IBM watsonx.ai on IBM Research BAM.
    """

    def __init__(self, model_id, configs = {
            "parameters": {
                "decoding_method": "greedy",
                "stop_sequences": [
                "\\n\\nPlease provide the actual"
                ],
                "include_stop_sequence": False,
                "min_new_tokens": 1,
                "max_new_tokens": 2048
            },
            "moderations": {
                "hap": {
                "threshold": 0.75,
                "input": True,
                "output": True
                },
                "stigma": {
                "threshold": 0.75,
                "input": True,
                "output": True
                }
            }
    }):
        
        """
        Initializes the Client instance, model_id and generation parameters
        Returns:
        None
        """
        
        self.params = configs['parameters']
        self.mod_params = configs['moderations']
        load_dotenv()
        creds = Credentials.from_env()
        self.client = Client(credentials=creds)
        self.model_name = model_id
        

    def summarize_prompt(self,text):
        prompt = f'''As an intelligent assistant your job is to generate comprehensive summary from a meeting transcript.                
Here are your guidelines:
- Focus on identifying the underlying intent behind each segment of the meeting, using this to categorize information more effectively. 
- Segregate key topics, action items, and next steps based on the intent expressed in the given summary. 
- Encapsulate the main ideas and discussions. 
- Maintain a context flow. 
- Interpret the intent or goal behind these tasks. 
- Reflect the future intentions or plans of the meeting participants.
Summarize the following sentence: \n{text}

Output:
'''
        return prompt

#     def mom_prompt_english(self, summary):
#         prompt = f'''As an intelligent assistant your job is to generate professional Minutes of Meeting (MOM) in HTML format from a meeting summary for a webpage.
# Here are the components to add:
# 1. Meeting details : Just mention the title of the meeting, and name of the speaker(s) attended in the meeting.
# 2. Agenda: List of topics or items to be discussed in the meeting. 
# 3. Key Notes: Detailed notes on each agenda item. Do not create hierarchical points. 
# 4. Action Items: List of tasks or actions assigned discussed in the meeting including the responsible individuals or teams with due dates. If responsible individuals or teams and due date are not mentioned in the summary, just mention list of tasks or actions assigned. Do not mention not discussed.
# 5. Next Steps: Future plans or actions to be taken and assignments for follow-up. Do not mention not discussed.
# 6. Questions & Answers : Mention key questions asked in the meeting and related answers discussed. If no questions are discussed, mention "Not discussed".
# 7. Closure and Next Meeting Date: Brief summary or conclusion, schedule for the next meeting.  If closure and next meeting date are not discussed, mention "Not discussed".
# 8. Feel free to add proper html tags for formatting like <b> tags to highlight key points and <h3> for headings 
# 9. Make sure that you generate valid html tags only not markdown.
# 10. Use ul and li for bulleted points.
# 11. Add inline styling in the html tags.
# - I want some description for all the above points if it's there in the original summary. 

# Here is your meeting summary :\n{summary} 
# '''  
#         return prompt
    





    def mom_prompt_english(self, summary):
        prompt = f'''Generate professional Minutes of Meeting (MOM) in HTML format from the provided meeting summary for a webpage. The document should be meticulously structured, ensuring that it is ready for professional presentation. Each section should be clearly defined, with important information highlighted and content organized for easy readability. Follow these detailed instructions for each component of the MOM:

        Begin with the meeting title "<div style='text-align: center; font-weight: bold; text-decoration: underline;'>title of the meeting</div>" and the names of the speakers. This title of the meeting should be bold and centered to signify its importance as the primary subject of the document. While formatting, ensure the title appears visually more prominent than the other section headings. The title should convey the meeting's main focus. All the below mentioned components should be added in the response. It is important to bold all the headers to make it more distinguishable.

        1. <b>Meeting Details:</b> Begin with the meeting title and the names of the speakers. This title of the meeting should be bold and centered to signify its importance as the primary subject of the document and should be centre aligned. Highlight these elements in bold to emphasize their importance. The title should convey the meeting's main focus, while the list of speakers should include their roles or expertise to provide context for their contributions. No need to mention the location of the meeting.

        2. <b>Agenda:</b> Itemize the topics or items that were discussed during the meeting. Use bullet points to list these items, ensuring each topic is clearly mentioned. This section should provide a roadmap of the meeting's content, giving readers an overview of the discussions.

        3. <b>Key Notes:</b> Summarize the discussion for each agenda item concisely in a single bullet point. This summary should include any significant points raised, conclusions reached, or insights shared by the participants. Aim for succinctness and coherence, integrating all critical aspects of the discussion into one comprehensive point to maintain clarity and conciseness.

        4. <b>Action Items:</b> List any tasks or actions that were assigned during the meeting, specifying the responsible individuals or teams, and including due dates if available. If certain details are not mentioned, simply list the tasks or actions. Use bullet points for clear presentation.

        5. <b>Next Steps:</b> Describe any future plans, actions to be taken, or assignments for follow-up that were agreed upon during the meeting. This section should outline the direction or objectives moving forward, providing clear guidance for participants or relevant parties.

        6. <b>Questions & Answers:</b> Summarize any key questions asked and the answers provided during the meeting. If this section does not apply, adjust the content accordingly without defaulting to "Not discussed."

        7. <b>Closure and Next Meeting Date:</b> Conclude with a brief summary of the meeting, highlighting any consensus reached or decisions made. Also, include the schedule for the next meeting if it was discussed. This provides a clear endpoint for the current meeting and sets the stage for future engagement.

        <b>Formatting Instructions:</b>
        - Utilize bold formatting (<b></b> tags) to draw attention to key elements such as section titles and important points.
        - Use bullet points (<ul> for unordered lists and <li> for list items) to organize information in the Agenda, Action Items, and other relevant sections.
        - Ensure that the HTML content is well-structured and adheres to web accessibility and readability standards, suitable for a professional environment.

        Here is your meeting summary:
        {summary}

        Transform this summary into a well-organized, clearly formatted MOM according to the guidelines provided, ensuring it is polished and ready for publication on a professional webpage.'''

        return prompt


    
#     def mom_prompt_language(self, mom_english, lang):
#         prompt = f'''Act as an English to {lang} translator. Follow the below instructions:
# 1. Ensure your {lang} translations are free from spelling mistakes and accurately maintain the original meaning from the English text. 
# 2. You should convey the precise intent of the input without incorporating any extra jargon into the translation. 
# 3. Do not produce any supplementary irrelevant text. 
# 4. Once the translation is complete, I would not want you to write any further text.
# Translate the input as directed. 

# Here is your Minutes of Meeting in English :\n{mom_english} 
# '''
#         return prompt
    


    def mom_prompt_language(self, mom_english, lang):
        prompt = f'''You are tasked with translating an English Minutes of Meeting (MOM) document into {lang}, focusing on maintaining the original HTML format. The translation must start with the `<!DOCTYPE html>` tag and end with the closing `</html>` tag, without including any additional text, comments, or annotations outside these HTML tags. Follow these guidelines closely to ensure the translation is both accurate and professionally formatted:

        1. Direct Translation Within HTML Structure: Start the translation with the `<!DOCTYPE html>` tag, and ensure the entire content, including the translated text, is contained within the `<html>` and `</html>` tags. There should be no text, annotations, or comments before the `<!DOCTYPE html>` tag or after the closing `</html>` tag.

        2. Accuracy and Professional Tone: The translation should accurately reflect the original document's meaning, tone, and content. Preserve the professional and formal tone throughout the translated document.

        3. Language Quality: Produce a grammatically correct translation using appropriate vocabulary for a professional {lang} audience, ensuring spelling and syntax are correct.

        4. Cultural Sensitivity: Adapt the content to fit cultural nuances of the target language without changing the original message's core meaning.

        5. Preserve Original Formatting: Maintain all original formatting elements, such as headings, bullet points, lists, and emphasis (bold or italic text), as they appear in the English document.

        6. Technical Terms Translation: Translate specialized terms accurately. If no direct equivalent exists in {lang}, use the most commonly accepted term or provide a brief explanation in a footnote or endnote within the HTML document.

        7. Conciseness: Include only content present in the original MOM. Do not add supplementary information or deviate from the provided material.

       your output should look like this:
        ```html
        <!DOCTYPE html>
        <html lang="{lang}">
        <head>
            <meta charset="UTF-8">
            <title>Translated Title Here</title>
        </head>
        <body>
        ...
        </body>
        </html>
        ```

        This example demonstrates starting directly with the HTML document structure. Your translation should follow this format, inserting the translated content where appropriate, and concluding the document without adding any text after the `</html>` tag.

        Now, translate the provided English MOM into {lang}, ensuring your translation adheres strictly to the instructions and example format provided:

        {mom_english}
        Translation:
        '''

        return prompt


    def rag_prompt(self, question, topn_chunks):
        prompt = ""
        prompt += 'Search results:\n'
            
        for c in topn_chunks:
            prompt += c + '\n\n'
        
        prompt += "Instructions: You are an expert in answering queries from a Minutes of Meeting (MOM) Generator. "\
                "Compose a comprehensive reply to the query using the search results given. "\
                "Only include information found in the results and "\
                "don't add any additional information. Make sure the answer is correct and don't output false content. "\
                "If the text does not relate to the query and the speaker is not present in the meeting, simply state 'Sorry, I didn't find nothing'. Ignore outlier "\
                "search results which has nothing to do with the question. Only answer what is asked. The "\
                "answer should be detailed and informative." 
        
        prompt += f"\n\n\nQuery: {question}\n\nAnswer: "
        
        return prompt



    def generate_response(self, prompt):
        if isinstance(prompt, str):
            for idx, response in enumerate(self.client.text.generation.create(model_id = self.model_name, inputs = prompt, parameters = self.params, moderations=self.mod_params)):
                # print(response)
                return response.results[0].generated_text
        
        if isinstance(prompt, list):
            outputs = []
            for idx, response in enumerate(self.client.text.generation.create(model_id = self.model_name, inputs = prompt, parameters = self.params, moderations=self.mod_params)):
                outputs.append(response.results[0].generated_text)
            return outputs
    
    def stream_response(self, prompt):
        for response in self.client.text.generation.create_stream(
        model_id=self.model_name, input=prompt, parameters=self.params, moderations=self.mod_params
    ):            
            for result in response.results:
                if result.generated_text:
                    yield result.generated_text


    # def stream_response(self, prompt):
    #     print("prompt: {}".format(prompt))
    #     for response in self.client.text.generation.create_stream(
    #     model_id=self.model_name, input=prompt, parameters=self.params, moderations=self.mod_params
    #     ):
    #         print("response: {}".format(response))            
    #         for result in response.results:
    #             if result.generated_text:
    #                 print("generated_result: {}".format(result.generated_text))
    #                 return result.generated_text