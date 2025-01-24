import React, { useState } from "react";
import {
  FileUploaderDropContainer,
  Button,
  Loading,
  TextInput,
  ProgressIndicator,
  ProgressStep,
  RadioButtonGroup,
  RadioButton,
  TextArea
} from "@carbon/react";
import "./FileUpload.scss";
import Result from "../Result/Result";


// Inside the FileUpload functional component, `const` declarations are used with the useState hook to define state variables and their corresponding setter functions. 

function FileUpload() {
  const [gotResponse, setGotResponse] = useState(false);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);
  // const [selectedLanguage, setSelectedLanguage] = useState('');
  // const [recipientEmail, setRecipientEmail] = useState('');
  const [querySearch, setQuerySearch] = useState("");
  const [queryResult, setQueryResult] = useState('');
  const [progress, setProgress] = useState(0);
  const [translateToSpanish, setTranslateToSpanish] = useState(false);
  const [translateToPortuguese, setTranslateToPortuguese] = useState(false);
  const [translateToJapanese, setTranslateToJapanese] = useState(false);
  const [translateToFrench, setTranslateToFrench] = useState(false);
  const [language, setLanguage] = useState("english");
  const [newUrl, setNewUrl] = useState(null);
  const [fileUrl, setFileUrl] = useState(null);
  const [prevUrl, setPrevUrl] = useState(null);
  const [englishSummary, setEnglishSummary] = useState("");
  const [click, setClick] = useState(false);
  const [momGenerated, setMomGenerated] = useState("");


  // This function handles the file upload event by extracting the uploaded file from the event object, creating a URL for the uploaded file, and updating relevant state variables for further processing.

  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    console.log("uploadedFile", uploadedFile);
    if (uploadedFile) {
      const url = URL.createObjectURL(uploadedFile);
      setFileUrl(url);
      setPrevUrl(url);
      setFile(uploadedFile);
      setGotResponse(false);
      setResult("");
      setProgress(1); // Progress updated for file upload step
      console.log(url);
    }
  };

  async function postData(url) {
    console.log("calling url -- >", url);
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    setProgress((progress) => progress + 1);
    console.log("Result -- >", response);
    if (url === "http://127.0.0.1:8000/query_search/") {
      return response;
    }
    return response.json();
  }

  // Supports respective Language Translations
  const handleLanguageChange = (value) => {
    if (value == "spanish") {
      setTranslateToSpanish(true);
      setTranslateToPortuguese(false);
      setTranslateToJapanese(false);
      setTranslateToFrench(false);
      setLanguage("spanish");

    } else if (value == "portuguese") {
      setTranslateToSpanish(false);
      setTranslateToPortuguese(true);
      setTranslateToJapanese(false);
      setTranslateToFrench(false);
      setLanguage("portuguese");

    } else if (value == "japanese") {
      setTranslateToSpanish(false);
      setTranslateToPortuguese(false);
      setTranslateToJapanese(true);
      setTranslateToFrench(false);
      setLanguage("japanese");

    } else if (value == "french") {
      setTranslateToSpanish(false);
      setTranslateToPortuguese(false);
      setTranslateToJapanese(false);
      setTranslateToFrench(true);
      setLanguage("french");
    
    } else {
      setTranslateToSpanish(false);
      setTranslateToPortuguese(false);
      setTranslateToJapanese(false);
      setTranslateToFrench(false);
      setLanguage("english");
    }
  };

  const handleButtonClick = async () => {
    setResult("");
    if (file) {
      setLoading(true);
      setGotResponse(true);
      setProgress(1); // Assuming next step in the process
      console.log("Uploading file...");

      const formData = new FormData();
      formData.append("file", file);
      // console.log(selectedLanguage)
      // formData.append('language', selectedLanguage); // Use selectedLanguage for the API request

      formData.append("translate_to_spanish", translateToSpanish);
      formData.append("translate_to_portuguese", translateToPortuguese);
      formData.append("translate_to_japanese", translateToJapanese);
      formData.append("translate_to_french", translateToFrench);

      console.log("Sending API request...");
      try {
        const response = await fetch("http://127.0.0.1:8000/UploadFile/", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          console.log("Response:", response);
          const response2 = await postData("http://127.0.0.1:8000/summary/");
          console.log(response2);
          // let resultString = await response.text().then(text => text.replace(/^"|"$/g, ''));

          // For hiding the results to get reflected in the summary
          // setResult(response2.summary);

          setEnglishSummary(response2.summary);
          console.log("Response 2:", response2);
          if (response2 && response2.ok) {
            setProgress(progress + 1);
            setLoading(false);
          }
        }
        if (language !== "english") {
          setLoading(true);
          console.log("language", language);
          // translation should work
          const response = await fetch("http://127.0.0.1:8000/generate_mom/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              language: language,
              summary: englishSummary,
            }),
          });

          if (response.ok) {
            console.log("Response:", response);

            const resultString = await response.json();
            // const resultString = await response.text().then(text => text.replace(/^"|"$/g, ''));
            // setResult(resultString.mom.text().then(text => text.replace(/^"|"$/g, ''));

            setResult(resultString.mom); // mom value needs to be set (this is a dictionary in the form of key:value pair and we have to just set the value. If we set  the dictionary, then the entre html will also display in the output)
            // setProgress(progress+1); // Assuming this is the progress step after generating the result
            setProgress(5);
            setMomGenerated(true)
          } else {
            console.error("Server error:", response);
          }
        } else {
          console.log("language", language);
          // translation should not work
          const response = await fetch("http://127.0.0.1:8000/generate_mom/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              language: "english",
              summary: englishSummary,
            }),
          });

          if (response.ok && response.ok) {
            console.log("Response:", response);
            const resultString = await response.json();
            console.log(resultString);
            // const resultString = await response.text().then(text => text.replace(/^"|"$/g, ''));
            setResult(resultString.mom);
            setProgress(4);
            setMomGenerated(true)
            console.log();
          } else {
            console.error("Server error:", response);
          }
        }
      } catch (error) {
        console.error("MOM Generation failed:", error);
      } finally {
        setLoading(false);
      }
    }
  };

  // For handling cancellation feature for the respective button.
  const handleCancellation = () => {
    setFile(null);
    setLoading(false);
    setFileUrl(null);
    setProgress(0);
    setGotResponse(false);
    setResult("");
    setClick(false);
    setLanguage("");
    setQuerySearch(""); // Reset the query search input
    setMomGenerated(false);
  };

  // For E - Mail Functionality
  // const handleEmailSend = async () => {
  //   setLoading(true);
  //   try {
  //     const response = await fetch('http://127.0.0.1:8000/send_email', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify({
  //         recipient_email: recipientEmail,
  //         subject: 'Your MOM',
  //         message: result, // Assuming result contains the MOM content
  //         password: 'your_outlook_password_here', // Replace with Outlook password
  //       }),
  //     });

  //     if (response.ok) {
  //       console.log('Email sent successfully');
  //     } else {
  //       console.error('Failed to send email:', response);
  //     }
  //   } catch (error) {
  //     console.error('Error sending email:', error);
  //   }
  //   setLoading(false);
  // };


  // For handling Query Search (RAG)
  const handleQuerySearch = async (question) => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/query_search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: querySearch,
          // message: result, // could be an error out here
        }),
      }
      );

      const data = await response.json(); // Assuming the server responds with JSON


  //     if (response.ok) {
  //       console.log("Query processed successfully");
  //       setQueryResult(data.message); // Update the queryResult state with the response
  //     } else {
  //       console.error("Failed to process query:", response);
  //       setQueryResult('Failed to process query'); // Provide feedback in case of failure
  //     }
  //   } catch (error) {
  //     console.error("Error processing query:", error);
  //     setQueryResult('Error processing query'); // Provide feedback in case of an exception
  //   }
  //   setLoading(false);
  // };


    if (response.ok) {
      console.log("Query processed successfully");
      setQueryResult(data.answer); // Update the queryResult state with the response
    } else {
      console.error("Failed to process query:", response);
      setQueryResult('Failed to process query'); // Provide feedback in case of failure
    }
  } catch (error) {
    console.error("Error processing query:", error);
    setQueryResult('Error processing query'); // Provide feedback in case of an exception
  }
  setLoading(false);
  };
  

  return (
    <div className="Flex">
      <div className="Component1">
        <FileUploaderDropContainer
          labelText={
            file
              ? `Uploaded File: ${file.name}`
              : "Upload Webex file in .txt or .mp4 here"
          }
          multiple={false}
          accept={[".txt", ".mp4"]}
          disabled={loading}
          onAddFiles={handleFileUpload}
          filenameStatus="complete"
          style={{
            width: '400px', // Attempting to directly set the width,
            height: '65px', // and height of the FileUploaderDropContainer
            display: 'flex', // These styles might not have the intended effect
            alignItems: 'center',
            justifyContent: 'center',
            overflow: 'hidden',
            border: '1px solid #cfbcd7',
            boxSizing: 'border-box',
            backgroundColor: 'rgba(224, 224, 224, 0.8)',
            borderRadius: '4px',
          }}
        />

        {/* Replace Checkbox with RadioButtonGroup for language selection */}
        <RadioButtonGroup
          name="languageSelection"
          onChange={(value) => handleLanguageChange(value)}
          // valueSelected={selectedLanguage}
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "flex-start",
            marginTop: "2%",
          }}
        >
          <RadioButton
            labelText="Translate to Spanish"
            value="spanish"
            id="translate_to_spanish"
          />
          <RadioButton
            labelText="Translate to Portuguese"
            value="portuguese"
            id="translate_to_portuguese"
          />
          <RadioButton
            labelText="Translate to Japanese"
            value="japanese"
            id="translate_to_japanese"
          />
          <RadioButton
            labelText="Translate to French"
            value="french"
            id="translate_to_french"
          />
        </RadioButtonGroup>

        <Button
          style={{ 
            marginLeft: "5%", 
            paddingRight: "30px", 
            justifyContent: 'center', 
            alignContent: 'center',
            alignItems: 'center',
            borderRadius: '10px'
          }}
          onClick={handleButtonClick}
          disabled={loading || !file}
        >
          Generate
        </Button>

        {file && (
          <Button
            style={{ 
              marginLeft: "10%", 
              paddingRight: "45px", 
              justifyContent: 'center', 
              alignContent: 'center',
              alignItems: 'center',
              borderRadius: '10px'
            }}
            onClick={handleCancellation}
            kind="danger"
          >
            Cancel
          </Button>
        )}

        {momGenerated===true &&
              (<>
                <div className="margin-top"></div>
                      <TextInput
                        id="query_search"
                        labelText="Search your query:"
                        value={querySearch}
                        onChange={(e) => setQuerySearch(e.target.value)}
                      />

                    <Button
                      style={{  
                        width: '120px',
                        height: '30px',
                        padding: '5px 10px',
                        alignContent: 'center',
                        alignItems: 'center',
                        justifyContent: 'center',
                        borderRadius: '10px'
                      }}
                      onClick={handleQuerySearch}
                      disabled={loading || !result || !querySearch}
                    >
                      Search Query
                    </Button>
                
                    
                    {/* {result && <TextArea value={''} />} */}

                {/* Adding space above the TextArea */}
                <div style={{ marginTop: '20px' }}> {/* Adjust the margin as needed */}
                  {result && 
                    <TextArea 
                      value={queryResult} // pass the result to be displayed from the RAG Operation (QueryResults) --> f_api
                      readOnly
                      style={{
                        height: '306px', // Smaller height for the TextArea
                        overflowY: 'scroll', // Ensure it's scrollable
                        border: '1px solid #E6D1EF',
                        boxSizing: 'border-box',
                        backgroundColor: 'rgba(224, 224, 224, 0.8)',
                        textAlign: 'justify',
                        borderRadius: '4px',
                      }}
                    />
                  }
                </div>
              </> 
          )
        }
      </div>

      

      <ProgressIndicator
        className="progress"
        currentIndex={progress}
        spaceEqually={true}
        style={{ marginTop: "1%" }}
      >
        <ProgressStep
          label="Step 1"
          description="Step 1: Register a onChange event"
          secondaryLabel="Upload File"
        />
        <ProgressStep
          label="Step 2"
          description="The progress indicator will listen for clicks on the steps"
          secondaryLabel="Summary Generated"
        />
        <ProgressStep
          label="Step 3"
          description="The progress indicator will listen for clicks on the steps"
          secondaryLabel="MOM In Progress"
        />
        <ProgressStep
          label="Step 4"
          description="The progress indicator will listen for clicks on the steps"
          secondaryLabel="MOM Generated"
        />
        <ProgressStep
          label="Step 5"
          description="The progress indicator will listen for clicks on the steps"
          secondaryLabel="Language Translation"
        />

      </ProgressIndicator>

      <div className="Component2">
        {loading && <Loading className={"loading"} withOverlay={false} />}
        <Result result={result} />
      </div>
    </div>
   
  );
}

export default FileUpload;
